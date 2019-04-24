#!/bin/bash

git pull
docker run -p 127.0.0.1:8888:8888 -p 127.0.0.1:8889:8889 -v "$(pwd)/notebooks":/notebooks -v "$(pwd)/data":/data codecentric/codecentric.ai-docker
