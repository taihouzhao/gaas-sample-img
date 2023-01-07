#!/bin/bash
set -euxo pipefail

docker build -t gaas-sample-img .
docker run --gpus all --rm -v $(pwd)/img:/img -v /opt/local/HF:/HF gaas-sample-img
tar -zcvf img.tar.gz img/
