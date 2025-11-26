return {
    {'akinsho/toggleterm.nvim', version = "*",
        opts={
            --open_mapping = [[<Leader>t]],
            direction = "float",
            insert_mappings = true,  -- Important: allows toggle from insert mode
            terminal_mappings = true,autochdir = true
        }
    },
    {
        'windwp/nvim-autopairs',
        event = "InsertEnter",
        config = function()
            require('nvim-autopairs').setup({
                -- You can add custom configurations here if needed
                check_ts = true,  -- For integration with treesitter (if you use it)
            })
        end
    },

    {
        "folke/snacks.nvim",
        priority = 1000,
        lazy = false,
        ---@type snacks.Config
        opts = {
           -- your configuration comes here
           -- or leave it empty to use the default settings
           -- refer to the configuration section below
           bigfile = { enabled = true },
           dashboard = { enabled = false },
           explorer = { enabled = false },
           indent = { enabled = true },
           input = { enabled = true },
           picker = { enabled = true},
           notifier = { enabled = false },
           quickfile = { enabled = true },
           scope = { enabled = true },
           scroll = { enabled = true },
           statuscolumn = { enabled = true },
           words = { enabled = true },
	    },
    },
    {
        "nvim-tree/nvim-web-devicons", -- not strictly required, but recommended
    },
    {
        "nvim-lua/plenary.nvim",
    },
    {
        "MunifTanjim/nui.nvim",
    },
    {

        "folke/tokyonight.nvim",
        lazy = false,
        priority = 1000,
        opts = {},
    },

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
    {
        "lukas-reineke/indent-blankline.nvim",
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
    { 'nvim-telescope/telescope.nvim',            tag = '0.1.8' },
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
            require 'alpha'.setup(require 'alpha.themes.dashboard'.config)
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
        lazy = true,
    },

}
