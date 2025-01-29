local NvimModule = {}

function NvimModule.setup()
    local nvim_tree = require("nvim-tree")
    
    -- Configure NvimTree
    nvim_tree.setup {
        view = {
            width = 30,
            side = "right",
        },
        renderer = {
            group_empty = true,
        },
        filters = {
            dotfiles = false,
        },
    }

    -- Key mapping for NvimTree toggle
    vim.api.nvim_set_keymap('n', '<leader>e', ':NvimTreeFindFileToggle<CR>', { noremap = true, silent = true })
end

return NvimModule
