return {
    {
    "NvChad/nvim-colorizer.lua",
    event = "BufReadPre",
    opts = { -- set to setup table
        },
    },
    { 'nvim-telescope/telescope-fzf-native.nvim', build = 'make' },
    'rktjmp/lush.nvim',
    {
      "utilyre/barbecue.nvim",
      name = "barbecue",
      version = "*",
      dependencies = {
        "SmiteshP/nvim-navic",
        "nvim-tree/nvim-web-devicons", -- optional dependency
      },
    },
    'fgheng/winbar.nvim',
    "nvim-treesitter/nvim-treesitter",
    {"lukas-reineke/indent-blankline.nvim",
    main = "ibl",
    ---@module "ibl"
    ---@type ibl.config
    opts = {},
    },
    'williamboman/mason.nvim',
    'williamboman/mason-lspconfig.nvim',
    'neovim/nvim-lspconfig',
    'neovim/nvim-lspconfig',
    'AlphaTechnolog/pywal.nvim',
    'deviantfero/wpgtk.vim',
    { 'nvim-telescope/telescope.nvim', tag = '0.1.8' },
    'nvim-lualine/lualine.nvim',
    {
    "hrsh7th/nvim-cmp",
    event = "InsertEnter",
    dependencies = {
      "hrsh7th/cmp-nvim-lsp",
      "hrsh7th/cmp-buffer",
      "hrsh7th/cmp-path",
      "hrsh7th/cmp-cmdline",
      "L3MON4D3/LuaSnip",
      "saadparwaiz1/cmp_luasnip",
      "rafamadriz/friendly-snippets",
        }
    },
    {
        "goolord/alpha-nvim",
        config = function()
            require'alpha'.setup(require'alpha.themes.dashboard'.config)
        end,
        dependencies = { 'nvim-tree/nvim-web-devicons' }
    },
    {
        'nvim-tree/nvim-tree.lua',
        dependencies = {
            'nvim-tree/nvim-web-devicons', -- optional, for file icons
        },
        config = function()
            require("nvim-tree").setup()
        end
    },
    -- Buffer Line
    {
        'akinsho/bufferline.nvim',
        version = "*",
        dependencies = 'nvim-tree/nvim-web-devicons'
    },
    {
        'SmiteshP/nvim-navic',
        dependencies = "neovim/nvim-lspconfig",
        lazy = true ,
    },

}
