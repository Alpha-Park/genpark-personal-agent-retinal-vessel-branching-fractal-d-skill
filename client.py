"""
Retinal Vascular Box-Counting Fractal Dimension (Df) & Microvascular Complexity Engine.
Provides deterministic, zero-dependency modeling of vascular fractal dimension,
Murray's Law bifurcation optimality, and systemic microvascular rarefaction kinetics.
"""

import math
from typing import Dict, Any, List, Optional


class RetinalVesselFractalDimensionClient:
    """
    Deterministic client for calculating retinal microvascular fractal dimension (Df).
    Uses logarithmic box-counting linear regression to assess microvascular complexity,
    geometric arborization efficiency, and cerebral small-vessel health.
    """

    def __init__(self):
        pass

    def evaluate_fractal_dimension(
        self,
        box_sizes: List[float],
        box_counts: List[int],
        branching_angles_deg: Optional[List[float]] = None,
        arteriolar_caliber_um: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculates fractal dimension Df via slope of log(N) vs log(1/box_size).
        Healthy human retinal vascular tree Df is typically 1.40 - 1.50.
        """
        n = len(box_sizes)
        if n < 3 or n != len(box_counts):
            return {"error": "box_sizes and box_counts must contain at least 3 matching elements"}

        x_vals = []
        y_vals = []
        for s, c in zip(box_sizes, box_counts):
            if s <= 0 or c <= 0:
                return {"error": "Box sizes and box counts must be strictly positive"}
            x_vals.append(math.log(1.0 / float(s)))
            y_vals.append(math.log(float(c)))

        # Linear regression: slope = (n*sum(xy) - sum(x)*sum(y)) / (n*sum(x^2) - (sum(x))^2)
        sum_x = sum(x_vals)
        sum_y = sum(y_vals)
        sum_xy = sum(x * y for x, y in zip(x_vals, y_vals))
        sum_x2 = sum(x * x for x in x_vals)
        sum_y2 = sum(y * y for y in y_vals)

        denom = (n * sum_x2 - sum_x * sum_x)
        if abs(denom) < 1e-9:
            return {"error": "Degenerate box size distribution"}

        slope = (n * sum_xy - sum_x * sum_y) / denom
        df = round(slope, 3)

        # R^2 correlation calculation
        ss_tot = sum_y2 - (sum_y * sum_y) / n
        ss_res = sum((y - ((slope * x) + ((sum_y - slope * sum_x) / n))) ** 2 for x, y in zip(x_vals, y_vals))
        r2 = round(1.0 - (ss_res / ss_tot) if ss_tot > 0 else 1.0, 3)

        # Average branching angle if available (Murray's Law optimal bifurcation is ~75.0 deg)
        mean_angle = None
        angle_deviation = None
        if branching_angles_deg and len(branching_angles_deg) > 0:
            mean_angle = round(sum(branching_angles_deg) / len(branching_angles_deg), 1)
            angle_deviation = round(abs(mean_angle - 75.0), 1)

        # Microvascular Complexity Score (0 - 100):
        # Target Df 1.41 - 1.49 -> 88 - 98.
        # Df < 1.34 -> < 50 (Microvascular pruning / rarefaction).
        if 1.41 <= df <= 1.49:
            score = 90.0 + min(10.0, (df - 1.41) * 12.5)
        elif 1.36 <= df < 1.41:
            score = 75.0 + ((df - 1.36) / 0.05) * 15.0
        elif 1.49 < df <= 1.54:
            score = 75.0 + ((1.54 - df) / 0.05) * 15.0
        elif df < 1.36:
            score = max(5.0, 75.0 - (1.36 - df) * 200.0)
        else:
            score = max(10.0, 75.0 - (df - 1.54) * 150.0)

        complexity_score = round(min(100.0, max(5.0, score)), 1)

        if 1.40 <= df <= 1.50:
            tier = "OPTIMAL_MICROVASCULAR_FRACTAL_COMPLEXITY"
            interp = f"Ideal space-filling fractal dimension (Df {df}, R^2 {r2}); preserved vascular arborization and microvascular density."
            guidance = "Optimal microvascular network topology. Excellent cerebral-retinal microcirculatory health."
        elif 1.35 <= df < 1.40:
            tier = "EARLY_MICROVASCULAR_SPARSITY"
            interp = f"Mild loss of fine vascular branches (Df {df}); early subtle rarefaction pattern."
            guidance = "Incorporate regular Zone 2 aerobic cardio and dietary nitrate sources (e.g. beetroot, leafy greens) to support endothelial nitric oxide."
        elif df < 1.35:
            tier = "MICROVASCULAR_RAREFACTION_PRUNING"
            interp = f"Marked reduction in fractal complexity (Df {df} < 1.35); significant pruning of capillary beds associated with vascular aging."
            guidance = "Microvascular rarefaction detected. Evaluate blood pressure variability, glycemic control, and consult ophthalmology/cardiology."
        else:
            tier = "ABERRANT_HYPERVASCULAR_PROLIFERATION"
            interp = f"Excessive fractal branching density (Df {df} > 1.52); points to chaotic neovascularization or microvascular tortuosity."
            guidance = "Pathological vascular branching pattern. Recommend comprehensive retinal fundus fluorescein imaging."

        return {
            "fractal_dimension_df": df,
            "r_squared_fit": r2,
            "box_sizes_evaluated": box_sizes,
            "mean_branching_angle_deg": mean_angle,
            "murray_angle_deviation_deg": angle_deviation,
            "arteriolar_caliber_um": arteriolar_caliber_um,
            "microvascular_complexity_score": complexity_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
