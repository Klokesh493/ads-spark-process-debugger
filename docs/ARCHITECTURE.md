# Ads Spark Process Debugger architecture

Classify common Spark process failures from synthetic log excerpts.

```mermaid
flowchart LR
    N0["example.json"]
    N1["agent.py"]
    N2["Match log evidence against known failure patterns."]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
