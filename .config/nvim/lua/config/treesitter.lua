local NvimModule = {}

function NvimModule.setup()
    require'nvim-treesitter.configs'.setup {
      -- A list of parser names, or "all" (the listed parsers MUST always be installed)
      ensure_installed = { "c", "lua", "vim","python","bash" },

      -- Install parsers synchronously (only applied to `ensure_installed`)
      sync_install = false,

      -- Automatically install missing parsers when entering buffer
      -- Recommendation: set to false if you don't have `tree-sitter` CLI installed locally
      auto_install = true,

      -- List of parsers to ignore installing (or "all")
      ignore_install = { "javascript" },

      highlight = {
        enable = true,

        -- list of language that will be disabled
        -- Note: I've modified this part to avoid having two `disable` configurations
        disable = function(lang, buf)
            local max_filesize = 100 * 1024 -- 100 KB
            local ok, stats = pcall(vim.loop.fs_stat, vim.api.nvim_buf_get_name(buf))
            if ok and stats and stats.size > max_filesize then
                return true
            end
            -- Optionally disable for specific languages
            -- return lang == "c" or lang == "rust"
        end,

        additional_vim_regex_highlighting = false,
      },
    }
end

return NvimModule
