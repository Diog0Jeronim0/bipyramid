import FreeCAD, Part
from math import sqrt, sin, cos, pi

# Function to create the hexagonal bipyramid
def create_hexagonal_bipyramid():
    # Radius of the vertices around the hexagonal base
    radius = 10
    height = radius * sqrt(3)  # Height of the pyramids based on the radius of the hexagonal base

    # Vertices of the hexagonal bipyramid
    vertices = [
        FreeCAD.Vector(radius * cos(2 * pi * i / 6), radius * sin(2 * pi * i / 6), 0) for i in range(6)
    ] + [
        FreeCAD.Vector(0, 0, height),  # Top vertex
        FreeCAD.Vector(0, 0, -height)  # Bottom vertex
    ]

    # Triangular faces of the bipyramid
    faces = [
        [i, (i + 1) % 6, 6] for i in range(6)  # Upper faces
    ] + [
        [i, (i + 1) % 6, 7] for i in range(6)  # Lower faces
    ]

    # Creating the faces of the hexagonal bipyramid
    face_array = []
    for face in faces:
        wire = Part.makePolygon([vertices[i] for i in face] + [vertices[face[0]]])
        face_array.append(Part.Face(wire))

    # Creating a solid object from the faces
    shell = Part.makeShell(face_array)
    solid = Part.Solid(shell)

    # Verify the validity of the solid and add it to the FreeCAD document
    if solid.isValid():
        Part.show(solid)
    else:
        print("The solid is not valid. Check the faces and the wire construction.")

# Call the function to create the hexagonal bipyramid
create_hexagonal_bipyramid()
