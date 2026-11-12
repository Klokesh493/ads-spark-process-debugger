import argparse
import json
from pathlib import Path


def evaluate(data):
    log = data["log"].lower()
    indicators = {"memory": ("outofmemoryerror", "oomkilled"),
                  "shuffle": ("fetchfailed", "shuffle fetch"),
                  "executor": ("executor heartbeat timed out",)}
    return [category for category, markers in indicators.items()
            if any(marker in log for marker in markers)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        print(json.dumps(evaluate(data), indent=2))
    except (KeyError, TypeError, ValueError, OSError) as exc:
        parser.exit(2, f"Invalid input: {exc}\n")


if __name__ == "__main__":
    main()
