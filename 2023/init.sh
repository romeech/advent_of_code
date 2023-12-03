mkdir $1
pushd $1

touch README.md

mkdir py
pushd py
touch main.py
touch __init__.py
popd

mkdir rs
pushd rs
touch main.rs
popd

mkdir data
pushd data
touch input.txt
touch control.txt
popd
