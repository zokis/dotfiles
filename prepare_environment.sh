#!/bin/bash
function exiting(){
    echo "Finalizing program..."
    echo $1
    exit
}

[ "$USER" != root ] && exiting "You are not root!"

add-apt-repository ppa:chris-lea/node.js; apt-get update;
add-apt-repository ppa:webupd8team/sublime-text-3; apt-get update;
gsettings set com.canonical.desktop.interface scrollbar-mode normal;
gsettings set com.canonical.Unity.Lenses remote-content-search none;
apt-get remove -y unity-lens-shopping;
echo 127.0.0.1 productsearch.ubuntu.com | tee -a /etc/hosts;

apt-get install aplay;
echo '==='
apt-get install python-software-properties;
echo '==='
apt-get install -y git
echo '==='
apt-get install -y python-dev
echo '==='
apt-get install -y python-pip
echo '==='
apt-get install -y terminator
echo '==='
apt-get install -y sublime-text-installer
echo '==='
apt-get install -y python-pygments
echo '==='
apt-get install -y bpython
echo '==='
apt-get install -y nodejs
echo '==='
apt-get install -y npm

echo '==='
if which pip > /dev/null; then
    pip install ipython
    echo '==='
    pip install pep8
    echo '==='
    pip install virtualenvwrapper
    echo '==='
    pip install youtube-dl
fi
