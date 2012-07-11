dotfiles
========

### @zokis's dotfiles

This project is a collections of dotfiles forked from https://github.com/deniscostadsc/dotfiles . I used just on Ubuntu.

> Welcome message, PS1 and PS2.
>
> ![Welcome message, PS1 and PS2.](https://github.com/zokis/dotfiles/raw/master/.terminal.png "Welcome message, PS1 and PS2.")
>

to download the project:

```bash
git clone https://github.com/zokis/dotfiles.git
```

install system applications:
```bash
cd dotfiles
sudo ./prepare_environment.sh
```

install the dotfiles

```bash
./install.sh
source ~/.bashrc
```
## Aliases:
### Sublime text 2 Aliases
* alias subl='sublime-text-2'
* alias suble='sublime-text-2 &'

###Git Aliases
* alias ga='git add'
* alias gA='git add .'
* alias gau='git add -u'
* alias gb='git branch'
* alias gc='git checkout'
* alias gcl='git clone'
* alias gct='git commit'
* alias gcm='gct -m'
* alias gcma='gct -am'
* alias gcv='gct -v'
* alias gd='git diff'
* alias gl='git log'
* alias glgol='gl --graph --decorate --pretty=oneline --abbrev-commit'
* alias glgola='gl --graph --decorate --pretty=oneline --abbrev-commit --all'
* alias gps='git push'
* alias gpl='git pull'
* alias gra='git remote add'
* alias grm='git rm'
* alias grr='git remote rm'
* alias gst='git status'

### Python Django aliases
* alias drs='python manage.py runserver'
* alias dtest='python manage.py test'
* alias dshell='python manage.py shell'
* alias ddump='python manage.py dumpdata'
* alias dload='python manage.py loaddata'
#### If the South is installed
* alias dmigr='python manage.py migrate'