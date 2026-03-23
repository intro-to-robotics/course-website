"""Simple workspace visualization for a planar 2-link manipulator."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def forward_kinematics(
    theta1: np.ndarray, theta2: np.ndarray, l1: float, l2: float
) -> tuple[np.ndarray, np.ndarray]:
    """Compute end-effector x,y from two joint-angle arrays."""
    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
    return x, y


def main() -> None:
    l1, l2 = 1.0, 0.8
    theta1 = np.linspace(-np.pi, np.pi, 180)
    theta2 = np.linspace(-np.pi, np.pi, 180)
    t1, t2 = np.meshgrid(theta1, theta2)

    x, y = forward_kinematics(t1, t2, l1, l2)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(x.ravel(), y.ravel(), s=2, alpha=0.25, color="#A31F34")
    ax.set_title("2-Link Planar Arm Workspace")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
