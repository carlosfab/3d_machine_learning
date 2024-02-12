
import numpy as np
import open3d as o3d

# Loading and visualizing a PLY point cloud
print("Loading a PLY point cloud, printing, and rendering...")
ply_point_cloud = o3d.data.PLYPointCloud()
pcd = o3d.io.read_point_cloud(ply_point_cloud.path)

# Applying voxel downsampling
downpcd = pcd.voxel_down_sample(voxel_size=0.05)

print("Recomputing normals for the downsampled point cloud")

# Estimating normals for the downsampled point cloud
downpcd.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30)
)

# Visualization parameters for displaying normals
normals_view_params = {
    "zoom": 0.3412,
    "front": [0.4257, -0.2125, -0.8795],
    "lookat": [2.6172, 2.0475, 1.532],
    "up": [-0.0694, -0.9768, 0.2024],
    "point_show_normal": True,
}

# Rendering the downsampled point cloud with normals
o3d.visualization.draw_geometries([downpcd], **normals_view_params)
