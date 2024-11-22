# {{cookiecutter.project_name}}
{{cookiecutter.project_description}}

---

[![Test Status](https://github.com/{{cookiecutter.github_username_or_org}}/{{cookiecutter.project_name}}/workflows/Test/badge.svg?branch=main)](https://github.com/{{cookiecutter.github_username_or_org}}/{{cookiecutter.project_name}}/actions?query=workflow%3ATest)
[![Lint Status](https://github.com/{{cookiecutter.github_username_or_org}}/{{cookiecutter.project_name}}/workflows/Lint/badge.svg?branch=main)](https://github.com/{{cookiecutter.github_username_or_org}}/{{cookiecutter.project_name}}/actions?query=workflow%3ALint)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username_or_org}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username_or_org}}/{{cookiecutter.project_name}})
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)
![ROS2](https://img.shields.io/badge/ros-%230A0FF9.svg?logo=ros&logoColor=white)

---

## Running This Project

For in-depth documentation on the repository features, read the [About Template](docs/about_template.md) documentation.

### Dependencies

This project depends on [Docker](https://docs.docker.com/get-docker/), and can be accelerated using [Nvidia Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html). Install both before proceeding.

The linting tooling requires [Poetry](https://python-poetry.org/docs/) to run.

### Running the Project

To run the project, use the following command:

```shell
docker/launch {{cookiecutter.example_launch_profile}}
```

Then, open http://localhost/ on your browser to view the project logs.



---
This repository was initialized by the [create-ros-app](https://github.com/UrbanMachine/create-ros-app) template. Contributions are welcome!
