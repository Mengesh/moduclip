# ModuClip - PolyClipper API #

# About #

ModuClip is an API for [polyclipper.py](polyclipper.py) - a 3D polygon clipping module.

## Constraints ##

- Only clipping by plane is supported.
- Polygon must be convex\*
- Polygon must lie in XY plane
- Plane must be perpendicular to the polygon\*

\* PolyClipper does not require polygon convexity nor polygon-plane orthogonality. 
Both constraints are implemented only inside API for the completeness of the coding challenge.

## Quickstart ##

Install dependencies:

``` shell
pip install -r requirements.txt
```

or for development:

``` shell
pip install -r requirements-dev.txt
```

Start live server using [uvicorn](https://www.uvicorn.org/):

``` shell
uvicorn moduclip:app --reload
```

Inspect interactive API docs: <http://localhost:8000>

Run tests:

``` shell
pytest -k "not visual"
```

or with clipping visualisations generated by `trimesh.viewer`:

``` shell
pytest
```

## Deployment with Docker ##

Build image:

``` shell
docker build -t moduclip .
```

Run container:

``` shell
docker run -d --name moduclip -p 8089:80 moduclip
```

Or use `docker-compose`:

``` shell
docker compose up -d
```

Inspect interactive API docs: <http://localhost:8089>

# Dependencies #

PolyClipper depends on:

- [trimesh](https://trimsh.org/index.html) (3D polygon clipping)
- [shapely](https://shapely.readthedocs.io/en/stable/) (2D polygon convexity check)
- [pydantic](https://docs.pydantic.dev/) (data validation)

ModuClip is built with [FastAPI](https://fastapi.tiangolo.com/).

Both PolyClipper and ModuClip depend on polygon and plane classes defined in [models.py](models.py).
They are designed do be used seamlessly with js 3D libraries such as
[three](https://threejs.org/) and [babylon](https://www.babylonjs.com/).

# Examples #

Check [test_polyclipper.py](test_polyclipper.py) for polygon and plane instance creation examples.

Check [test_moduclip.py](test_moduclip.py) for API body requests examples.

