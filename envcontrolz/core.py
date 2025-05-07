
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




**GitHub Desktop 多账户管理**
1. 添加两个账户：
   - 文件 > 选项 > 账户
   - 分别登录个人和公司账户
2. 克隆时选择身份：
   - 点击 "Clone Repository" 时选择对应账户
3. 提交时自动使用仓库关联账户


如何防止.idea 这类文件上传到github中呢?
 : 我采用DeskTop 方案, 并使用PyCharm进行编程, 如何防止.idea 这类文件上传到github中呢?

 : 在使用 GitHub Desktop 以及 PyCharm 时，可以通过创建或修改 `.gitignore` 文件来防止某些文件或目录被提交到 GitHub。对于 PyCharm 项目，通常需要忽略 `.idea` 目录以及其他不必要的文件。

步骤：

1. **创建或修改 `.gitignore` 文件：**

   在你的项目根目录下，确保有一个名为 `.gitignore` 的文件。如果没有，你需要创建一个。

2. **配置 `.gitignore` 文件：**

   打开 `.gitignore` 文件，添加如下行来忽略 PyCharm 相关的配置文件：

   ```plaintext
   # Ignore PyCharm project files
   .idea/
   ```

如何把误上传的github中的.idea文件夹删除呢?
 : 如何把误上传的github中的.idea文件夹删除呢?
:  要从 GitHub 仓库中删除误上传的 `.idea` 文件夹，你可以按照以下步骤操作：

步骤一：在本地仓库中删除 `.idea` 文件夹

1. **打开终端或命令行**，导航到你的本地 Git 仓库的根目录。

2. **从 Git 索引中移除 `.idea` 文件夹**，但保留本地文件。这会从版本控制中删除该文件夹，但不会删除本地的实际文件：

   ```bash
   git rm -r --cached .idea/
   ```

3. **确认移除操作**：确保 `.idea` 文件夹不再处于索引中。

步骤二：更新 `.gitignore` 文件

1. 编辑 `.gitignore` 文件，确保它包含 `.idea/` 行以忽略此文件夹：

   ```plaintext
   # Ignore PyCharm project files
   .idea/
   ```

2. **添加 `.gitignore`** 文件到 Git 索引：

   ```bash
   git add .gitignore
   ```

步骤三：提交更改并推送到 GitHub

1. **提交更改**：

   ```bash
   git commit -m "Remove .idea directory from version control and update .gitignore"
   ```

2. **推送更改**到 GitHub：

   ```bash
   git push origin main
   ```

   注意：如果你的默认分支不是 `main`，请将其替换为对应的分支名称（如 `master`）。

完成上述步骤后，`.idea` 文件夹将从你的 GitHub 仓库中删除，并且 `.gitignore` 文件将确保 `.idea` 文件夹不会在未来的提交中被包含。








