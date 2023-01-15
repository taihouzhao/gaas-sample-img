#!/bin/bash
set -euxo pipefail

docker build -t gaas-sample-img .
docker run --gpus all --rm -v $(pwd)/img:/img -v /opt/local/HF:/HF gaas-sample-img
tar -C img/ffhq_crop/ -czvf ffhq.tar.gz .
tar -czvf man.tar.gz img/man/
tar -czvf woman.tar.gz img/woman/
