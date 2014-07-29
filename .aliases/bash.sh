# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

alias mkcd='mkdir -p $1 && cd $1'

# some more ls aliases
alias ll='ls -AhlF'
alias la='ls -A'
alias l='ls -CF'

# alias sublime text 2
alias subl='sublime-text-2'
alias suble='sublime-text-2 &'

# alias reload self 
alias rself='source ~/.bashrc'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'


# terminalTimer alias
alias timer='python ~/.timer/termtimer.py'