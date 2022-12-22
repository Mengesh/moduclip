import numpy as np
from fastapi import FastAPI, HTTPException

import polyclipper
from models import Plane, Polygon

app = FastAPI(
    title="ModuClip",
    description="API for PolyClipper - a polygon clipping module",
    docs_url="/",
)


@app.post("/polygon-clip-by-plane")
async def clip_polygon_by_plane(polygon: Polygon, plane: Plane):
    """Returns a polygon clipped by the plane"""

    """
    NOTE: These exceptions are not required by the clipper.
          They are here because of the completeness of the challenge.
          Though the challenge says that this CAN be assumed,
          and not that this MUST be assumed.
    """

    if polygon.is_convex() is False:
        raise HTTPException(status_code=422, detail="Polygon must be convex.")

    if np.dot(polygon.normal(), plane.normal) != 0.0:
        raise HTTPException(
            status_code=422, detail="Plane must be orthogonal to the polygon."
        )

    return polyclipper.clip_polygon_by_plane(polygon, plane)
