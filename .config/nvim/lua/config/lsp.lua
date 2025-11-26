local NvimModule = {}

function NvimModule.setup()
    require("mason").setup()
    require("mason-lspconfig").setup({
        ensure_installed = {
            "rust_analyzer",        -- Rust
            "lua_ls",              -- Lua
            "pylsp",               -- Python LSP (stable, no npm needed)
        },
        automatic_installation = true,
    })

    local on_attach = function(client, bufnr)
        local opts = { noremap=true, silent=true }
        vim.api.nvim_buf_set_keymap(bufnr, 'n', 'gD', '<cmd>lua vim.lsp.buf.declaration()<CR>', opts)
        vim.api.nvim_buf_set_keymap(bufnr, 'n', 'gd', '<cmd>lua vim.lsp.buf.definition()<CR>', opts)
        vim.api.nvim_buf_set_keymap(bufnr, 'n', 'K', '<cmd>lua vim.lsp.buf.hover()<CR>', opts)
    end

    local capabilities = require('cmp_nvim_lsp').default_capabilities()

    -- NEW WAY: Configure LSPs with vim.lsp.config
    vim.lsp.config.pylsp = {
        cmd = { 'pylsp' },
        filetypes = { 'python' },
        root_markers = { 'pyproject.toml', 'setup.py', '.git' },
        on_attach = on_attach,
        capabilities = capabilities,
        settings = {
            pylsp = {
                plugins = {
                    pycodestyle = {
                        enabled = true,
                        maxLineLength = 150,
                    },
                    mccabe = { enabled = false },
                    pyflakes = { enabled = true },
                    pylint = { enabled = false },
                }
            }
        }
    }

    vim.lsp.config.rust_analyzer = {
        cmd = { 'rust-analyzer' },
        filetypes = { 'rust' },
        root_markers = { 'Cargo.toml' },
        on_attach = on_attach,
        capabilities = capabilities,
    }

    vim.lsp.config.lua_ls = {
        cmd = { 'lua-language-server' },
        filetypes = { 'lua' },
        root_markers = { '.luarc.json', '.luarc.jsonc', '.luacheckrc', '.stylua.toml', 'stylua.toml', 'selene.toml', 'selene.yml', '.git' },
        on_attach = on_attach,
        capabilities = capabilities,
        settings = {
            Lua = {
                diagnostics = {
                    globals = {'vim', 'require'}
                }
            }
        }
    }

    vim.lsp.config.groovyls = {
        cmd = { 'groovy-language-server' },
        filetypes = { 'groovy' },
        root_markers = { '.git' },
        on_attach = on_attach,
        capabilities = capabilities,
    }

    -- Enable all LSPs
    vim.lsp.enable('pylsp')
    vim.lsp.enable('rust_analyzer')
    vim.lsp.enable('lua_ls')
    vim.lsp.enable('groovyls')
end

return NvimModule
