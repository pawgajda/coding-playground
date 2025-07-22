### Redis

Dynamic Programming Playground with Redis.

##### Running on MacOS

1. Start Docker VM

```
limactl start template://docker
export DOCKER_HOST=$(limactl list docker --format 'unix://{{.Dir}}/sock/docker.sock')
```

2. Start Redis

```
docker.lima run -d -p 6379:6379 redis
```

3. Verify

```
% docker.lima ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                         NAMES
8ce0656bb6b3   redis     "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp   brave_easley
```

4. Setup Virtualenv

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install redis_decorators fakeredis
```
