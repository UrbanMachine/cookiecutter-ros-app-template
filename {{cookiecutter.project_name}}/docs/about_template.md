# Using `create-ros-app`

This repository was initialized by the [create-ros-app](https://github.com/UrbanMachine/create-ros-app) template.
This template is a everything-but-the-robot-code starter for ROS projects. It includes a Dockerfile for building ROS packages, a GitHub Actions workflow for linting and autoformatting, and a few other goodies.

This documentation walks through the features of the template, and how to use them.

**Make sure to follow the [Post-Set-Up Guide](https://github.com/UrbanMachine/create-ros-app/blob/main/README.md#post-set-up-guide) after setting up the template before diving into the features below!**

## Fancy Features

- Linting and autoformatting for python (ruff), C++ (clangformat), bash (shellcheck), and javascript (eslint)
  
  **Relevant Scripts:**
  ```shell
  poetry run lint --help
  ```
- Easily build ROS apps in an out-of-the box containerized environment, with helper scripts under the `docker/` directory.
  **Relevant Scripts:**
  ```shell
  # Run a profile specified under `launch-profiles/`
  docker/launch <profile>
  
  # Run and enter a ROS container without executing anything
  docker/run
  
  # Enter an existing ROS container to poke around
  docker/exec
  ```

## Project Structure

### `pkgs/`

The packages directory contains all the packages that are used in the project. Each package is added in the `Dockerfile`, and any new packages should be added there as well.

#### Package structure
Each package is made up of:
- A `resource` directory, which is a colcon requirement
- A `package.xml` file, which is a colcon requirement
- A `pyproject.toml`, because this project uses [colcon-poetry-ros](https://github.com/UrbanMachine/colcon-poetry-ros) to install project dependencies. Most ROS python packages use `setup.py`, but by using this plugin, we can use a modern python tool called [Poetry](https://python-poetry.org/) to manage dependencies.
- A directory for code
- A directory for tests

#### Test directories

As (arbitrary) best practice, the example node uses a test directory that follows the following structure

```shell

package_name/
├── package_name/
│   ├── __init__.py
│   ├── node.py
├── package_name_test/
│   ├── unit/ 
│   │   ├── test_node.py
│   ├── integration/
│   │   ├── test_node.py

```

Essentially, tests exist in a parallel directory to the package, and are split into `unit` and `integration` tests. The directories within `unit` and `integration` mirror the structure of the package itself, except that module names are prefixed with `test_`.

### `Dockerfile`

Feel free to edit as you like, but it's recommended to stick to editing within the sections
blocked off by `#######`. 

The Dockerfile will need to be edited in two places for each new ROS package you add:

1. Copying in the `package.xml`
2. Copying in the `pyproject.toml` and `poetry.lock`

### `.github/`

This project uses poetry for linting, and has some code for running linting and autoformatting under `.github/lint`.
Run `poetry install` then enter the shell via `poetry shell` to get access to the linting tool.

This project is based on a template, upstream changes can be found on the [template repository](https://github.com/UrbanMachine/create-ros-app).
A tool called `cruft` will alert you when there are upstream changes, and help you merge those in.
