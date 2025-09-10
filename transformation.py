import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Function to build HTM
def get_htm(tx, ty, tz, rx, ry, rz):
    # Rotation around X
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(rx), -np.sin(rx)],
        [0, np.sin(rx), np.cos(rx)]
    ])

    # Rotation around Y
    Ry = np.array([
        [np.cos(ry), 0, np.sin(ry)],
        [0, 1, 0],
        [-np.sin(ry), 0, np.cos(ry)]
    ])

    # Rotation around Z
    Rz = np.array([
        [np.cos(rz), -np.sin(rz), 0],
        [np.sin(rz), np.cos(rz), 0],
        [0, 0, 1]
    ])

    # Combined rotation
    R = Rz @ Ry @ Rx

    # HTM 4x4
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = [tx, ty, tz]
    return T


# 2. Apply transformation
def transform_points(points, T):
    n = len(points)
    homog = np.hstack((points, np.ones((n, 1))))
    transformed = (T @ homog.T).T
    return transformed[:, :3]


# 3. Main Program

if __name__ == "__main__":
    # Input number of points
    n = int(input("Enter number of points: "))

    points = []
    for i in range(n):
        x, y, z = map(float, input(f"Enter point {i+1} (x y z): ").split())
        points.append([x, y, z])
    points = np.array(points)

    # Input translation
    tx, ty, tz = map(float, input("Enter translation (tx ty tz): ").split())

    # Input rotation angles (in degrees)
    rx, ry, rz = map(float, input("Enter rotation angles (θx θy θz) in degrees: ").split())

    # Convert to radians
    rx, ry, rz = np.radians([rx, ry, rz])

    # Build HTM
    T = get_htm(tx, ty, tz, rx, ry, rz)

    # Transform points
    transformed_points = transform_points(points, T)

    # 4. Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', label="Original")
    ax.scatter(transformed_points[:, 0], transformed_points[:, 1], transformed_points[:, 2], c='r', label="Transformed")

    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    ax.legend()
    plt.show()
