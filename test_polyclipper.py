import pytest
from models import Polygon, Plane
from polyclipper import clip_polygon_by_plane


def test_diamond_polygon_convexity():
    polygon = Polygon(
        vertices=[1, 0, 0, 2, 1, 0, 1, 2, 0, 0, 1, 0],
        faces=[0, 1, 2, 0, 2, 3],
    )
    assert polygon.is_convex() is True


def test_L_polygon_convexity():
    polygon = Polygon(
        vertices=[0, 0, 0, 2, 0, 0, 2, 1, 0, 1, 1, 0, 1, 2, 0, 0, 2, 0],
        faces=[0, 1, 2, 0, 2, 3, 0, 3, 4, 0, 4, 5],
    )
    assert polygon.is_convex() is False


@pytest.mark.visual
def test_convex_diamond_clip_by_half():
    polygon = Polygon(
        vertices=[1, 0, 0, 2, 1, 0, 1, 2, 0, 0, 1, 0], faces=[0, 1, 2, 0, 2, 3]
    )
    plane = Plane(normal=[1, 0, 0], constant=1.0)
    clip_polygon_by_plane(polygon, plane, show=True)


@pytest.mark.visual
def test_L_polygon_clip():
    polygon = Polygon(
        vertices=[0, 0, 0, 2, 0, 0, 2, 1, 0, 1, 1, 0, 1, 2, 0, 0, 2, 0],
        faces=[0, 1, 2, 0, 2, 3, 0, 3, 4, 0, 4, 5],
    )
    plane = Plane(normal=[1, 0, 0], constant=1)
    clip_polygon_by_plane(polygon, plane, show=True)
