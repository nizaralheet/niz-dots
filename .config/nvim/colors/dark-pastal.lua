-- Custom Neovim Color Scheme
-- Save this file as ~/.config/nvim/colors/custom.lua
-- Then use :colorscheme custom in Neovim

local colors = {
  -- Backgrounds
  bg0 = "#0a0a0a",
  bg1 = "#0f0f0f",
  bg2 = "#1a1a1a", -- Slightly lighter for diagnostic backgrounds
  
  -- Foregrounds
  fg0 = "#f0f0f0",
  fg1 = "#d6d6d6",
  
  -- Enhanced palette colors (more vibrant but still pastel)
  black = "#0a0a0a",
  gray = "#bac2de",
  
  red = "#f28fad",        -- More vibrant pink-red
  bright_red = "#f5a3c7",
  
  green = "#b8f2c4",      -- More vibrant green
  bright_green = "#c2f0e8",
  
  yellow = "#fceaa1",     -- More vibrant yellow
  bright_yellow = "#ead581",
  
  blue = "#7e99fc",       -- More vibrant blue
  bright_blue = "#92a6ef",
  
  magenta = "#b97efc",    -- More vibrant magenta
  bright_magenta = "#ca8dfc",
  
  cyan = "#81ebf9",       -- More vibrant cyan
  bright_cyan = "#9ae6f0",
  
  white = "#bac2de",
  bright_white = "#f8c8e7",
  
  -- Visual selection colors (more visible)
  visual_bg = "#2a2a3a",      -- Darker purple-gray for selection
  visual_line_bg = "#252535", -- Slightly different for line selection
  
  -- Diagnostic colors (dimmed versions for backgrounds)
  diag_error_bg = "#2d1619",   -- Dark red background
  diag_warn_bg = "#2d2419",    -- Dark yellow background
  diag_info_bg = "#192629",    -- Dark blue background
  diag_hint_bg = "#1f2d29",    -- Dark cyan background
}

-- Clear existing highlights
vim.cmd("highlight clear")
if vim.fn.exists("syntax_on") then
  vim.cmd("syntax reset")
end

vim.o.background = "dark"
vim.g.colors_name = "custom"

local function hi(group, opts)
  vim.api.nvim_set_hl(0, group, opts)
end

-- Base highlights
hi("Normal", { fg = colors.fg0, bg = colors.bg0 })
hi("NormalFloat", { fg = colors.fg0, bg = colors.bg1 })
hi("NormalNC", { fg = colors.fg1, bg = colors.bg0 })

-- UI Elements
hi("ColorColumn", { bg = colors.bg1 })
hi("Cursor", { fg = colors.bg0, bg = colors.fg0 })
hi("CursorLine", { bg = colors.bg1 })
hi("CursorColumn", { bg = colors.bg1 })
hi("CursorLineNr", { fg = colors.bright_white, bold = true })
hi("LineNr", { fg = colors.gray })
hi("SignColumn", { fg = colors.gray, bg = colors.bg0 })
hi("VertSplit", { fg = colors.bg1, bg = colors.bg0 })
hi("WinSeparator", { fg = colors.bg1, bg = colors.bg0 })

-- Status line
hi("StatusLine", { fg = colors.fg0, bg = colors.bg1 })
hi("StatusLineNC", { fg = colors.fg1, bg = colors.bg1 })
hi("TabLine", { fg = colors.fg1, bg = colors.bg1 })
hi("TabLineFill", { fg = colors.fg1, bg = colors.bg1 })
hi("TabLineSel", { fg = colors.fg0, bg = colors.bg0 })

-- Popup menu
hi("Pmenu", { fg = colors.fg0, bg = colors.bg1 })
hi("PmenuSel", { fg = colors.bg0, bg = colors.blue })
hi("PmenuSbar", { bg = colors.bg1 })
hi("PmenuThumb", { bg = colors.gray })

-- Search
hi("Search", { fg = colors.bg0, bg = colors.yellow })
hi("IncSearch", { fg = colors.bg0, bg = colors.bright_yellow })
hi("Substitute", { fg = colors.bg0, bg = colors.red })

-- Visual selection
hi("Visual", { fg = colors.fg0, bg = colors.visual_bg })
hi("VisualNOS", { fg = colors.fg0, bg = colors.visual_line_bg })

-- Folding
hi("Folded", { fg = colors.gray, bg = colors.bg1 })
hi("FoldColumn", { fg = colors.gray, bg = colors.bg0 })

-- Syntax highlighting
hi("Comment", { fg = colors.gray, italic = true })
hi("Constant", { fg = colors.red })
hi("String", { fg = colors.green })
hi("Character", { fg = colors.green })
hi("Number", { fg = colors.red })
hi("Boolean", { fg = colors.red })
hi("Float", { fg = colors.red })

