-- init.lua
-- Load core modules
 vim.g.loaded_netrw = 1
    vim.g.loaded_netrwPlugin = 1
require('core.bootstrap').setup()  -- Load bootstrap first
require('core.options').setup()    -- Then load options
require('core.keymaps').setup()    -- Then load keymaps

vim.g.neovide_padding_top = 18
vim.g.neovide_padding_bottom = 18
vim.g.neovide_padding_right = 25
vim.g.neovide_padding_left = 25
vim.o.guifont = "Iosevka NFP Medium:h17"
require('config').setup()

