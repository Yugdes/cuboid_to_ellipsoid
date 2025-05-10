import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_cuboid_and_ellipsoid(a, b, c, annotate_vertices=False):
    # 1. Compute half-dimensions
    hx, hy, hz = a/2, b/2, c/2

    # 2. Cuboid vertices: all combinations of (±hx, ±hy, ±hz)
    corners = np.array([[sx*hx, sy*hy, sz*hz]
                        for sx in (-1, 1)
                        for sy in (-1, 1)
                        for sz in (-1, 1)])
    
    # 3. Edges defined by index pairs into 'corners'
    edges = [
        (0, 1), (0, 2), (0, 4),
        (1, 3), (1, 5),
        (2, 3), (2, 6),
        (3, 7),
        (4, 5), (4, 6),
        (5, 7),
        (6, 7)
    ]

    # 4. Ellipsoid radii (minimal-volume circumscribing)
    k = np.sqrt(3) / 2
    rx, ry, rz = k * a, k * b, k * c

    # 5. Prepare figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 6. Plot cuboid edges
    for i, j in edges:
        xs, ys, zs = zip(corners[i], corners[j])
        ax.plot(xs, ys, zs, color='black', linewidth=1.5)

    # 7. Optionally annotate vertices
    if annotate_vertices:
        for idx, (x0, y0, z0) in enumerate(corners):
            ax.scatter(x0, y0, z0, color='red', s=20)
            # Place label slightly offset
            ax.text(x0, y0, z0, f'{idx}', color='blue', fontsize=10)

    # 8. Plot ellipsoid surface via parametric angles
    u = np.linspace(0, 2 * np.pi, 80)
    v = np.linspace(0, np.pi, 80)
    U, V = np.meshgrid(u, v)
    X_e = rx * np.sin(V) * np.cos(U)
    Y_e = ry * np.sin(V) * np.sin(U)
    Z_e = rz * np.cos(V)
    ax.plot_surface(X_e, Y_e, Z_e, rstride=4, cstride=4,
                    alpha=0.3, linewidth=0)

    # 9. Equal aspect ratio
    max_range = max(a, b, c)
    for setter in (ax.set_xlim, ax.set_ylim, ax.set_zlim):
        setter(-max_range/2, max_range/2)

    # 10. Labels & title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Cuboid {a}×{b}×{c} and its Circumscribing Ellipsoid')

    plt.show()

# Example usage:
# To plot with vertex labels, set annotate_vertices=True
if __name__ == '__main__':
    plot_cuboid_and_ellipsoid(a=10, b=50, c=1.5, annotate_vertices=True)
