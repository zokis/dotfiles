#!/bin/bash
function exiting(){
    echo "Finalizing program..."
    echo $1
    exit
}

[ "$USER" != root ] && exiting "You are not root!"

add-apt-repository ppa:webupd8team/sublime-text-2; apt-get update;

apt-get install -y git
echo '==='
apt-get install -y python-dev
echo '==='
apt-get install -y python-pip
echo '==='
apt-get install -y terminator
echo '==='
apt-get install -y sublime-text
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
echo '==='
apt-get install -y conky
echo '==='
if which pip > /dev/null; then
    pip install ipython
    echo '==='
    pip install pep8
    echo '==='
    pip install virtualenvwrapper
fi
