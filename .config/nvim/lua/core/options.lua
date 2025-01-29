local NvimModule = {}

local cache_dir = vim.fn.expand("$HOME") .. "/.cache/nvim"
local undodir = cache_dir .. "/undo"

if vim.fn.isdirectory(undodir) == 0 then
  vim.fn.mkdir(undodir, "p")
end
--vim.o.winbar = '%f'

--vim.o.winbar = "%{%v:lua.require'nvim-navic'.get_location()%}"
function NvimModule.setup()
    local options = {
        title = true,
        undofile = true,
        undodir = undodir,
        linebreak =true,
        wrap = false ,
        number = true,         -- Show line numbers
        relativenumber = true, -- Show relative line numbers
        tabstop = 4,          -- Number of spaces per tab
        shiftwidth = 4,       -- Number of spaces for autoindent
        expandtab = true,     -- Convert tabs to spaces
        clipboard = "unnamedplus",
        swapfile = false,
        showmode = false,
    }

    for k, v in pairs(options) do
        vim.opt[k] = v
    end
end

return NvimModule
