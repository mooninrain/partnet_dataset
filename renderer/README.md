# Blender Part Hierarchy Renderer
This repo contains code to generate html visualization for the final annotated hierarchical segmentation results. For example, check

        http://download.cs.stanford.edu/orion/partnet_dataset/data_v0/2230/tree_hier.html

To run the code, use

        cd part_hier_visu
        bash gen_mask.sh [dir_path]

Replace `[dir_path]` to the folder that contains the downloaded annotation record.

Visualization is at `sample_data/tree_hier.html`.

The codebase depends on Blender and some regular python dependencies. Please download Blender here

        https://www.blender.org/download/


/data/vision/billf/object-properties/dataset/billf-6/ShapeNetCore.v1/02691156/fff513f407e00e85a9ced22d91ad7027/model.obj