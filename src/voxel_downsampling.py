
import numpy as np
import open3d as o3d

print("Downsampling the point cloud with a voxel size of 0.05")

# Loading and visualizing a PLY point cloud
print("Loading a PLY point cloud, printing, and rendering...")
ply_point_cloud = o3d.data.PLYPointCloud()
pcd = o3d.io.read_point_cloud(ply_point_cloud.path)

# Applying voxel downsampling
downpcd = pcd.voxel_down_sample(voxel_size=0.05)

# Setting visualization parameters for the downsampled point cloud
downsample_view_params = {
    "zoom": 0.3412,
    "front": [0.4257, -0.2125, -0.8795],
    "lookat": [2.6172, 2.0475, 1.532],
    "up": [-0.0694, -0.9768, 0.2024],
}

# Rendering the downsampled point cloud
o3d.visualization.draw_geometries([downpcd], **downsample_view_params)
