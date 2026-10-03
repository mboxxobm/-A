import bpy, math
from mathutils import Vector

# ADA / FLAG // PROTOCOL — modular low-poly prototype

# Reset scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

def make_mat(name, color, metallic=0.0, roughness=0.42, emission=None):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get('Principled BSDF')
    bsdf.inputs['Base Color'].default_value = (*color, 1.0)
    bsdf.inputs['Metallic'].default_value = metallic
    bsdf.inputs['Roughness'].default_value = roughness
    if emission:
        bsdf.inputs['Emission Color'].default_value = (*emission[0], 1.0)
        bsdf.inputs['Emission Strength'].default_value = emission[1]
    return m

def assign(obj, mat):
    if obj.data and hasattr(obj.data, 'materials'):
        obj.data.materials.append(mat)
    return obj

def bevel(obj, amount=0.12, segments=3):
    mod = obj.modifiers.new('Soft bevel', 'BEVEL')
    mod.width = amount
    mod.segments = segments
    return obj

def cube(name, loc, scale, mat, bevel_amt=0.10, rot=(0,0,0)):
    bpy.ops.mesh.primitive_cube_add(location=loc, rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if bevel_amt:
        bevel(obj, bevel_amt)
    return assign(obj, mat)

def sphere(name, loc, scale, mat):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=20, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    assign(obj, mat)
    bpy.ops.object.shade_smooth()
    return obj

def cylinder_between(name, a, b, radius, mat, vertices=24):
    a, b = Vector(a), Vector(b)
    vec = b - a
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=vec.length, location=(a+b)/2)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_mode = 'QUATERNION'
    obj.rotation_quaternion = Vector((0,0,1)).rotation_difference(vec.normalized())
    assign(obj, mat)
    bevel(obj, min(radius*0.35, 0.08), 3)
    return obj

def look_at(obj, target):
    obj.rotation_euler = (Vector(target) - obj.location).to_track_quat('-Z', 'Y').to_euler()

def area_light(name, loc, energy, color, size):
    data = bpy.data.lights.new(name, 'AREA')
    data.energy = energy
    data.color = color
    data.shape = 'DISK'
    data.size = size
    obj = bpy.data.objects.new(name, data)
    bpy.context.collection.objects.link(obj)
    obj.location = loc
    look_at(obj, (0,0,4.0))
    return obj

# Materials
navy = make_mat('Ada_Armor_Navy', (0.018, 0.045, 0.090), 0.72, 0.24)
navy2 = make_mat('Ada_Armor_Blue', (0.035, 0.13, 0.25), 0.58, 0.28)
cyan = make_mat('Ada_Neon_Cyan', (0.02, 0.42, 0.55), 0.35, 0.20, ((0.03,0.75,1.0), 4.0))
lime = make_mat('Ada_Neon_Lime', (0.30, 0.75, 0.08), 0.15, 0.25, ((0.45,1.0,0.08), 3.0))
yellow = make_mat('Ada_Accent_Yellow', (0.88, 0.54, 0.05), 0.35, 0.28, ((1.0,0.38,0.02), 2.0))
hair = make_mat('Ada_Hair', (0.018, 0.028, 0.055), 0.10, 0.28)
skin = make_mat('Ada_Skin', (0.72, 0.31, 0.22), 0.0, 0.48)
black = make_mat('Ada_Visor_Black', (0.002,0.004,0.008), 0.25, 0.15)
white = make_mat('Ada_White', (0.60,0.78,0.82), 0.35, 0.22)

# Floor and neon rings
bpy.ops.mesh.primitive_plane_add(size=30, location=(0,0,0))
floor = bpy.context.object
floor.name = 'Neo Tokyo Platform'
assign(floor, make_mat('Floor', (0.004,0.009,0.020), 0.30, 0.28))
for radius, mat in [(3.2, cyan), (2.5, lime)]:
    bpy.ops.mesh.primitive_torus_add(major_radius=radius, minor_radius=0.025, major_segments=96, minor_segments=8, location=(0,0,0.025))
    assign(bpy.context.object, mat)

