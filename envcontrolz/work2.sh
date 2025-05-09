#!/bin/bash
set -e # 如果任何命令失败，立即退出脚本

echo "============================================="
echo " 开始执行 Python 包仓库初始化脚本"
echo "============================================="

# Step 0: 起名 查看pypi 是否重名 (自动化检查 + 手动确认)
echo "步骤 0: 起名并检查 PyPI 是否重名"

# 假设 check_pypi_name.py 在脚本当前目录或 PATH 中
CHECK_SCRIPT="check_pypi_name.py" # 或者指定完整路径

while true; do
    read -p "请输入您希望在 PyPI 上注册的包名称 (例如: my-awesome-package): " PYPI_PACKAGE_NAME

    if python "$CHECK_SCRIPT" "$PYPI_PACKAGE_NAME"; then
        # python 脚本返回 0，表示可用
        echo "继续创建项目..."
        break # 包名可用，退出循环
    else
        # python 脚本返回非 0，表示不可用或检查失败
        echo "请尝试另一个包名。"
        # 这里不需要 sys.exit(1) 因为我们用 while 循环让用户重试
    fi
done

# 派生出 Python 模块名 (通常是将连字符替换为下划线)
MODULE_NAME=$(echo "$PYPI_PACKAGE_NAME" | sed 's/-/_/g')
echo "确认包名 '$PYPI_PACKAGE_NAME' 可用，派生的内部 Python 模块名称为: '$MODULE_NAME'"

read -p "请输入您希望创建的项目目录名称 (通常与包名类似或相同): " PROJECT_DIR_NAME

#################################
# Step 1: 在能力面板创建其内容 (外部步骤)
echo "步骤 1: 在您的能力面板/项目管理工具中创建相关内容 (外部操作)"
read -p "请在完成后按 Enter 继续..."

# Step 2: 创建仓库 (本地目录创建)
echo "步骤 2: 创建项目目录并进入"
mkdir -p "$PROJECT_DIR_NAME"
cd "$PROJECT_DIR_NAME"
echo "已创建目录 '$PROJECT_DIR_NAME' 并进入"

# Step 3: 克隆 (如果仓库是先远程创建的，此处应是 git clone)
# 假设你是在一个新目录中开始，所以这里是本地 git init
echo "步骤 3: 初始化本地 Git 仓库"
if [ -d .git ]; then
  echo "Git 仓库已存在，跳过 git init"
else
  git init
  echo "本地 Git 仓库初始化完成"
  # 如果需要关联远程仓库，请在此手动添加
  # git remote add origin <your_remote_repo_url>
  # echo "请手动添加远程仓库，例如: git remote add origin <your_remote_repo_url>"
fi


# --- 包和文档初始化 ---
echo "--- 包和文档初始化 ---"

# 步骤 0 uv: uv init .
echo "步骤 0 uv: 初始化 uv 环境 (创建 pyproject.toml)"
if [ -f pyproject.toml ]; then
  echo "pyproject.toml 已存在，跳过 uv init"
else
  uv init . --name "$PYPI_PACKAGE_NAME" # uv init 可以指定包名
  echo "uv init . 完成"
fi

# 步骤 1 uv: uv sync
echo "步骤 1 uv: 同步初始依赖 (安装 build backend 等)"
uv sync
echo "uv sync 完成"

# 步骤 1 mkdocs: mkdocs new .
echo "步骤 1 mkdocs: 初始化 MkDocs 文档结构"
if [ -f mkdocs.yml ]; then
   echo "mkdocs.yml 已存在，跳过 mkdocs new"
else
   mkdocs new .
   echo "mkdocs new . 完成"
fi

# 步骤 3: 构建包 init (创建 src/module_name 目录结构) - 对应您列表中的第3步
echo "步骤 3: 创建包的源代码目录结构"
mkdir -p "src/$MODULE_NAME"
touch "src/$MODULE_NAME/__init__.py"
touch "src/$MODULE_NAME/__main__.py" # 如果你的包支持 python -m 包名 运行，需要这个文件
echo "已创建 src/$MODULE_NAME/__init__.py 和 src/$MODULE_NAME/__main__.py"


