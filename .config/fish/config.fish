##function fish_prompt -d "Write out the prompt"
##    # This shows up as USER@HOST /home/user/ >, with the directory colored
##    # $USER and $hostname are set by fish, so you can just use them
##    # instead of using `whoami` and `hostname`
##    printf '%s@%s %s%s%s > ' $USER $hostname \
##        (set_color $fish_color_cwd) (prompt_pwd) (set_color normal)
##end

if status is-interactive
    printf '\e[5 q'
    # Commands to run in interactive sessions can go here
    set fish_greeting
        cowsay $(fortune -s)
    if test "$TERM" = "xterm-ghostty"

    end
end
function top_view
    mpv --ytdl-format='bestvideo[height<=720]+bestaudio/best' \
    --cache=yes \
    --cache-secs=60 \
    --demuxer-readahead-secs=60 \
    $argv[1]
end


function brightness
    set val $argv[1]
    if test $val -lt 10
        set val 10
    end
    sudo light -S $val
end

function runjava
    set java_file $argv[1]
    javac java_file
    java (string replace -r '\.java$' '' $file)
end

function load_env --description 'Load environment variables from .env file'
    if test -f .env
        for line in (cat .env | grep -v '^#' | grep -v '^$')
            set -gx (echo $line | cut -d= -f1) (echo $line | cut -d= -f2-)
        end
    end
end

set -x XCURSOR_THEME 'Bibata-Modern-Classic'
set -x XCURSOR_SIZE 24
set -x MANGOHUD_CONFIG 'fps, cpu_stats, gpu_stats, cpu_temp, gpu_temp, ram, swap'
#set -x GTK_THEME 'Orchis-Dark'
set -x MOZ_ENABLE_WAYLAND 1
alias pamcan=pacman
export LC_ALL=en_US.UTF-8
fish_add_path $HOME/.local/bin
alias :q='exit'
alias en-bluetooth='sudo systemctl enable bluetooth.service'
alias en-cups='sudo systemctl enable cups.socket'
alias dl='yay -Rns'
alias fortuneo= 'fortune -n 3'
alias cls='clear'
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias qtile-restart='qtile cmd-obj -o root -f restart'
alias lvim='/home/$USER/.local/bin/lvim'
function sudovim
    sudo env "PATH=$PATH" lvim
end



set -g VIRTUAL_ENV_DISABLE_PROMPT 1 # for venv promt
function fish_prompt
    set -l COLORFGBG  "15;0"
    set last_status $status

    # Username and Hostname
    set_color cyan
    echo -n ""
    set_color --background=cyan black
    echo -n " "(whoami)"@"(hostname | cut -d '.' -f1)" "
    set_color cyan --background normal
    echo -n ""
    
    # Current directory
    set_color yellow
    echo -n " •• "
    set_color --background=yellow black
    echo -n "  "(prompt_pwd)" "
    
    # Git branch (if inside a repo)
    set branch (git branch --show-current 2>/dev/null)
    if test -n "$branch"
        set_color yellow --background green
        echo -n ""
        set_color --background=green black
        echo -n "  $branch "
        set_color green --background normal
        echo -n ""
    else
        set_color yellow --background normal
        echo -n ""
    end
    
    if set -q VIRTUAL_ENV
        set venv (basename "$VIRTUAL_ENV")
        set_color blue
        echo -n " •• "
        set_color --background=blue black
        echo -n " $venv "
        set_color blue --background normal
        echo -n ""
    end
    # Exit status (if last command failed)
    if test $last_status -ne 0
        set_color red
        echo -n " •• "
        set_color --background=red black
        echo -n "⚠ $last_status "
        set_color red --background normal
        echo -n ""
    end
    
    # Time display on the right (if command took time)
    set -l cmd_time "$CMD_DURATION"
    if test -n "$cmd_time" -a "$cmd_time" -gt 0
        # Calculate actual length
        set -l used_length (math (string length (whoami)) + 1 + (string length (hostname | cut -d '.' -f1)) + (string length (prompt_pwd)) + 15)
        
        # Add branch length if exists
        if test -n "$branch"
            set used_length (math $used_length + (string length $branch) + 9)
        else 
            set used_length (math $used_length +4 )
        end

        if set -q VIRTUAL_ENV
            set venv (basename "$VIRTUAL_ENV")
            set used_length (math $used_length + (string length $venv) + 9)
        end

        # Add error code length if exists
        if test $last_status -ne 0
            set used_length (math $used_length + (string length $last_status) + 9)
        end
        
        # Add time display length
        set -l time_text "🔄 "(math $cmd_time / 1000)"s"
        set used_length (math $used_length + (string length $time_text) + 0)
        
        # Calculate spaces needed
        set -l terminal_width (tput cols)
        set -l spaces_needed (math $terminal_width - $used_length)
        
        if test $spaces_needed -gt 0
            printf "%*s" $spaces_needed ""
        end
        
        set_color magenta
        echo -n ""
        set_color --background=magenta black
        echo -n "󱑂  "(math $cmd_time / 1000)"s "
        set_color magenta --background normal
        echo -n ""
    end
    
    # Newline for spacing
    set_color normal
    echo -e "\n ❯ "
end
