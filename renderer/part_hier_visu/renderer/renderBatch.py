# import bpy
# import os
# import sys

# modelpath = sys.argv[6]
# pngpath = sys.argv[7]

<<<<<<< HEAD
# # bpy.ops.import_scene.obj(filepath = modelpath)
# # bpy.data.scenes['Scene'].render.filepath = pngpath
# # print('rendering')
# # bpy.ops.render.render( write_still=True)
# # print('rendered')
# # sys.exit(0) # exit python and blender
# # print('exited')
=======
bpy.context.scene.render.engine = 'CYCLES'
bpy.ops.import_scene.obj(filepath = modelpath)
bpy.data.scenes['Scene'].render.filepath = pngpath
print('rendering')
bpy.ops.render.render( write_still=True)
print('rendered')
sys.exit(0) # exit python and blender
print('exited')
>>>>>>> b0e58997cb66bbe9b956b811cb5d8365ad0118b4
