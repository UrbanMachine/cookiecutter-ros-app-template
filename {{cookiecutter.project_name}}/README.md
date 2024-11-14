# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

# Project Structure

## `pkgs/`

The packages directory contains all the packages that are used in the project. Each package is added in the `Dockerfile`, and any new packages should be added there as well.

### Package structure
Each package is made up of:
- A `resource` directory, which is a colcon requirement
- A `package.xml` file, which is a colcon requirement
- A `pyproject.toml`, because this project uses [colcon-poetry-ros](https://github.com/UrbanMachine/colcon-poetry-ros) to install project dependencies. Most ROS python packages use `setup.py`, but by using this plugin, we can use a modern python tool called [Poetry](https://python-poetry.org/) to manage dependencies.
- A directory for code
- A directory for tests

### Test directories

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

## `.github/`

Linting tools and CI/CD configuration are stored in the `.github` directory. This project is based on a template, upstream changes can be found on the [template repository](https://github.com/UrbanMachine/create-ros-app).