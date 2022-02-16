# create a docker container
```bash
docker run --ipc=host --gpus all -it \
    --privileged \
    -v /dev/video0:/dev/video0 \
    -v /dev/snd:/dev/snd \
    --memory=10g \
    --shm-size=12gb \
    --net=host \
    --env=unix$DISPLAY \
    -e="QT_X11_NO_MITSHM=1" \
    -v="/tmp/.X11-unix:/tmp/.X11-unix" \
    --name=Giwon_y5_1 \
    ultralytics/yolov5:latest
```