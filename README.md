# 初始化一个仓库的步骤

使用该方式 仓库 来固定知识


0 起名 查看pypi 是否重名
1 在能力面板创建其内容
2 创建仓库
3 克隆

0 uv init .
1 uv sync


1 mkdocs new .
2 p_pulldocs 
3 构建包 init
4 更新readme  pyproject
5 更新mkdocs.yml  
6 mkdocs gh-deploy -d ../.temp
7 p_pushdocs 
8 p_build

测试的时候
1 在jupyter 上使用 use case
2 写入use case
3 编写细节的 pytesr
测试完再上的应该