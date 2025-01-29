local NvimModule = {}

function NvimModule.setup()
  local cmp = require("cmp")
  local luasnip = require("luasnip")

  require("luasnip.loaders.from_vscode").lazy_load()

  cmp.setup({
    sorting = {
        priority_weight = 2,
        comparators = {
            cmp.config.compare.offset,
            cmp.config.compare.exact,
            cmp.config.compare.score,
            cmp.config.compare.recently_used,
            cmp.config.compare.locality,
            cmp.config.compare.kind,
            cmp.config.compare.sort_text,
            cmp.config.compare.length,
            cmp.config.compare.order,
        },
    },
    snippet = {
      expand = function(args)
        luasnip.lsp_expand(args.body)
      end,
    },
    window = {
      completion = {
        border = "rounded",
        winhighlight = "Normal:Normal,FloatBorder:FloatBorder,CursorLine:Visual,Search:None",
        col_offset = -3,
        side_padding = 0,
        max_height = 15, -- Limit the dropdown height
      },
      documentation = {
        border = "rounded",
        max_height = 20,
      },
    },
    formatting = {
      fields = { "kind", "abbr", "menu" },
      format = function(entry, vim_item)
        -- Show source in menu
        vim_item.menu = ({
          nvim_lsp = "[LSP]",
          luasnip = "[Snippet]",
          buffer = "[Buffer]",
          path = "[Path]",
        })[entry.source.name]
        return vim_item
      end,
    },
    mapping = cmp.mapping.preset.insert({
      ["<C-b>"] = cmp.mapping.scroll_docs(-4),
      ["<C-f>"] = cmp.mapping.scroll_docs(4),
      ["<C-Space>"] = cmp.mapping.complete(),
      ["<C-e>"] = cmp.mapping.abort(),
      ["<CR>"] = cmp.mapping.confirm({ select = true }),
      ["<Tab>"] = cmp.mapping(function(fallback)
        if cmp.visible() then
          cmp.select_next_item()
        elseif luasnip.expand_or_jumpable() then
          luasnip.expand_or_jump()
        else
          fallback()
        end
      end, { "i", "s" }),
      ["<S-Tab>"] = cmp.mapping(function(fallback)
        if cmp.visible() then
          cmp.select_prev_item()
        elseif luasnip.jumpable(-1) then
          luasnip.jump(-1)
        else
          fallback()
        end
      end, { "i", "s" }),
    }),
    sources = cmp.config.sources({
      { 
        name = "nvim_lsp",
        entry_filter = function(entry, ctx)
          -- Filter out suggestions that are too short
          return entry:get_word():len() > 1
        end,
        max_item_count = 20, -- Limit number of suggestions
      },
      { name = "luasnip", max_item_count = 5 },
      { 
        name = "buffer", 
        max_item_count = 5,
        keyword_length = 3, -- Only show buffer suggestions after 3 characters
      },
      { name = "path", max_item_count = 5 },
    }),
    completion = {
      keyword_length = 1, -- Start suggesting after 1 character
      completeopt = "menu,menuone,noinsert",
    },
    matching = {
      disallow_fuzzy_matching = false,
      disallow_partial_matching = false,
      disallow_prefix_unmatching = true,
    },
  })

  -- Add specific filetype configuration for Python
  cmp.setup.filetype("python", {
    sources = cmp.config.sources({
      {
        name = "nvim_lsp",
        entry_filter = function(entry, ctx)
          -- Filter out suggestions that are too short
          return entry:get_word():len() > 1
        end,
        max_item_count = 20,
      },
      { name = "luasnip", max_item_count = 5 },
      { 
        name = "buffer", 
        max_item_count = 5,
        keyword_length = 3,
        option = {
          -- Get words from all buffers for better Python completion
          get_bufnrs = function()
            local bufs = {}
            for _, win in ipairs(vim.api.nvim_list_wins()) do
              bufs[vim.api.nvim_win_get_buf(win)] = true
            end
            return vim.tbl_keys(bufs)
          end
        }
      },
      { name = "path", max_item_count = 5 },
    }),
    -- Add this inside cmp.setup({...})
formatting = {
    fields = { "kind", "abbr", "menu" },
    format = function(entry, vim_item)
        local kind_icons = {
            Text = "󰉿",
            Method = "󰆧",
            Function = "󰊕",
            Constructor = "",
            Field = "󰜢",
            Variable = "󰀫",
            Class = "󰠱",
            Interface = "",
            Module = "",
            Property = "󰜢",
            Unit = "󰑭",
            Value = "󰎠",
            Enum = "",
            Keyword = "󰌋",
            Snippet = "",
            Color = "󰏘",
            File = "󰈙",
            Reference = "󰈇",
            Folder = "󰉋",
            EnumMember = "",
            Constant = "󰏿",
            Struct = "󰙅",
            Event = "",
            Operator = "󰆕",
            TypeParameter = "",
        }
        vim_item.kind = string.format('%s %s', kind_icons[vim_item.kind], vim_item.kind)
        vim_item.menu = ({
            nvim_lsp = "[LSP]",
            luasnip = "[Snippet]",
            buffer = "[Buffer]",
            path = "[Path]",
        })[entry.source.name]
        return vim_item
    end,
    },
  })
end

return NvimModule
