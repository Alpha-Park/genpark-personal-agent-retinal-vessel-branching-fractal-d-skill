# Retinal Vascular Box-Counting Fractal Dimension (Df) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of retinal microvascular box-counting fractal dimension (Df), arborization complexity, and capillary rarefaction.

```mermaid
flowchart TD
    Fundus["Retinal Fundus Image / Vessel Segmentation"] --> MultiScale["Multi-Scale Box Partitioning (Epsilon)"]
    MultiScale --> BoxCount["Occupied Box Enumeration N(Epsilon)"]
    BoxCount --> LogRegression["Linear Regression (log N vs log 1/Epsilon)"]
    LogRegression --> FractalScore["Fractal Dimension Df & Complexity Score"]
    FractalScore --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Mathematical Fractal Geometry**: Implements rigorous logarithmic box-counting and Pearson correlation validation.
- **Microvascular Aging Stratification**: Non-invasive detection of capillary rarefaction and cerebral small vessel health.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import RetinalVesselFractalDimensionClient

client = RetinalVesselFractalDimensionClient()
result = client.evaluate_fractal_dimension(
    box_sizes=[4.0, 8.0, 16.0, 32.0, 64.0, 128.0],
    box_counts=[1745, 640, 235, 86, 31, 11]
)
print("Fractal Dimension Df:", result["fractal_dimension_df"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
