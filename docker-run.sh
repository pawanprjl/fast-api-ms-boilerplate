#!/bin/bash -e

echo "starting docker build"
docker build -f Dockerfile -t fast-api-server:latest .

echo "starting container build"
docker container rm -f fast-api || true
docker image prune -f
docker run -d --network=test-network --name fast-api fast-api-server

echo "container build finished"