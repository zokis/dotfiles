#!/bin/bash
function exiting(){
    echo "Finalizing program..."
    echo $1
    exit
}

[ "$USER" != root ] && exiting "You are not root!"

apt-get install -y git
echo '==='
apt-get install -y python-pip
echo '==='
apt-get install -y terminator
echo '==='
apt-get install -y sublime-text-2
echo '==='
apt-get install -y virtualbox
echo '==='
apt-get install -y python-pygments
echo '==='
apt-get install -y bpython
echo '==='
apt-get install -y gitg
echo '==='
apt-get install -y nodejs

if which pip > /dev/null; then
    pip install virtualenvwrapper
    pip install ipython
fi