# --- 手动编辑配置阶段 ---
echo "--- 手动编辑配置阶段 ---"

# 步骤 4: 更新 README pyproject (手动步骤)
echo "步骤 4: 手动更新 README.md 和 pyproject.toml"
echo "  - 编辑 pyproject.toml: 填充项目描述、作者、license、依赖等信息。"
echo "    请确保 [project] -> name 是 '$PYPI_PACKAGE_NAME'。"
echo "    请确保 [tool.setuptools] -> package-dir = {\"\" = \"src\"} 且 [tool.setuptools.packages] -> find = {where = [\"src\"]} 指向 'src' 目录。"
echo "  - 编辑 README.md: 写入项目介绍、安装和使用方法等。"
read -p "请在完成后按 Enter 继续..."

# 步骤 5: 更新 mkdocs.yml (手动步骤)
echo "步骤 5: 手动更新 mkdocs.yml"
echo "  - 编辑 mkdocs.yml: 配置 site_name, nav (导航), theme, plugins 等。"
read -p "请在完成后按 Enter 继续..."


# --- 构建和发布文档 ---
echo "--- 构建和发布文档 ---"

# 步骤 2 p_pulldocs (执行自定义脚本) - 对应您列表中的第2步
echo "步骤 2 p_pulldocs: 执行自定义文档拉取脚本"
# 如果 p_pulldocs 需要参数，请根据实际情况修改下方命令
p_pulldocs
echo "p_pulldocs 执行完成"


# 步骤 6: mkdocs gh-deploy -d ../.temp (构建文档到临时目录)
echo "步骤 6: 使用 mkdocs gh-deploy 构建文档到临时目录 ../.temp"
mkdocs gh-deploy -d ../.temp # 注意：这里是构建，不自动推送到 gh-pages
echo "mkdocs gh-deploy -d ../.temp 完成"


# 步骤 7: p_pushdocs (执行自定义脚本推送文档)
echo "步骤 7: p_pushdocs: 执行自定义文档推送脚本"
# 如果 p_pushdocs 需要参数，请根据实际情况修改下方命令
# 注意：p_pushdocs 应该负责将 ../.temp 目录的内容推送到您的 GitHub Pages 分支
p_pushdocs
echo "p_pushdocs 执行完成"


# --- 构建和发布包 ---
echo "--- 构建和发布包 ---"

# 步骤 8: p_build (构建分发包)
echo "步骤 8: 构建 Python 包分发文件 (.whl, .tar.gz)"
uv build # 等同于 python -m build
echo "uv build 完成，分发文件在 ./dist/ 目录下"


# 步骤 9: uv publish (发布到 PyPI)
echo "步骤 9: 发布包到 PyPI"
echo "请确保您已配置 PyPI 认证信息 (例如通过环境变量或 ~/.pypirc)"
echo "# uv publish # 此行默认注释，请在确认无误后手动执行以发布"
# uv publish # 发布到 PyPI，请在测试后手动执行！


# --- 测试阶段 (手动步骤) ---
echo "--- 测试阶段 (手动操作) ---"
echo "以下是测试建议步骤，需要您手动完成："
echo "步骤 1: 在 Jupyter 环境中使用 use case (导入您的包并运行示例代码)"
echo "步骤 2: 写入 use case 代码 (在文档或示例目录中编写使用示例)"
echo "步骤 3: 编写细节的 pytest 测试 (在 tests/ 目录下编写测试文件)"

echo "--- 测试完成后 ---"
echo "请在测试全部通过后，提交您的代码，打上 Git Tag (建议遵循 Semantic Versioning)，然后手动运行 'uv publish' 发布该版本。"


echo "============================================="
echo " Python 包仓库初始化脚本执行完毕"
echo "请根据提示完成手动配置和后续步骤"
echo "============================================="