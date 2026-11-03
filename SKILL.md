---
name: genpark-personal-agent-retinal-vessel-branching-fractal-d-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for evaluating retinal microvascular box-counting fractal dimension (Df), vascular complexity, and capillary rarefaction.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Retinal Vascular Box-Counting Fractal Dimension (Df) Skill

A sovereign personal agent capability for evaluating microvascular geometric arborization, space-filling fractal dimension ($D_f$), and detecting microvascular rarefaction linked to cognitive decline and cardiovascular wear.

## Core Capabilities
- **Box-Counting Linear Regression**: Calculates Hausdorff fractal dimension ($D_f$) across multi-scale grid partitions.
- **Goodness-of-Fit Validation**: Evaluates regression coefficient ($R^2$) to verify scale-invariance.
- **Bifurcation Optimality**: Audits vascular branching junction angles against Murray's minimum-work principle (~75.0 deg).
- **Vascular Lifestyle Pacing**: Provides targeted lifestyle guidance on aerobic nitric oxide promotion and microcirculatory conditioning.

## Fast Invocation
```python
from client import RetinalVesselFractalDimensionClient

client = RetinalVesselFractalDimensionClient()
res = client.evaluate_fractal_dimension(
    box_sizes=[4.0, 8.0, 16.0, 32.0, 64.0, 128.0],
    box_counts=[1745, 640, 235, 86, 31, 11]
)
print("Fractal Dimension Df:", res["fractal_dimension_df"])
print("Complexity Score:", res["microvascular_complexity_score"])
```