hi("Identifier", { fg = colors.cyan })
hi("Function", { fg = colors.blue })

hi("Statement", { fg = colors.magenta })
hi("Conditional", { fg = colors.magenta })
hi("Repeat", { fg = colors.magenta })
hi("Label", { fg = colors.magenta })
hi("Operator", { fg = colors.bright_magenta })
hi("Keyword", { fg = colors.magenta })
hi("Exception", { fg = colors.magenta })

hi("PreProc", { fg = colors.bright_cyan })
hi("Include", { fg = colors.bright_cyan })
hi("Define", { fg = colors.bright_cyan })
hi("Macro", { fg = colors.bright_cyan })
hi("PreCondit", { fg = colors.bright_cyan })

hi("Type", { fg = colors.yellow })
hi("StorageClass", { fg = colors.yellow })
hi("Structure", { fg = colors.yellow })
hi("Typedef", { fg = colors.yellow })

hi("Special", { fg = colors.bright_white })
hi("SpecialChar", { fg = colors.bright_white })
hi("Tag", { fg = colors.bright_white })
hi("Delimiter", { fg = colors.fg1 })
hi("SpecialComment", { fg = colors.gray })
hi("Debug", { fg = colors.red })

-- Errors and warnings
hi("Error", { fg = colors.red, bold = true })
hi("ErrorMsg", { fg = colors.red, bold = true })
hi("WarningMsg", { fg = colors.yellow, bold = true })
hi("Todo", { fg = colors.bg0, bg = colors.yellow, bold = true })

-- Diff
hi("DiffAdd", { fg = colors.green, bg = colors.bg1 })
hi("DiffChange", { fg = colors.yellow, bg = colors.bg1 })
hi("DiffDelete", { fg = colors.red, bg = colors.bg1 })
hi("DiffText", { fg = colors.blue, bg = colors.bg1, bold = true })

-- Spell checking
hi("SpellBad", { fg = colors.red, underline = true })
hi("SpellCap", { fg = colors.yellow, underline = true })
hi("SpellLocal", { fg = colors.cyan, underline = true })
hi("SpellRare", { fg = colors.magenta, underline = true })

-- LSP highlights with subtle background differentiation
hi("DiagnosticError", { fg = colors.red })
hi("DiagnosticWarn", { fg = colors.yellow })
hi("DiagnosticInfo", { fg = colors.blue })
hi("DiagnosticHint", { fg = colors.cyan })

hi("DiagnosticSignError", { fg = colors.red, bg = colors.bg0 })
hi("DiagnosticSignWarn", { fg = colors.yellow, bg = colors.bg0 })
hi("DiagnosticSignInfo", { fg = colors.blue, bg = colors.bg0 })
hi("DiagnosticSignHint", { fg = colors.cyan, bg = colors.bg0 })

-- Virtual text diagnostics with subtle backgrounds
hi("DiagnosticVirtualTextError", { fg = colors.red, bg = colors.diag_error_bg })
hi("DiagnosticVirtualTextWarn", { fg = colors.yellow, bg = colors.diag_warn_bg })
hi("DiagnosticVirtualTextInfo", { fg = colors.blue, bg = colors.diag_info_bg })
hi("DiagnosticVirtualTextHint", { fg = colors.cyan, bg = colors.diag_hint_bg })

-- Underline diagnostics for better code distinction
hi("DiagnosticUnderlineError", { undercurl = true, sp = colors.red })
hi("DiagnosticUnderlineWarn", { undercurl = true, sp = colors.yellow })
hi("DiagnosticUnderlineInfo", { undercurl = true, sp = colors.blue })
hi("DiagnosticUnderlineHint", { undercurl = true, sp = colors.cyan })

-- Tree-sitter highlights (optional, for better syntax highlighting)
hi("@variable", { fg = colors.fg0 })
hi("@variable.builtin", { fg = colors.red })
hi("@variable.parameter", { fg = colors.bright_yellow })
hi("@variable.member", { fg = colors.cyan })

hi("@constant", { fg = colors.red })
hi("@constant.builtin", { fg = colors.red })
hi("@constant.macro", { fg = colors.bright_cyan })

hi("@string", { fg = colors.green })
hi("@string.regex", { fg = colors.bright_green })
hi("@string.escape", { fg = colors.bright_white })

hi("@character", { fg = colors.green })
hi("@character.special", { fg = colors.bright_white })

hi("@number", { fg = colors.red })
hi("@boolean", { fg = colors.red })
hi("@float", { fg = colors.red })

hi("@function", { fg = colors.blue })
hi("@function.builtin", { fg = colors.bright_blue })
hi("@function.macro", { fg = colors.bright_cyan })
hi("@function.method", { fg = colors.blue })

hi("@constructor", { fg = colors.yellow })
hi("@operator", { fg = colors.bright_magenta })

