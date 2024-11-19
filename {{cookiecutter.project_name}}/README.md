# {{cookiecutter.project_name}}
{{cookiecutter.project_description}}

---

[![Test Status](https://github.com/{{cookiecutter.github_org}}/{{cookiecutter.project_name}}/workflows/Test/badge.svg?branch=main)](https://github.com/{{cookiecutter.github_org}}/{{cookiecutter.project_name}}/actions?query=workflow%3ATest)
[![Lint Status](https://github.com/{{cookiecutter.github_org}}/{{cookiecutter.project_name}}/workflows/Lint/badge.svg?branch=main)](https://github.com/{{cookiecutter.github_org}}/{{cookiecutter.project_name}}/actions?query=workflow%3ALint)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_org}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_org}}/{{cookiecutter.project_name}})
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://timothycrosley.github.io/isort/)

---

## Running This Project

For in-depth documentation on the repository features, read the [About Template](docs/about_template.md) documentation.

### Dependencies

This project depends on [Docker](https://docs.docker.com/get-docker/), and can be accelerated using [Nvidia Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html). Install both before proceeding.

### Running the Project

To run the project, use the following command:

```shell
docker/launch {{cookiecutter.example_launch_profile}}
```

Then, open http://localhost/ on your browser to view the project logs.



---
This repository was initialized by the [create-ros-app](https://github.com/UrbanMachine/create-ros-app) template. Contributions are welcome!

# TODO: Add 'how to run' instructions
# TODO: Explain steps for adding a new package
# TODO: Find out if node helpers doesn't work still w/o cyclone and put an issue in the Dockerfile

# TODO: In the main readme document running the project and viewing logs
#       Depencencies: docker
#       To run: `docker/launch cool-project` then open `localhost` on your browser
#       The username & password for editing the logs dashboard is `admin` 