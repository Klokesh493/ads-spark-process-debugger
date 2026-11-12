# Ads Spark Process Debugger walkthrough

## Business problem

Classify common Spark process failures from synthetic log excerpts.

## Reproduce the workflow

Run `python3 agent.py example.json` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
[
  "memory"
]
```

The sample supplies these fields. `log`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.

## Regression scenario

An ordinary completion message has no known failure pattern.

`make verify` runs this scenario and compares the result with the checked-in expected JSON.
