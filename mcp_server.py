"""
MCP Server for Retinal Vascular Box-Counting Fractal Dimension (Df) Skill.
Exposes JSON-RPC Model Context Protocol tools for microvascular arborization and fractal complexity analysis.
"""

import sys
import json
from typing import Dict, Any, List
from client import RetinalVesselFractalDimensionClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_fractal_dimension",
                "description": "Calculates retinal microvascular box-counting fractal dimension (Df), R^2 regression fit, and microvascular health score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "box_sizes": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "List of grid box sizes in pixels (e.g. [4, 8, 16, 32, 64, 128])."
                        },
                        "box_counts": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Number of occupied boxes for each size (e.g. [1620, 520, 165, 52, 16, 5])."
                        },
                        "branching_angles_deg": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "Optional list of vascular bifurcation angles in degrees."
                        },
                        "arteriolar_caliber_um": {
                            "type": "number",
                            "description": "Optional mean arteriolar caliber in micrometers."
                        }
                    },
                    "required": ["box_sizes", "box_counts"]
                }
            }
        ]
    }


def handle_request(client: RetinalVesselFractalDimensionClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_fractal_dimension":
            cal_val = args.get("arteriolar_caliber_um")
            if cal_val is not None:
                cal_val = float(cal_val)

            res = client.evaluate_fractal_dimension(
                box_sizes=list(args.get("box_sizes", [4, 8, 16, 32, 64])),
                box_counts=list(args.get("box_counts", [1600, 510, 160, 50, 15])),
                branching_angles_deg=args.get("branching_angles_deg"),
                arteriolar_caliber_um=cal_val
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = RetinalVesselFractalDimensionClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
