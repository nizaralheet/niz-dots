-- lua/config/alpha.lua
local NvimModule = {}

function NvimModule.setup()
    local alpha = require("alpha")
    local dashboard = require("alpha.themes.dashboard")

    -- Set header
    dashboard.section.header.val = {
        "                                              ",
        "       ████ ██████           █████      ██",
        "      ███████████             █████ ",
        "      █████████ ███████████████████ ███   ███████████",
        "     █████████  ███    █████████████ █████ ██████████████",
        "    █████████ ██████████ █████████ █████ █████ ████ █████",
        "  ███████████ ███    ███ █████████ █████ █████ ████ █████",
        " ██████  █████████████████████ ████ █████ █████ ████ ██████",
            }

    -- Set menu
    dashboard.section.buttons.val = {
        dashboard.button( "e", "   New File" , ":ene <BAR> startinsert <CR>"),
        dashboard.button( "f", " 󰮗  Find File", ":cd $HOME/ | Telescope find_files<CR>"),
        dashboard.button( "r", "   Recent Files"   , ":Telescope oldfiles<CR>"),
        dashboard.button( "c", "   Configuration" , ":e $MYVIMRC | :cd %:p:h | split . | wincmd k | pwd<CR>"),
        dashboard.button( "l", " 󰒲  Lazy ", ":Lazy<CR>"),
        dashboard.button( "q", "   Quit NVIM", ":qa<CR>"),
    }

    -- Send config to alpha
    alpha.setup(dashboard.opts)

    -- Disable folding on alpha buffer
    vim.cmd([[
        autocmd FileType alpha setlocal nofoldenable
    ]])
     require("alpha").setup(dashboard.opts)

    -- show the cost time of plugins loading
    vim.api.nvim_create_autocmd("User", {
        pattern = "LazyVimStarted",
        callback = function()
            local stats = require("lazy").stats()
            local ms = (math.floor(stats.startuptime * 100 + 0.5) / 100)
            dashboard.section.footer.val = "⚡ Neovim loaded "
                                            .. stats.loaded
                                            .. "/"
                                            .. stats.count
                                            .. " plugins in "
                                            .. ms .. "ms"
            pcall(vim.cmd.AlphaRedraw)
        end,})
end

return NvimModule
