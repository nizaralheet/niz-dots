local NvimModule = {}

function NvimModule.setup()
    --  require("config.snacks").setup()
    require("config.telescope").setup()
    require('config.barbecue').setup()
    require('config.lsp').setup()
    require('config.lualine').setup()
    require('config.alpha').setup()
    require('config.nvim-tree').setup()  -- Add this
    require('config.bufferline').setup() -- Add this line
    require("config.completion").setup()
    require("ibl").setup()
    require("colorizer").setup()
    require("config.treesitter").setup()
end

return NvimModule