# Body — slightly feminine proportions
cube('Ada_Hips', (0,0,2.20), (1.05,0.60,0.42), navy2, 0.20)
cube('Ada_Waist', (0,0,2.92), (0.72,0.48,0.32), navy, 0.16)
cube('Ada_Torso', (0,0,4.02), (1.18,0.62,1.12), navy, 0.22)
sphere('Ada_Chest_Plate', (0,-0.66,4.12), (0.78,0.13,0.88), navy2)
cube('Ada_Core', (0,-0.81,4.16), (0.11,0.035,0.54), cyan, 0.025)
cube('Ada_Core_Top', (0,-0.82,4.72), (0.26,0.035,0.035), lime, 0.02)
cube('Ada_Belt', (0,-0.66,3.06), (1.02,0.10,0.12), yellow, 0.04)
for x in (-0.86, 0.86):
    cube('Ada_Belt_Light', (x,-0.79,3.08), (0.08,0.03,0.16), cyan, 0.02)

# Head, hair, face
cylinder_between('Ada_Neck', (0,0,5.00), (0,0,5.48), 0.34, skin, 20)
sphere('Ada_Head', (0,-0.03,6.36), (0.91,0.78,1.03), skin)
sphere('Ada_Hair_Cap', (0,0.10,6.96), (1.03,0.84,0.78), hair)
for i, (x, z, tilt) in enumerate([(-0.70,6.82,-0.34),(-0.40,7.04,-0.16),(0.0,7.10,0.0),(0.40,7.03,0.16),(0.70,6.82,0.34)]):
    cube('Ada_Hair_Bang_%02d' % i, (x,-0.67,z), (0.22,0.11,0.38), hair, 0.10, rot=(0,tilt,0))
for x in (-0.31, 0.31):
    sphere('Ada_Eye', (x,-0.755,6.52), (0.105,0.045,0.16), black)
    sphere('Ada_Eye_Cyan', (x,-0.797,6.52), (0.035,0.018,0.060), cyan)
    cube('Ada_Brow', (x,-0.785,6.78), (0.18,0.025,0.035), hair, 0.025, rot=(0,0,(-0.10 if x < 0 else 0.10)))
cube('Ada_Mouth', (0,-0.785,6.18), (0.20,0.024,0.028), hair, 0.02)
for x in (-0.88,0.88):
    sphere('Ada_Comms', (x,-0.02,6.42), (0.10,0.16,0.18), cyan)

# Arms, shoulders, shield, sword
for side in (-1,1):
    sphere('Ada_Shoulder', (side*1.32,0,4.72), (0.42,0.70,0.46), navy2)
    cube('Ada_Shoulder_Light', (side*1.42,-0.55,4.83), (0.10,0.03,0.25), lime, 0.03)
    cylinder_between('Ada_UpperArm', (side*1.34,0,4.46), (side*1.48,-0.02,3.58), 0.28, navy2)
    cylinder_between('Ada_Forearm', (side*1.48,-0.02,3.58), (side*1.58,-0.12,2.98), 0.24, navy)
    sphere('Ada_Glove', (side*1.58,-0.16,2.87), (0.27,0.24,0.25), black)
sphere('Ada_Shield', (-1.92,-0.40,4.05), (0.58,0.12,0.86), navy2)
cube('Ada_Shield_Core', (-1.92,-0.55,4.05), (0.08,0.025,0.42), cyan, 0.025)
cube('Ada_Shield_Core_H', (-1.92,-0.56,4.05), (0.27,0.025,0.06), lime, 0.02)
cylinder_between('Ada_Sword_Grip', (1.80,-0.20,3.02), (1.80,-0.20,3.62), 0.07, black, 16)
cube('Ada_Sword_Guard', (1.80,-0.20,3.62), (0.42,0.08,0.07), yellow, 0.025)
blade = cube('Ada_Sword_Blade', (1.80,-0.20,4.56), (0.09,0.035,0.92), cyan, 0.025)
blade.rotation_euler[1] = math.radians(-8)

