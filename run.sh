#!/bin/bash

git pull
docker run -p 127.0.0.1:8888:8888 -v $(pwd)/notebooks:/notebooks -v $(pwd)/data:/data codecentric.ai-docker