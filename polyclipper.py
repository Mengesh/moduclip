import trimesh

from models import Plane, Polygon


def clip_polygon_by_plane(polygon: Polygon, plane: Plane, show=False):
    """Returns a polygon clipped by the plane.

    :param polygon: polygon to clip
    :param plane: clipping plane
    :param show: visualize original (blue) and clipped (red) polygon using trimesh. Dev dependencies must be installed.
    :returns: clipped polygon

    """

    mesh = polygon.trimesh_polygon()

    # Slice polygon by plane
    sliced_mesh = trimesh.intersections.slice_mesh_plane(
        mesh, plane.normal, plane.point()
    )

    if show:
        mesh.visual.face_colors = [0, 0, 250, 100]
        sliced_mesh.visual.face_colors = [250, 0, 0, 100]
        trimesh.Scene([mesh, sliced_mesh]).show()

    # Get sliced polygon coordinates array
    sliced_vertices = sliced_mesh.vertices.reshape(-1).tolist()
    sliced_faces = sliced_mesh.faces.reshape(-1).tolist()

    if sliced_vertices:
        return Polygon(vertices=sliced_vertices, faces=sliced_faces)
    else:
        return polygon
