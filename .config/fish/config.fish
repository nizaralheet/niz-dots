if status is-interactive
    # Commands to run in interactive sessions can go here
end
set -x TERMINAL kitty
set -Ux EDITOR lvim

export LC_ALL=en_US.UTF-8
fish_add_path $HOME/.local/bin
alias :q='exit'
alias lf='ranger'
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias qtile-restart='qtile cmd-obj -o root -f restart'
function sudovim
    sudo env "PATH=$PATH" lvim
end

#set -x QT_QPA_PLATFORM qtile
#set -x QT_QPA_PLATFORMTHEME qt5ct
#set -x QT_AUTO_SCREEN_SCALE_FACTOR 1
#set -x QT_STYLE_OVERRIDE kvantum



function fish_prompt
    set_color red
    echo -n "╭── ∫ ( "
    set_color normal 
    echo -n (whoami)
    set_color red
    echo -n " ☪ ) ─ [ "
    set_color green
    echo -n (prompt_pwd)
    set_color red
    echo " ]"
    echo -n "╰───▶ "
    set_color normal
 end

set -g fish_greeting