hi("@keyword", { fg = colors.magenta })
hi("@keyword.function", { fg = colors.magenta })
hi("@keyword.operator", { fg = colors.bright_magenta })
hi("@keyword.return", { fg = colors.magenta })

hi("@type", { fg = colors.yellow })
hi("@type.builtin", { fg = colors.yellow })
hi("@type.definition", { fg = colors.yellow })

hi("@property", { fg = colors.cyan })
hi("@field", { fg = colors.cyan })

hi("@punctuation.delimiter", { fg = colors.fg1 })
hi("@punctuation.bracket", { fg = colors.fg1 })
hi("@punctuation.special", { fg = colors.bright_white })

hi("@comment", { fg = colors.gray, italic = true })
hi("@comment.documentation", { fg = colors.gray, italic = true })

hi("@tag", { fg = colors.magenta })
hi("@tag.attribute", { fg = colors.cyan })
hi("@tag.delimiter", { fg = colors.fg1 })

-- Git signs (if using gitsigns.nvim)
hi("GitSignsAdd", { fg = colors.green, bg = colors.bg0 })
hi("GitSignsChange", { fg = colors.yellow, bg = colors.bg0 })
hi("GitSignsDelete", { fg = colors.red, bg = colors.bg0 })

-- Telescope (if using telescope.nvim)
hi("TelescopeBorder", { fg = colors.bg1, bg = colors.bg0 })
hi("TelescopePromptBorder", { fg = colors.bg1, bg = colors.bg0 })
hi("TelescopePromptNormal", { fg = colors.fg0, bg = colors.bg1 })
hi("TelescopePromptPrefix", { fg = colors.blue })
hi("TelescopeNormal", { fg = colors.fg0, bg = colors.bg0 })
hi("TelescopePreviewTitle", { fg = colors.bg0, bg = colors.green })
hi("TelescopePromptTitle", { fg = colors.bg0, bg = colors.blue })
hi("TelescopeResultsTitle", { fg = colors.bg0, bg = colors.magenta })
hi("TelescopeSelection", { fg = colors.fg0, bg = colors.bg1 })
hi("TelescopeSelectionCaret", { fg = colors.blue, bg = colors.bg1 })

-- NvimTree (if using nvim-tree.lua)
hi("NvimTreeNormal", { fg = colors.fg0, bg = colors.bg0 })
hi("NvimTreeFolder", { fg = colors.blue })
hi("NvimTreeOpenedFolder", { fg = colors.bright_blue })
hi("NvimTreeEmptyFolder", { fg = colors.gray })
hi("NvimTreeFolderIcon", { fg = colors.blue })
hi("NvimTreeRootFolder", { fg = colors.magenta, bold = true })
hi("NvimTreeSpecialFile", { fg = colors.bright_white })
hi("NvimTreeExecFile", { fg = colors.green })
hi("NvimTreeImageFile", { fg = colors.cyan })
hi("NvimTreeGitDirty", { fg = colors.yellow })
hi("NvimTreeGitStaged", { fg = colors.green })
hi("NvimTreeGitMerge", { fg = colors.magenta })
hi("NvimTreeGitRenamed", { fg = colors.bright_magenta })
hi("NvimTreeGitNew", { fg = colors.bright_green })
hi("NvimTreeGitDeleted", { fg = colors.red })

-- Additional UI elements
hi("Directory", { fg = colors.blue })
hi("Title", { fg = colors.magenta, bold = true })
hi("MoreMsg", { fg = colors.green })
hi("ModeMsg", { fg = colors.fg0 })
hi("Question", { fg = colors.cyan })
hi("WildMenu", { fg = colors.bg0, bg = colors.blue })
hi("MatchParen", { fg = colors.bright_white, bg = colors.bg1, bold = true })
hi("NonText", { fg = colors.gray })
hi("SpecialKey", { fg = colors.gray })
hi("Whitespace", { fg = colors.gray })

-- Terminal colors (for :terminal) - updated with enhanced colors
vim.g.terminal_color_0 = colors.black
vim.g.terminal_color_1 = colors.red
vim.g.terminal_color_2 = colors.green
vim.g.terminal_color_3 = colors.yellow
vim.g.terminal_color_4 = colors.blue
vim.g.terminal_color_5 = colors.magenta
vim.g.terminal_color_6 = colors.cyan
vim.g.terminal_color_7 = colors.white
vim.g.terminal_color_8 = colors.gray
vim.g.terminal_color_9 = colors.bright_red
vim.g.terminal_color_10 = colors.bright_green
vim.g.terminal_color_11 = colors.bright_yellow
vim.g.terminal_color_12 = colors.bright_blue
vim.g.terminal_color_13 = colors.bright_magenta
vim.g.terminal_color_14 = colors.bright_cyan
vim.g.terminal_color_15 = colors.bright_white
