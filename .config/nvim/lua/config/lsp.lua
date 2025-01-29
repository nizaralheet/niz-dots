-- lua/config/lsp.lua
local NvimModule = {}

function NvimModule.setup()
    require("mason").setup()
    require("mason-lspconfig").setup({
        -- Automatically install LSP servers for these languages
        ensure_installed = {
            "pyright",      -- Python
            "rust_analyzer", -- Rust
            "lua_ls",       -- Lua
            "jsonls",       -- JSON
        },
        automatic_installation = true,
    })

    local lspconfig = require("lspconfig")
    -- Setup each LSP server
    local on_attach = function(client, bufnr)
        -- Add your on_attach logic here, like keymappings
        local opts = { noremap=true, silent=true }
        vim.api.nvim_buf_set_keymap(bufnr, 'n', 'gD', '<cmd>lua vim.lsp.buf.declaration()<CR>', opts)
        vim.api.nvim_buf_set_keymap(bufnr, 'n', 'gd', '<cmd>lua vim.lsp.buf.definition()<CR>', opts)
        vim.api.nvim_buf_set_keymap(bufnr, 'n', 'K', '<cmd>lua vim.lsp.buf.hover()<CR>', opts)
    end

    -- Default configuration for all servers
    local capabilities = require('cmp_nvim_lsp').default_capabilities()

    -- Specific server configurations
    local servers = {
        "pyright", "rust_analyzer", "lua_ls",  "jsonls"
    }

    for _, server in ipairs(servers) do
        lspconfig[server].setup {
            on_attach = on_attach,
            capabilities = capabilities,
            -- Add any specific server configurations here
            settings = {
                Lua = {
                    diagnostics = {
                        globals = { 'vim' } -- Recognize vim global
                    }
                }
            }
        }
    end
end

return NvimModule
