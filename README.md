<p align="center">
  <img alt="extracon" src="https://excelcoaching.com.br/wp-content/uploads/2018/01/convert-pdf-to-excel.jpg" width="250px" float="center"/>
</p>

<h1 align="center">Welcome to Extracon repository</h1>

<p align="center">
  <strong>Convert PDF files, extract informantion and generate Excel files</strong>
</p>

<p align="center">
  <a href="https://github.com/lpmatos/extracon">
    <img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/lpmatos/extracon">
  </a>

  <a href="https://github.com/lpmatos/extracon">
    <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/lpmatos/extracon">
  </a>

  <a href="https://github.com/lpmatos/extracon/stargazers">
    <img alt="GitHub Stars" src="https://img.shields.io/github/stars/lpmatos/extracon?style=social">
  </a>

  <a href="https://github.com/lpmatos/extracon/commits/master">
    <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/lpmatos/extracon">
  </a>

  <a href="https://github.com/lpmatos/extracon">
    <img alt="Repository Size" src="https://img.shields.io/github/repo-size/lpmatos/extracon">
  </a>

  <a href="https://github.com/lpmatos/extracon/blob/master/LICENSE">
    <img alt="MIT License" src="https://img.shields.io/github/license/lpmatos/extracon">
  </a>

  <a href="https://github.com/lpmatos/extracon/commits/master">
    <img alt="Docker Image CI" src="https://github.com/lpmatos/extracon/workflows/Docker%20Image%20CI/badge.svg">
  </a>
</p>

## Menu

<p align="left">
  <a href="#pre-requisites">Pre-Requisites</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#description">Description</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#variables">Environment Variables</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#how-to-contribute">How to contribute</a>
</p>

## Getting Started

If you want use this repository you need to make a **git clone**:

```bash
git clone --depth 1 https://github.com/lpmatos/extracon.git -b master
```

This will give access on your **local machine**.

## Pre Requisites

To this project you yeed:

### Requirement

* Python 3.8.
* Telegram API Token.
* Docker and Docker Compose.

### Optional 

* NPM | Yarn (package tool)
* Install Packages
  * Husky
  * Commitlint
  * Commitizen
  * Standard-Version

### Helm and Kubernetes

* Kubernetes 1.10+
* PV dynamic provisioning support on the underlying infrastructure

## How to use it?

### Locale

1. Set the application environment variables.
2. Install python packages in requirements.txt.
3. Map PDF files and run script.
4. Profit.

### Docker

1. Set the environment variables.
2. Install python packages in requirements.txt.
3. Run this script with docker-compose, Dockerfile or into your local machine with Python command.
4. Profit.

Press CTRL + C to stop it in Docker Compose or Dockerfile.

This system is fully containerised. You will need [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/) to run it.

## Description

**Extracon** consist in a python automation that extract information from PDF files and create Excel files.

## Containers

It's set at [docker-compose.yml](docker-compose.yml) the **containers** required for application execution.

**Container** | **Description** | **Dockerfile**
:---: | :---: | :---:
extracon | **Python container with the code and modules** | [Dockerfile](Dockerfile)
bot | **Telegram Bot to controll Extracon** | [Dockerfile](Dockerfile)

## Architecture

![Alt text](docs/CONVERSION.png?raw=true "Architecture")

## Environment

### Variables

| Name | Description |
|---|---|
| LOG_PATH | Log Path used to create the logger |
| LOG_FILE | Log File used to create the logger | 
| LOG_LEVEL | Log Level used to create the logger |  
| LOGGER | Logger Name used to create the logger |  
| PDF_PATH | PDF files Path |  
| EXCEL_NUMBER | Number of Excel files generated in the final of the process |  
| TELEGRAM_TOKEN | Telegram Token |  

### File

We use decouple for strict separation of settings from code. It helps us with to store parameters in .env file and properly convert values to correct data type.

Copy the file .env-example to a .env file and replace the values inside of it.

## 🐋 Development with Docker

Steps to build the Docker Image.

### Build

```bash
docker image build -t <IMAGE_NAME> -f <PATH_DOCKERFILE> <PATH_CONTEXT_DOCKERFILE>
docker image build -t <IMAGE_NAME> . (This context)
```

### Run

Steps to run the Docker Container.

* **Linux** running:

```bash
docker container run -d -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME> <COMMAND>
docker container run -it --rm --name <CONTAINER_NAME> -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME> <COMMAND>
```

* **Windows** running:

```
winpty docker.exe container run -it --rm <IMAGE_NAME> <COMMAND>
```

