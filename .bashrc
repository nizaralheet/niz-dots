#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
alias lf='ranger'
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias vim='lvim'
alias lvim=' /home/nizar/.local/bin/lvim'


# most important part of the rice 
function pywal() {
  killall dunst ; 
  wal -i "wallpapers/wallpaper$1.jpg" &&
  qtile cmd-obj -o cmd -f reload_config &&
  wpg -s ~/wallpapers/wallpaper$1.jpg ; dunst & # you could add" pywalfox update " if use firefox

}



PS1=$'\n\[\e[37m\]\u256D\u2500\u2500\[\e[35m\] \u222B ( \u ) \[\e[37m\]\u2500\[\e[48m\] [ \W ]\[\e[37m\]\n\u2570\u2500\u2500\u2500\u25b6\[\e[37m\] '
#PS1='[ \u @ \h \W]\$ '



(cat ~/.cache/wal/sequences &)

# Alternative (blocks terminal for 0-3ms)
cat ~/.cache/wal/sequences

# To add support for TTYs this line can be optionally added.
source ~/.cache/wal/colors-tty.sh
export QT_QPA_PLATFORMTHEME=qt5ct



[ -f ~/.fzf.bash ] && source ~/.fzf.bash
