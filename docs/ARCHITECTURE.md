# Ads Spark Process Debugger architecture

Classify common Spark process failures from synthetic log excerpts.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