For more information, access the [Docker](https://docs.docker.com/) documentation or [this](docs/docker.md).

## 🐋 Development with Docker Compose

Build and run a docker-compose.

```bash
docker-compose up --build
```

Down all services deployed by docker-compose.

```bash
docker-compose down
```

Down all services and delete all images.

```bash
docker-compose down --rmi all
```

## Params

![Alt text](docs/USAGE.PNG?raw=true "Usage")

## Helm

### Organization

* **/templates** is a directory of templates that, when combined with values.
* **/templates/_helpers.tpl** file where we define custom templates.
* **/templates/NOTES.txt** OPTIONAL: A plain text file containing short usage notes.
* **/files** folder to inject external files.
* **Chart.yml** A YAML file containing information about the chart.
* **values.yml** The default configuration values for this chart.
* **README.md** OPTIONAL: A human-readable README file.

### Installing the Chart

To install the chart with the release name `my-release`:

```bash
$ helm install --name my-release extracon
```

### Deleting the Charts

Delete the Helm deployment as normal

```
$ helm delete my-release
```

Deletion of the StatefulSet doesn't cascade to deleting associated PVCs. To delete them:

```
$ kubectl delete pvc -l release=my-release,component=data
```

### Validate Helm

To valite your Helm Template you can run this command:

```bash
helm install --debug --dry-run . --generate-name
```

### Exemple Helm Answers

```yaml
deployment:
  type:
    name: servidor
    version: v2
  telegram:
    token: "5435efdjhds6709077adhhGDSHGDS"
  excel:
    number: 15
```

## Commit Lint

We all did bad commit messages. Lucky us, Conventional Commits specification exists, and with it a set of powerful tools to help us.

To enforce a standard every time we make a commit, we have husky and commitlint. Husky listen to git hooks, and we will use it to trigger the commitlint when we type a commit message.

Commitizen is a package that makes it easier to create commit messages following the previous specification.

* husky
* commitlint
* commitizen

<strong>Requirements:</strong>

> OBS: Required .git folder in project
* .git in folder
* Node
* yarn | npm

<strong>Install by default [package.json](package.json):</strong>

```cmd
yarn install
```

<strong>Manual Installment:</strong>

```cmd
yarn init -y

yarn add @commitlint/config-conventional @commitlint/cli husky commitizen -D

echo module.exports = {extends: ['@commitlint/config-conventional']} > commitlint.config.js
```

add configuration in package.json:

```json
"husky": {
    "hooks": {
        "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
    }
},
"config": {
    "commitizen": {
        "path": "./node_modules/cz-conventional-changelog"
    }
}
```

<strong>Use:</strong>

with dependencies already installed, commits that do not follow the semmantic commit rules will be automatically blocked in the development environment

```cmd
C:\>  git add .
C:\>  git commit -m "commit"


husky > commit-msg (node v12.14.0)
⧗   input: commit
✖   subject may not be empty [subject-empty]
✖   type may not be empty [type-empty]

✖   found 2 problems, 0 warnings
ⓘ   Get help: https://github.com/conventional-changelog/commitlint/#what-is-commitlint

husky > commit-msg hook failed (add --no-verify to bypass)
```

using the commitzen, previously installed, an auxiliary service will be available to build the commits

```cmd
C:\>  git add .
C:\>  npm run commit


cz-cli@4.0.3, cz-conventional-changelog@3.2.0

? Select the type of change that you're committing: (Use arrow keys)
> feat:     A new feature
  fix:      A bug fix
  docs:     Documentation only changes
  style:    Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
  refactor: A code change that neither fixes a bug nor adds a feature
  perf:     A code change that improves performance
  test:     Adding missing tests or correcting existing tests
  build:    Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
  ci:       Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs) 
  chore:    Other changes that don't modify src or test files
  revert:   Reverts a previous commit
```

## Standard version

Once you have conventional commits, you can make use of them with the next tool. Standard-version will usually do the following things:

* updates semantic version according to the scope of changes described in the commits
* updates CHANGELOG.md file with the new version and list of changes
* commits both changes and tags them with the new version

## Features

- [x] Github Actions to build and push docker image to github repository and docker hub repository.
- [x] Makefile with some short cuts for docker and docker-compose.
- [x] Helm chart to deploy this application in a Kubernetes cluster.

## How to contribute

>
> 1. Make a **Fork**.
> 2. Follow the project organization.
> 3. Add the file to the appropriate level folder - If the folder does not exist, create according to the standard.
> 4. Make the **Commit**.
> 5. Open a **Pull Request**.
> 6. Wait for your pull request to be accepted.. 🚀
>
Remember: There is no bad code, there are different views/versions of solving the same problem. 😊

## Add to git and push

You must send the project to your GitHub after the modifications

```bash
git add -f .
git commit -m "Added - Fixing somethings"
git push origin master
```

## Versioning

- [CHANGELOG](CHANGELOG.md)

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Author

👤 **Lucca Pessoa**

Hey!! If you like this project or if you find some bugs feel free to contact me in my channels:

> * Email: luccapsm@gmail.com
> * Website: https://github.com/lpmatos
> * Github: [@lpmatos](https://github.com/lpmatos)
> * LinkedIn: [@luccapessoa](https://www.linkedin.com/in/lucca-pessoa-4abb71138/)

## Show your support

Give a ⭐️ if this project helped you!

## Project Status

* ✔️ Finish

---

<p align="center">Make with ❤️ by <strong>Lucca Pessoa :wave:</p>
