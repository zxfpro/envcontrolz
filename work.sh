project_name=memorier

cp ../tools/mkdocs.yml .
mkdir $project_name && touch $project_name/core.py
mkdir test && touch test/test_.py
uv init .
uv sync
rm main.py   
mkdocs new .
bash update_docs.sh 
mkdocs gh-deploy -d ../.temp
bash run_build.sh 
uv publish
