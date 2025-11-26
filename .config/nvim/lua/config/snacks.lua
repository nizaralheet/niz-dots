local NvimModule = {}

function NvimModule.setup()
    local snacks = require("snacks")

    snacks.setup {
        ---@type snacks.config
        lazy = false,
        priority = 1000,

        opts = {
            -- your configuration comes here
            -- or leave it empty to use the default settings
            -- refer to the configuration section below
            bigfile = { enabled = true },
            dashboard = { enabled = true },
            explorer = {
                enabled = false,
                show_hidden = true,
            },
            indent = { enabled = true },
            input = { enabled = true },
            picker = { enabled = false },
            notifier = { enabled = false},
            quickfile = { enabled = true },
            scope = { enabled = true },
            scroll = { enabled = true },
            statuscolumn = { enabled = true },
            words = { enabled = true },
        },
    }
end

return NvimModule
