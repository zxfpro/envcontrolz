



### 工具
```python
uv python dir
uv tool dir
```

### 安装python
```python
uv python list
uv python install 3.13
```

### 升级包
```python
uv lock --upgrade-package requests
```

### 设定环境变量
```bash
# 缓存目录
export UV_CACHE_DIR=/path/to/cache/dir

# 镜像地址
export UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple

# 额外镜像地址
export EXTRA_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple

# 不用缓存
export UV_NO_CACHE=0

# 下载包时的超时时间，单位为秒
UV_HTTP_TIMEOUT=60
```






class UVManager():
	def __init__(self) -> None:
		pass

	def add(package:str):
		# 安装开发和生产环境
		if 1:
			return "uv add {package}"
		elif:
			return "uv add --group dev pandas"
		else
			return "uv add --group production requests"
		
	def remove(package:str):
		return "uv remove {package}"

	def init(project):
		return "uv init ."
		return "uv init <project dir>"

	def build():
		return "uv build"

	def sync():
		return "uv sync"

	def run():
		return "uv run ./hallo.py"

	def requiretmn():
		### 导出环境
		# uv export --format requirements-txt > requirements.txt


class docker_compose():
	"""
	文件布局
```
project
- docker-compose.yml
- Dockerfile.kimi
- Dockerfile.obsidianrag
```

ports 映射
主机:容器

restart
- `no`：不自动重启容器，默认值。
- `always`：总是自动重启容器。
- `on-failure`：仅在容器非正常退出时自动重启。
- `unless-stopped`：除非手动停止容器，否则总是自动重启。

	"""
	def __init__(self) -> None:
		pass

	def build():
		# 使用 `--force-rm` 和 `--no-cache` 选项
		# docker-compose build --force-rm --no-cache mcpserver
		# docker-compose build <service_name>

	def up():
		# docker-compose up mcpserver
		# docker-compose up --build
		# docker-compose up -d --no-deps --build <service_name>

	def docker_run():
		# 如果构建完成后，你希望立即启动该服务，可以使用以下命令
		#  docker run -i -t ubuntu:15.10 /bin/bash

	def write():
		"""
		

docker compose


```docker-compose.yml
version: '3.8'

services:
  obsidianrag:
	restart: always
    build:
      context: .
      dockerfile: Dockerfile.obsidianrag
    ports:
      - "9000:9000"
    volumes:
      - .:/app
      - /Users/zhaoxuefeng/本地文稿/百度空间/cloud/Obsidian/知识体系尝试:/Users/zhaoxuefeng/本地文稿/百度空间/cloud/Obsidian/知识体系尝试
      - /Users/zhaoxuefeng/GitHub/test1:/Users/zhaoxuefeng/GitHub/test1
  kimi:
    build:
      context: .
      dockerfile: Dockerfile.kimi
    ports:
      - "9001:9000" # 主机:容器
    volumes:
      - .:/app
      - /Users/zhaoxuefeng/本地文稿/百度空间/cloud/Obsidian/知识体系尝试:/Users/zhaoxuefeng/本地文稿/百度空间/cloud/Obsidian/知识体系尝试
      - /Users/zhaoxuefeng/GitHub/test1:/Users/zhaoxuefeng/GitHub/test1

```
		"""

class pi():
	### 上传到pip私有源
	def __init__(self):
		pass
	
	def update(self):
		# cp dist/dataserver-0.0.1-py3-none-any.whl /Users/zhaoxuefeng/Documents/DataCentre/pypi  # 拷贝你的whl包 到pypi私有源位置
		# dir2pi /Users/zhaoxuefeng/Documents/DataCentre/pypi # 更新pip私有源
		# pip2pi  /Users/zhaoxuefeng/Documents/DataCentre/pypi pandas # 使用pip私有源

	def pip(self):
		# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

import numpy as np
from IPython.display import display,Audio


class Ipython():
     def __init__(self) -> None:
		  pass
     
	def du():
		framerate = 44100 #评率
		t = np.linspace(0,5,framerate*5)
		dataleft = np.sin(2*np.pi*220*t)
		dataright = np.sin(2*np.pi*224*t)
		display(Audio([dataleft, dataright], rate=framerate))
	def play_speech(data):
		display(Audio(data,autoplay=True))


