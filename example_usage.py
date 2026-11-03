"""
Example Usage: Retinal Vascular Box-Counting Fractal Dimension (Df) Evaluation.
Demonstrates space-filling microvascular complexity and arborization analysis.
"""

from client import RetinalVesselFractalDimensionClient


def main():
    client = RetinalVesselFractalDimensionClient()
    print("=== Retinal Vascular Box-Counting Fractal Dimension (Df) Demo ===")

    # Test Case 1: Healthy normal retinal microvascular tree
    # Box sizes: 4, 8, 16, 32, 64, 128 px
    # Box counts reflecting Df ~ 1.45
    sizes = [4.0, 8.0, 16.0, 32.0, 64.0, 128.0]
    counts_normal = [1745, 640, 235, 86, 31, 11]
    angles_normal = [74.5, 76.0, 73.0, 78.0, 75.2]

    res1 = client.evaluate_fractal_dimension(
        box_sizes=sizes,
        box_counts=counts_normal,
        branching_angles_deg=angles_normal,
        arteriolar_caliber_um=96.5
    )
    print("\nTest Case 1: Healthy Microvascular Arborization")
    print(f"  Fractal Dimension (Df): {res1['fractal_dimension_df']}")
    print(f"  R^2 Regression Fit: {res1['r_squared_fit']}")
    print(f"  Mean Branching Angle: {res1['mean_branching_angle_deg']} deg (Deviation: {res1['murray_angle_deviation_deg']} deg)")
    print(f"  Complexity Score: {res1['microvascular_complexity_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Microvascular rarefaction (Pruned capillary network)
    # Counts reflecting lower slope Df ~ 1.28
    counts_pruned = [850, 360, 150, 65, 28, 12]
    res2 = client.evaluate_fractal_dimension(
        box_sizes=sizes,
        box_counts=counts_pruned
    )
    print("\nTest Case 2: Microvascular Rarefaction Pattern")
    print(f"  Fractal Dimension (Df): {res2['fractal_dimension_df']}")
    print(f"  R^2 Fit: {res2['r_squared_fit']}")
    print(f"  Complexity Score: {res2['microvascular_complexity_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
