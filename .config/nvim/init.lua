-- init.lua
-- Load core modules
require('core.bootstrap').setup()  -- Load bootstrap first
require('core.options').setup()    -- Then load options
require('core.keymaps').setup()    -- Then load keymaps

-- Initialize lazy.nvim
require("lazy").setup(require("plugins"), {
    install = { colorscheme = { "habamax","pywal" } },
    checker = { enabled = true },
    change_detection = {
    enabled = false, -- Completely turn off change detection
    notify = false,  -- Suppress notifications for plugin updates
    },
})

require('config').setup()
