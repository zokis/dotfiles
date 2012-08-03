#!/bin/bash

cd "$(dirname "$0")"

function install() {
    rsync \
        --exclude ".git/" \
        --exclude ".gitignore" \
        --exclude "install.sh" \
        --exclude "README.md" \
        --exclude "prepare_environment.sh" \
        --exclude "*.swp" \
        --exclude ".terminal.png" \
        --exclude "*~" \
        -av . ~
}

read -p "Running this file, you'll override some config files. Do you want to continue? (y/n) "

if [[ $1 =~ ^(-f|--force)$ ]]; then
    install
else
    if [[ $REPLY =~ ^[yY]$ ]]; then
        install 
    fi
fi