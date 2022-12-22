from fastapi.testclient import TestClient

from moduclip import app

client = TestClient(app)


def test_convex_polygon_clip_by_orthogonal_plane():
    body = {
        "polygon": {
            "vertices": [1, 0, 0, 2, 1, 0, 1, 2, 0, 0, 1, 0],
            "faces": [0, 1, 2, 0, 2, 3],
        },
        "plane": {
            "normal": [1, 0, 0],
            "constant": 1.0,
        },
    }
    response = client.post("/polygon-clipper-by-plane", json=body)
    assert response.status_code == 200
    assert response.json() == {
        "vertices": [1.0, 0.0, 0.0, 2.0, 1.0, 0.0, 1.0, 2.0, 0.0],
        "faces": [0, 1, 2],
    }


def test_nonconvex_L_polygon_clip():
    body = {
        "polygon": {
            "vertices": [0, 0, 0, 2, 0, 0, 2, 1, 0, 1, 1, 0, 1, 2, 0, 0, 2, 0],
            "faces": [0, 1, 2, 0, 2, 3, 0, 3, 4, 0, 4, 5],
        },
        "plane": {
            "normal": [1, 0, 0],
            "constant": 1.0,
        },
    }
    response = client.post("/polygon-clipper-by-plane", json=body)
    assert response.status_code == 422
    assert response.json() == {"detail": "Polygon must be convex."}


def test_convex_polygon_clip_by_non_orthogonal_plane():
    body = {
        "polygon": {
            "vertices": [1, 0, 0, 2, 1, 0, 1, 2, 0, 0, 1, 0],
            "faces": [0, 1, 2, 0, 2, 3],
        },
        "plane": {
            "normal": [1, 0, 1],
            "constant": 1.0,
        },
    }
    response = client.post("/polygon-clipper-by-plane", json=body)
    assert response.status_code == 422
    assert response.json() == {"detail": "Plane must be orthogonal to the polygon."}