class Colab(Know):

    def 防止自动退出(self):
        return """
防止colab 自动退出
```python
#@title 1. Keep this tab alive to prevent Colab from disconnecting you { display-mode: "form" }
#@markdown Press play on the music player that will appear below:
%%html
<audio src="https://oobabooga.github.io/silence.m4a" controls> 用来防止发生断裂
```

"""




   # 适配器


   def 防止自动退出():
      #%%html
      #<audio src="https://oobabooga.github.io/silence.m4a" controls> 用来防止发生断裂
      pass

   # 挂载云盘
   def drive():
      from google.colab import drive
      drive.mount('/content/drive')



   # 环境变量
   def get_veriable():
      from google.colab import userdata
      api_key = userdata.get('api_key')



class IPManager():
     def __init__(self) -> None:
		  pass
     
	 def ip1():
          # 使用netstat命令 该命令会列出所有与端口9669相关的网络连接信息，包括协议、本地地址、外部地址、状态和进程ID。
          return """ `sudo netstat -tunlp | grep "9669"`"""
          
	def ip2():
          # 该命令会列出占用端口9669的进程信息。
          return """ `sudo lsof -i :9669` """

	def xx():
          chmod +x myscript.sh
          
	def write():
		"""
            
		"""
            sudo mv myscript.sh /usr/local/bin/myscript


		echo "print('Hello from Python!')" | python3


class Xmind:
	def work1():

		Xmind 导出为opml格式
		```
		- 直接将<head> ... </head>删除
		```


		mindly 导出为txt 将txt 复制粘贴到Xmind中



#### GitHub


class Githubs():
	def __init__(self) -> None:
		pass

	def multi_user_manage(self):
		# GitHub Desktop 多账户管理 文件 > 选项 > 账户





class ServerMechine():
	def __init__(self) -> None:
		pass

	def set_server(self):
		# - 关闭自动睡眠   - 设置-> 锁定屏幕 -> 不活跃时启动屏幕保护程序 -> 永不,永不 永不
		# - 开机自动登录   - 用户和群组 -> 自动以此身份登录
		# - 断点后自动开机 - 节能 -> 断电后自动开机
		# - 远程访问      - 设置-> 通用-> 共享 -> 远程管理

	def build_mechine(self):
		pass

	def get_info_mechine(self):
		"""
		uname -m #查看架构
		df -h # 查看磁盘
		lscpu # cpu信息
		nvidia-smi # gpu信息
		ping -4 www.baidu.com
		"""

	def create_user(self):
		"""
		创建用户组
		```
		adduser username
		passwd username
		usermod -aG sudo qework
		```
		"""

	def init_server(self):
		# 安装基础依赖包
		"""
		
		sudo apt update
		sudo apt install build-essential
		apt install python3
		apt install vim git curl htop -y

		"""

	def anz_conda(self):
		"""
		安装conda
		wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

		bash Miniconda3-latest-Linux-x86_64.sh

		"""


class XClashh():
	def 如何在局域网中设置代理():
		"""
## 可以让设备访问外网

## 方法
windows10 -> 设置 -> 代理 -> 启用“使用代理服务器” -> 输入代理服务器地址和端口号
mac -> 点击当前连接的Wi-Fi网络旁边的“i”按钮 -> 配置代理”->“手动” -> 输入代理服务器地址和端口号
Oculurs -> 网络 -> 高级设置 -> 代理 ->输入代理服务器地址和端口号


如何使用ClashX控制操作


## 性质
**全局模式**：所有流量都通过代理节点，适合需要全面保护的情况。
**规则模式**：根据配置文件中的规则，决定哪些流量走代理，哪些直连。
**直连模式**：所有流量不走代理，适合访问本地网络。
**脚本模式（Script Mode）**是一种高级功能，允许用户通过自定义脚本来动态处理网络请求的分流

**设置系统代理**：如果希望所有应用都通过ClashX代理，可以在ClashX的菜单栏图标中选择“设置为系统代理”。

可以使用局域网共享来分享VPN

## 方法
分享 VPN : **允许局域网连接**
记下显示的HTTP和SOCKS代理端口，通常默认HTTP端口为7890。

1. 打开设备的Wi-Fi设置，点击当前连接的Wi-Fi网络旁边的“i”按钮。
2. 滑动到底部，选择“配置代理”->“手动”。
3. 填写以下信息：
4. - **服务器**：输入ClashX运行的电脑的IP地址（如`192.168.x.x`）。
        
    - **端口**：输入ClashX的HTTP代理端口（通常是`7890`）。
        
    - **认证**：通常不开启。
        
设置[[如何在局域网中设置代理]]: 分享本机的外网网络给局域网的其他设备

将配置移到新的设备中: 配置 -> 打开配置文件夹 -> 将对应的配置文件夹移动到新位置


查看端口被占用情况


		"""









