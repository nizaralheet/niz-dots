local NvimModule = {}
local cache_dir = vim.fn.expand("$HOME") .. "/.cache/nvim"
local undodir = cache_dir .. "/undo"
    vim.cmd('colorscheme dark-pastal')
    vim.cmd(string.format('highlight SnacksPicker guibg=None'))
vim.cmd('cnoreabbrev suw Suw')
vim.api.nvim_create_user_command('Suw', function()
  local file = vim.fn.expand('%')
  if file == '' then
    vim.notify('No file to save', vim.log.levels.ERROR)
    return
  end

  vim.cmd('w !sudo tee % > /dev/null')
  vim.cmd('edit!')
  vim.notify('File saved with sudo', vim.log.levels.INFO)
end, { desc = 'Save with sudo' })

-- Auto cd into buffer's directory
-- Auto cd into buffer's directory (safer version)
-- Create an autocommand group to prevent stacking
local cd_group = vim.api.nvim_create_augroup("AutoCD", { clear = true })

vim.api.nvim_create_autocmd("BufEnter", {
  group = cd_group,
  pattern = "*",
  callback = function()
    -- Get the full path of the buffer's directory
    -- vim.fn.expand returns an empty string for unlisted/special buffers
    local buffer_dir = vim.fn.expand("%:p:h")

    -- Only continue if the buffer has a real directory
    -- Also, don't run on special buffer types like 'nofile', 'terminal', etc.
    if buffer_dir == "" or vim.bo.buftype ~= "" then
      return
    end

    -- Get the current working directory
    local current_dir = vim.fn.getcwd()

    -- Compare and change directory only if they are different
    if buffer_dir ~= current_dir then
      -- Use vim.fn.chdir() which is the API equivalent of :cd
      vim.fn.chdir(buffer_dir)
      -- You could add a print statement to see when it changes:
      -- print("Changed directory to: " .. buffer_dir)
    end
  end,
})
vim.api.nvim_create_user_command('W', 'w', {})
vim.api.nvim_create_user_command('Q', 'q', {})

vim.api.nvim_create_user_command('WQ', function() vim.cmd('wq') end, {})
vim.api.nvim_create_user_command('Wq', function() vim.cmd('wq') end, {})

vim.diagnostic.config({
  virtual_text = {
    prefix = '!',  -- You can change to '■', '▎', '→', or ''
    spacing = 2,
  },
  signs = true,
  underline = true,
  update_in_insert = false,
  severity_sort = true,
})
if vim.fn.isdirectory(undodir) == 0 then
  vim.fn.mkdir(undodir, "p")
end

function NvimModule.setup()

  -- Your existing highlight groups
  local hl_groups = {
    "Normal",
    "NvimTreeNormalFloat",
    "StatusLineNC",
    "TelescopePromptTitle",
    "SnacksPickerInputBorder",
    "SnacksPickerInputTitle",
    "StatusLine",
    "SignColumn",
    "NormalNC",
    "TelescopeBorder",
    "NvimTreeNormal",
    "NvimTreeNormalNC",
    "NeoTreeNormal",
    "NeoTreeNormalNC",
    "EndOfBuffer",
    "MsgArea",
    "SnacksNormal",
    "SnacksNormalNC",
    "TelescopeNormal",
    "TelescopePromptBorder",
    "LspInfoBorder",
    "FloatBorder",
    "SnacksPicker",
  }
  
  -- Get all Snacks highlight groups using vim.api
  local snacks_highlights = vim.fn.getcompletion("Snacks", "highlight")
  
  -- Add all Snacks highlight groups to our list
  for _, hl_name in ipairs(snacks_highlights) do
    -- Check if the highlight group is not already in our list
    local found = false
    for _, existing in ipairs(hl_groups) do
      if existing == hl_name then
        found = true
        break
      end
    end
    
    if not found then
      table.insert(hl_groups, hl_name)
    end
  end
  
  -- Apply transparent background to all groups
  for _, name in ipairs(hl_groups) do
    vim.cmd(string.format("highlight %s ctermbg=none guibg=none", name))
  end
      vim.opt.fillchars = "eob: "

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
        termguicolors = true,

    }

    for k, v in pairs(options) do
        vim.opt[k] = v
    end
end

vim.api.nvim_create_autocmd({ "VimEnter" }, {
  callback = function()
    local arg = vim.fn.argv(0)
    if arg ~= "" and vim.fn.isdirectory(arg) == 1 then
      require("nvim-tree.api").tree.open()
    end
  end
})
return NvimModule
