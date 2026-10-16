"""Command-line interface: stackup <csv file> --lower <mm> --upper <mm>."""

import argparse

import pandas as pd

from stackup.core import calc_rss, calc_worst_case, simulate_gaps, calc_pct_out_of_spec
from stackup.plots import plot_gap_histogram


def check_range(min_gap, max_gap, lower_limit, upper_limit):
    """Return "PASS" if the whole range is inside the requirement, otherwise "FAIL"."""
    if min_gap >= lower_limit and max_gap <= upper_limit:
        return "PASS"
    return "FAIL"


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Tolerance stack-up calculator: worst case, RSS and Monte Carlo."
    )
    parser.add_argument("stack_file", help="CSV file with name, nominal, plus_tol, minus_tol, direction")
    parser.add_argument("--lower", type=float, required=True, help="lower gap limit (mm)")
    parser.add_argument("--upper", type=float, required=True, help="upper gap limit (mm)")
    parser.add_argument("--samples", type=int, default=100_000, help="Monte Carlo samples (default: 100000)")
    parser.add_argument("--distribution", choices=["normal", "uniform"], default="normal",
                        help="part distribution for Monte Carlo (default: normal)")
    parser.add_argument("--seed", type=int, default=42, help="random seed (default: 42)")
    parser.add_argument("--plot", default=None, help="save a histogram of the simulated gaps to this file")
    args = parser.parse_args(argv)

    # load csv and define arrays
    df = pd.read_csv(args.stack_file)
    nominals = df["nominal"].to_numpy()
    plus_tols = df["plus_tol"].to_numpy()
    minus_tols = df["minus_tol"].to_numpy()
    directions = df["direction"].to_numpy()

    # calculate limits, gaps, pct out
    wc_limits = calc_worst_case(nominals, plus_tols, minus_tols, directions)
    rss_limits = calc_rss(nominals, plus_tols, minus_tols, directions)
    gaps = simulate_gaps(nominals, plus_tols, minus_tols, directions,
                         n_samples=args.samples, seed=args.seed, distribution=args.distribution)
    pct_out = calc_pct_out_of_spec(gaps, args.lower, args.upper)

    # min/max gaps and result
    min_gap_wc, max_gap_wc = wc_limits
    min_gap_rss, max_gap_rss = rss_limits
    wc_result = check_range(min_gap_wc, max_gap_wc, args.lower, args.upper)
    rss_result = check_range(min_gap_rss, max_gap_rss, args.lower, args.upper)

    # print results
    print(f"Stack:        {args.stack_file} ({len(df)} dimensions)")
    print(f"Requirement:  {args.lower:.3f} to {args.upper:.3f} mm")
    print(f"Worst case:   {min_gap_wc:.3f} to {max_gap_wc:.3f} mm  {wc_result}")
    print(f"RSS:          {min_gap_rss:.3f} to {max_gap_rss:.3f} mm  {rss_result}")
    print(f"Monte Carlo:  {pct_out:.3f}% outside the requirement "
          f"({args.samples:,} samples, {args.distribution} parts, seed {args.seed})")

    # plot
    if args.plot:
        title = f"Simulated gap ({args.samples:,} assemblies, {args.distribution} parts)"
        fig, ax = plot_gap_histogram(gaps, args.lower, args.upper, rss_limits, wc_limits, title)
        fig.savefig(args.plot, dpi=150, bbox_inches="tight")
        print(f"Histogram saved to {args.plot}")


if __name__ == "__main__":
    main()
