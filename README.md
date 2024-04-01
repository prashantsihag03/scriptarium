# Scriptarium

This repo holds bunch of automation scripts.

## Execution

Apart from standalone execution of script, there are two different types of execution:

1. Dockerised
2. As a Launch Item on MacOS

For setting up each automation, follow instructions provided in its own Readme file.

## Executing Dockerised Automation

Start docker compose

> docker-compose up -d

Remove docker compose

> docker-compose rm

Delete docker-compose images

> docker-compose rmi scriptarium-<image-name>:latest
