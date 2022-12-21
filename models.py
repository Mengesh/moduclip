import numpy as np
import trimesh
from pydantic import BaseModel, Field, validator


class Polygon(BaseModel):
    vertices: list[float] = Field(example=[1, 0, 0, 2, 1, 0, 1, 2, 0, 0, 1, 0])
    faces: list[int] = Field(example=[0, 1, 2, 0, 2, 3])

    def trimesh_vertices(self):
        """Converts coordinates to 2d numpy array of 3d points."""
        return np.reshape(self.vertices, (-1, 3))

    def trimesh_faces(self):
        """Converts faces to 2d numpy array."""
        return np.reshape(self.faces, (-1, 3))

    def normal(self):
        """Returns polygon normal vector."""
        p = self.trimesh_vertices()
        n = np.cross(p[1] - p[0], p[2] - p[0])
        n /= np.linalg.norm(n)
        return n

    def trimesh_polygon(self):
        return trimesh.Trimesh(
            vertices=self.trimesh_vertices(), faces=self.trimesh_faces()
        )

    def is_convex(self):
        """Check if polygon is convex."""
        import shapely

        # Project vertices to XY and convert to 2D space (remove Z coordinate)
        vertices_2d = self.trimesh_vertices()[:, 0:2]

        # Create shapely polygon
        polygon_2d = shapely.Polygon(vertices_2d)

        # Check if polygon is equal to its convex hull
        return polygon_2d.equals(polygon_2d.convex_hull)

    @validator("vertices")
    def check_coordinates(cls, v):
        assert len(v) % 3 == 0, "Number of polygon coordinates must be divisible by 3."
        assert len(v) >= 9, "Polygon must have at least 3 points."

        z = v[2::3]
        assert z.count(z[0]) == len(z), "Polygon must lie in XY plane."

        return v

    @validator("faces")
    def check_faces(cls, v):
        assert len(v) % 3 == 0, "Number of faces must be divisible by 3."
        assert len(v) >= 1, "Polygon must have at least 1 face."
        return v


class Plane(BaseModel):
    normal: list[float] = Field(example=[1.0, 0, 0])
    constant: float = Field(example=0.0)

    def point(self):
        """Returns plane point."""
        return self.normal * self.constant

    @validator("normal")
    def check_coefficients(cls, n):
        assert len(n) == 3, "Plane normal must be a 3D vector."
        assert sum(n) != 0, "Plane normal must be a non-zero 3D vector."
        return n / np.linalg.norm(n)
