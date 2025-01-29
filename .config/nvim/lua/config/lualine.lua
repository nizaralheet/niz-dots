local NvimModule = {}

function NvimModule.setup()
    vim.cmd([[hi WinBar guibg=NONE]])
    vim.cmd([[hi WinBarNC guibg=NONE]])
    require('lualine').setup {
      options = {
          theme = 'auto',
          section_separators = { left = '', right = '' },
          component_separators = { left = '│', right = '│' },
          disabled_filetypes= {
                'startify',
                'dashboard',
                'packer',
                'neogitstatus',
                'NvimTree',
                'Trouble',
                'alpha',
                'lir',
                'Outline',
                'spectre_panel',
                'toggleterm',
                'qf',
          },

      },
      sections = {
        lualine_a = { { icon =' ','mode', separator = { left = '',right = '' }, right_padding = 2 } },
        lualine_b = {
            'branch',
            {
            'diff',
            source = nil, -- A function that works as a data source for diff.
            'diff',
            symbols = {added = ' ', modified = ' ', removed = ' '},
            },
            'diagnostics'},
        lualine_c = { {'filename',symbols={modified='󰳻 ',readonly=' '} } },
        lualine_x = { 'fileformat', 'filetype' },
        lualine_y = { 'progress' },
        lualine_z = { { 'location', separator = { left ='', right = '' }, left_padding = 2 } }
      },
      inactive_sections = {
        lualine_a = { { 'filename', separator = { left = '' }, right_padding = 2 } },
        lualine_b = {},
        lualine_c = {},
        lualine_x = {},
        lualine_y = {},
        lualine_z = { { 'location', separator = { right = '' }, left_padding = 2 } }
      }
     }
end

return NvimModule
