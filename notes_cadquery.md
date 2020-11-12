

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

bash miniconda.sh -b -p $HOME/miniconda

conda update -n base -c defaults conda

conda create -n cadquery

conda activate cadquery

conda install -c conda-forge -c cadquery cadquery=master

conda install -c cadquery -c conda-forge cq-editor=master


https://cqparts.github.io/
https://cadquery.readthedocs.io/en/latest/selectors.html
