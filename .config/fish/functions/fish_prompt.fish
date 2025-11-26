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
