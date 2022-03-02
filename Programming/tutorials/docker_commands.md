# basic docker run command for detectron2 : creating container
```bash
docker run --gpus all -it \
  --shm-size=12gb --env=unix$DISPLAY --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --name=Giwon detectron2:v0
```

# basic docker run command for detectron2 : creating container _second try
```bash
docker run --gpus all -it \
    --privileged \
    -v /dev/video0:/dev/video0 \
    -v /dev/snd:/dev/snd \
    --memory=200g \
    --shm-size=200gb \
    --net=host \
    --env=unix$DISPLAY \
    -e="QT_X11_NO_MITSHM=1" \
    -v="/tmp/.X11-unix:/tmp/.X11-unix" \
    --name=Giwon_scratch1 \
    ubuntu:latest
```

# First thing to do after opening a Container
```sql
  pip install -e .
```

# rename containers
docker rename [old] [new]


# container to image
```sql
docker commit container_name image_name:version
```