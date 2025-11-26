local NvimModule = {}

function NvimModule.setup()
    require('telescope').setup {
        defaults = {
            file_ignore_patterns = {
                -- Hide all hidden files EXCEPT .config and .bash*
                "^%.[^cb]",           -- Hidden files NOT starting with 'c' or 'b'
                "^%.c[^o]",           -- Hidden files starting with 'c' but not 'co'
                "^%.co[^n]",          -- Hidden files starting with 'co' but not 'con'
                "^%.con[^f]",         -- Hidden files starting with 'con' but not 'conf'
                "^%.conf[^i]",        -- Hidden files starting with 'conf' but not 'confi'
                "^%.confi[^g]",       -- Hidden files starting with 'confi' but not 'config'
                "^%.b[^a]",           -- Hidden files starting with 'b' but not 'ba'
                "^%.ba[^s]",          -- Hidden files starting with 'ba' but not 'bas'
                "^%.bas[^h]",         -- Hidden files starting with 'bas' but not 'bash'
                -- Hide all image files
                "%.png$",
                "^%.git/",
                "%.jpg$",
                "%.jpeg$",
                "%.gif$",
                "%.bmp$",
                "%.svg$",
                "%.webp$",
                "%.ico$",
                "doc%..*%.org/",
                "go/"
            },
        },
        pickers = {
            find_files = {
                hidden = true,
                no_ignore = true,
                find_command = { "fd", "--type", "f", "--hidden", "--no-ignore" }
            }
        },
        extensions = {
            fzf = {
                fuzzy = true,
                override_generic_sorter = true,
                override_file_sorter = true,
                case_mode = "smart_case",
            }
        }
    }
    
    require('telescope').load_extension('fzf')
end

return NvimModule
