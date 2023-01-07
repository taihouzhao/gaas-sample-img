#!/bin/bash
set -euxo pipefail

docker build -t gaas-sample-img .
docker run --gpu all --rm -v $(pwd)/img:/img -v /opt/local/HF:/HF gaas-sample-img