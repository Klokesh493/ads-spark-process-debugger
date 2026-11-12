# ADS Spark Process Debugger

During a Spark incident, operators need to distinguish memory, shuffle, and executor symptoms in a log excerpt before choosing a runbook.

## What I built

I built a log triage CLI that normalizes case and checks separate signatures for memory pressure, shuffle-fetch failures, and executor heartbeat timeouts. It can report several symptom categories from one excerpt.

## How it works

```mermaid
flowchart LR
    A["Spark log excerpt"]
    B["Normalize case and match signature groups"]
    C{"Known symptom present?"}
    D["Memory, shuffle, or executor categories"]
    E["Empty category list"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [agent.py](agent.py) implements the CLI and decision rules. Uses `argparse` to parse command-line options, `json` to read or write structured records, `pathlib` to read local files. |
| Make | Runs the documented example and local checks. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 agent.py example.json
```

The bundled out-of-memory excerpt produces the memory category. [Full expected output](examples/Bundled%20scenario.stdout.txt)

### Additional replay cases

- **Regression scenario** · `python3 agent.py examples/regression.json` · [Expected output](examples/Regression%20scenario.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

The categories suggest investigation paths. They do not determine root cause or execute recovery steps.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
