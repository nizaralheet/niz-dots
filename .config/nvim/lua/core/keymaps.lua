local NvimModule = {}

function NvimModule.setup()
    local keymaps = {
        ['n'] = {
            -- Normal mode keymaps
            ['<C-Space>'] = { cmd = ":Telescope find_files<CR>", opts = { noremap = true, silent = true } },
        },
    }

    for mode, maps in pairs(keymaps) do
        for keymap, value in pairs(maps) do
            vim.api.nvim_set_keymap(mode, keymap, value.cmd, value.opts)
        end
    end
end

return NvimModule