# Legs, boots, skirt armor
for side in (-1,1):
    cylinder_between('Ada_Thigh', (side*0.53,0,2.12), (side*0.58,0,1.18), 0.36, navy2)
    cylinder_between('Ada_Shin', (side*0.58,0,1.18), (side*0.62,-0.02,0.42), 0.28, navy)
    cube('Ada_Boot', (side*0.62,-0.12,0.22), (0.38,0.62,0.22), black, 0.10)
    cube('Ada_Boot_Light', (side*0.62,-0.72,0.24), (0.20,0.035,0.035), cyan, 0.02)
    cube('Ada_Skirt_Panel', (side*0.62,-0.56,2.56), (0.42,0.08,0.38), navy2, 0.08, rot=(0,side*0.12,0))

# Neon halo and floor identity label
bpy.ops.mesh.primitive_torus_add(major_radius=1.56, minor_radius=0.035, major_segments=96, minor_segments=10, location=(0,0.58,6.45), rotation=(math.radians(90),0,0))
assign(bpy.context.object, cyan)
bpy.ops.mesh.primitive_torus_add(major_radius=1.28, minor_radius=0.018, major_segments=96, minor_segments=8, location=(0,0.60,6.45), rotation=(math.radians(90),0,0))
assign(bpy.context.object, lime)
curve = bpy.data.curves.new('Ada_Label_Curve', 'FONT')
curve.body = 'ADA  //  FLAG  //  PROTOCOL'
curve.align_x = 'CENTER'
curve.size = 0.38
curve.extrude = 0.012
label = bpy.data.objects.new('ADA_Label', curve)
bpy.context.collection.objects.link(label)
label.location = (0,-2.55,0.06)
label.rotation_euler = (math.radians(90),0,0)
assign(label, cyan)

# Camera and lights
cam_data = bpy.data.cameras.new('Ada_Camera')
cam = bpy.data.objects.new('Ada_Camera', cam_data)
bpy.context.collection.objects.link(cam)
cam.location = (9.2,-15.0,7.2)
cam_data.lens = 58
cam_data.sensor_width = 36
look_at(cam, (0,0,4.15))
bpy.context.scene.camera = cam
area_light('Key_Cyan', (5,-8,11), 1250, (0.20,0.70,1.0), 5.5)
area_light('Fill_Warm', (-6,-5,6), 900, (1.0,0.30,0.12), 4.0)
area_light('Rim_Lime', (4,4,9), 1500, (0.45,1.0,0.10), 3.0)
ld = bpy.data.lights.new('Front_Neon', 'POINT')
ld.energy = 180
ld.color = (0.2,0.8,1.0)
lo = bpy.data.objects.new('Front_Neon', ld)
bpy.context.collection.objects.link(lo)
lo.location = (0,-4,6)

# Render, metadata, save
scene = bpy.context.scene
scene.render.engine = 'BLENDER_EEVEE'
scene.render.resolution_x = 640
scene.render.resolution_y = 820
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.film_transparent = False
scene.render.filepath = '/Users/th/Documents/MONEYSITE-HOMEPAGE/blender_prototype_ada.png'
scene.world.color = (0.002,0.004,0.012)
scene.render.image_settings.color_mode = 'RGBA'
scene['character_code'] = 'ADA'
scene['archetype'] = 'Knight / 騎士'
scene['language_tag'] = 'ADA // PROTOCOL'
scene['status'] = 'prototype / low-poly modular rig seed'
bpy.ops.wm.save_as_mainfile(filepath='/Users/th/Documents/MONEYSITE-HOMEPAGE/blender_prototype_ada.blend')
bpy.ops.render.render(write_still=True)
