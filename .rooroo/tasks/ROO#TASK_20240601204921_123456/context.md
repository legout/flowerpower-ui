The user wants to refactor the `FlowerPowerProjectManager` class located in [`app/main.py`](app/main.py).

Add the following methods to the `FlowerPowerProjectManager` class:

- `load_project`: This method should load a flowerpower project from a filesystem (could be local, s3, github or any `fsspec` compatible filesystem).
- `new_project`: This method should create a new flowerpower project on any writable filesystem.

Use your deep knowledge about `FlowerPower` and `fsspec` to implement these methods correctly.