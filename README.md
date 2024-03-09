# Tesk task Model with [FastAPI](https://fastapi.tiangolo.com/) and [Docker](https://www.docker.com/)

## How to run
  * Install and run Docker
  * Build Docker Image with `docker build . -t model`
  * Run Docker container using `docker --rm -it -p 80:80 model` 
  * Go to `http://127.0.0.1:80`

## Source code
 * [model.py](model.py) train model using train dataset
 * [server.py](server.py) contains API logic
 * [Dockerfile](Dockerfile) describes a Docker image
