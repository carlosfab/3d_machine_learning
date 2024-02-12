
import numpy as np
import open3d as o3d

# Loading and visualizing a PLY point cloud
print("Loading a PLY point cloud, printing, and rendering...")
ply_point_cloud = o3d.data.PLYPointCloud()
pcd = o3d.io.read_point_cloud(ply_point_cloud.path)

# Printing point cloud information and points array
print(pcd)
print(np.asarray(pcd.points))

# Setting visualization parameters
view_params = {
    "zoom": 0.3412,
    "front": [0.4257, -0.2125, -0.8795],
    "lookat": [2.6172, 2.0475, 1.532],
    "up": [-0.0694, -0.9768, 0.2024],
}

# Rendering the point cloud
o3d.visualization.draw_geometries([pcd], **view_params)

