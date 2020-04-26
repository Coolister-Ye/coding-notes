### pycharm + docker 构建tensorflow深度学习环境

本notes根据网上资料结合实际生成环境进行配置实验

1. pre-requestition
- pycharm professional
- dcoker
- Nvidia-docker

2. 新建docker image
- Dockerfile
```
FROM tensorflow/tensorflow:devel-py3
LABEL maintainer="Coolister-Ye"

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
            vim \
            cron \
            openssh-server \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --default-timeout-100 -r requirements.txt
```

3. 创建docker container
- sudo nvidia-docker run (nvidia-docker-v1)
- sudo docker run --runtime=nvidia (nvidia-docker-v2)

example:
```shell
docker run \
    --runtime=nvidia \
    --rm \
    -ti \
    -v /remote dir:/container dir \
    -p 8822:22 \
    -p 8888:8888 \
    -name="dockerName" \
    dockerImageId bash

docker run --rm -ti -v $pwd:/app -p 8822:22 -p 8888:8888 --name="deploy_tensor" cb4d7ac68d16
```

noets：
- 这里要注意一下镜像cuda的版本
- 8888端口是tensorflow jupyter notebook
- 22端口是ssh服务
- 退出时不要ctrl+c/ctrl+z/exits退出，会导致container关闭，直接关闭窗口即可

4. 在镜像内进行ssh-server配置
```
mkdir /var/run/sshd
echo 'root:passwd-xxx' | chpasswd #修改ssh密码
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config #修改ssh配置

service ssh restart #重启服务
```
notes: 
- debug-01: 有可能在用pycharm连服务器的时，ssh session可以启动，但在“TEST SFTP CONNECTION”的时候会一直loading状态，这时候可以试一下是否以下sftp设置原因造成：

```
- sftp -P 8822 root@0.0.0.0
- 输入密码进行登陆
- 提示`sftp Ensure the remote shell produces no output for non-interactive sessions.`错误
- 修改/etc/ssh/sshd_config中的Subsystem配置为`Subsystem sftp internal-sftp`
- 重启服务 `service ssh restart`
```

- debug-02: 上传镜像的时候，可能会频繁更改port配置，有可能出现`ECDSA host key "ip-address" for has changed and you have requested strict checking`错误

```
ssh-keygen -R "你的远程服务器ip地址"
eg. ssh-keygen -R [0.0.0.0]:8822
```

5. 测试
```
sudo docker port [docker-id/name] 22 #输出0.0.0.0:8822 服务器-8822端口绑定到container-22端口
ssh root@[host-ip/0.0.0.0] -p 8022 #测试ssh能否登入container
```

6. 配置pycharm
- Pycharm Tools > Deployment > Configuration, 新建SFTP服务器
- 点击TEST测试能否链接成功
- File > Setting > Project > Project Interpreter, 新建SSH Interpreter (新版本在Preference里面)

##### extra notes
- 监控gpu使用情况：watch -n 5 nvida-smi
- 监控cpu/memery使用情况：top
- 如果images不是long running的，使用tail -f /dev/null来保持进程
- 需要绑定server端python，使用which python来查看路径
