"""
Shared senator-selection logic for extract_senator_data.py and
render_brief_docx.py, so "--party ALP" / "--state QLD" / "--all" / names
mean the same thing in both places. One home for the selection rule.

Usage from a tool script:
    from _selection import parse_selection_args
    selector = parse_selection_args(sys.argv[1:])
    keys = selector.resolve(available)   # available: {key: {"party":.., "state":..}}
"""
import argparse
from dataclasses import dataclass, field


@dataclass
class Selection:
    names: list = field(default_factory=list)   # normalized senator keys, e.g. "katherine gallagher"
    party: str = None                             # party abbreviation, e.g. "ALP"
    state: str = None                              # state abbreviation, e.g. "QLD"
    all_: bool = False

    def resolve(self, available: dict, default_keys=None):
        """available: {normalized_key: {"party": ABBR, "state": ABBR}}.
        Returns the list of normalized keys matching the selection.
        If nothing was specified on the command line, falls back to default_keys
        (or every key in `available` if default_keys is None)."""
        if self.all_:
            return list(available.keys())
        if self.names:
            return self.names
        if self.party:
            return [k for k, v in available.items() if v.get("party", "").upper() == self.party.upper()]
        if self.state:
            return [k for k, v in available.items() if v.get("state", "").upper() == self.state.upper()]
        return list(default_keys) if default_keys is not None else list(available.keys())


def parse_selection_args(argv, default_names=None):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--party", default=None, help="party abbreviation, e.g. ALP, LP, AG, ON, IND")
    parser.add_argument("--state", default=None, help="state/territory abbreviation, e.g. QLD, NSW, ACT")
    parser.add_argument("names", nargs="*", help="senator name(s), e.g. \"Katherine Gallagher\"")
    args = parser.parse_args(argv)

    if sum([args.all, bool(args.party), bool(args.state), bool(args.names)]) > 1:
        raise SystemExit("Choose one selection mode: --all, --party, --state, or explicit name(s) - not a mix.")

    from_names = [n.strip() for n in args.names] if args.names else []
    return Selection(names=from_names, party=args.party, state=args.state, all_=args.all), (default_names or [])
