local NvimModule = {}

function NvimModule.setup()
  local navic = require("nvim-navic")

  navic.setup({
    icons = {
        File = "",
        Module = "",
        Namespace = "",
        Package = "",
        Class = "",
        Method = "",
        Property = "",
        Field = "",
        Constructor = "",
        Enum = "",
        Interface = "",
        Function = "",
        Variable = "",
        Constant = "",
        String = "",
        Number = "",
        Boolean = "",
        Array = "",
        Object = "",
        Key = "",
        Null = "󰟢",
        EnumMember = "",
        Struct = "",
        Event = "",
        Operator = "",
        TypeParameter = ""
    },
    highlight = true,
    separator = " > ",
    depth_limit = 0,
    depth_limit_indicator = "..",
    safe_output = true
  })

  -- Attach navic to all LSP clients
  vim.api.nvim_create_autocmd("LspAttach", {
    callback = function(args)
      local buffer = args.buf
      local client = vim.lsp.get_client_by_id(args.data.client_id)
      if client.server_capabilities.documentSymbolProvider then
        navic.attach(client, buffer)
      end
    end,
  })
end

return NvimModule
