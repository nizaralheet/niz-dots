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

end

return NvimModule
