local NvimModule = {}

function NvimModule.setup()
    vim.g.mapleader = ' '
    local keymaps = {
        ['n'] = {
            -- Normal mode keymaps
            --['<C-t>'] = {cmd='<cmd>ToggleTerm direction=float<cr>',opts = { noremap = true, silent = true } },
            ['<C-Space>'] = { cmd = ":Telescope find_files<CR>", opts = { noremap = true, silent = true } },
            --            ['<Leader>e'] = { cmd = "<cmd>Neotree toggle<CR>", opts = { noremap = true, silent = true } },
            ["<leader>e"] = { cmd = ":NvimTreeFindFileToggle<CR>", opts = { noremap = true, silent = true }, desc = "File Explorer" },
            --this shit suck so hard ["<leader>e"] = { cmd = ":lua Snacks.explorer.open()<CR>:highlight SnacksPicker guibg=None<CR>", opts = { noremap = true, silent = true }, desc = "File Explorer" },
            ['<A-h>']= { cmd=':BufferLineCyclePrev<CR>',opts = { noremap = true, silent = true }},
            ['<A-l>']={ cmd=':BufferLineCycleNext<CR>', opts= { noremap = true, silent = true }},
            ['<A-w>']={ cmd=':BufferLinePickClose<CR>', opts= { noremap = true, silent = true }},
            ['<leader>t']={ cmd=':ToggleTerm <CR>', opts= { noremap = true, silent = true }},

        },
        ['t']={
            ['<Esc>']={ cmd='<cmd>ToggleTerm<CR>', opts= { noremap = true, silent = true }},
        }
    }

    for mode, maps in pairs(keymaps) do
        for keymap, value in pairs(maps) do
            vim.api.nvim_set_keymap(mode, keymap, value.cmd, value.opts)
        end
    end

end

return NvimModule
