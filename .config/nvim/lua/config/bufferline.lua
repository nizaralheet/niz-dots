local NvimModule = {}

function NvimModule.setup()
    require("bufferline").setup{
        options = {
            offsets = {
                    {
                        filetype = "NvimTree", -- Filetype for the sidebar
                        text = "File Explorer", -- Title shown in the bufferline
                        text_align = "center", -- Text alignment
                        separator = true,      -- Add a separator to distinguish
                        padding = 0,           -- Adds extra space
                    },
                },
            mode = "buffers",
            separator_style = "thick",
            diagnostics = "nvim_lsp",
            always_show_bufferline = false,
        },
    }

    -- Key mappings for buffer navigation

    vim.api.nvim_set_keymap('n', '<A-h>', ':BufferLineCyclePrev<CR>', { noremap = true, silent = true })
    vim.api.nvim_set_keymap('n', '<A-l>', ':BufferLineCycleNext<CR>', { noremap = true, silent = true })end
    vim.api.nvim_set_keymap('n', '<A-w>', ':BufferLinePickClose<CR>', { noremap = true, silent = true })

return NvimModule
