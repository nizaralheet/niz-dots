local NvimModule = {}

function NvimModule.setup()
    require("barbecue").setup({
        theme= 'auto',
        show_basename = true,
        show_dirname = false ,
        show_modified = true,
        symbols = {
            modified = '󰽂 ',  -- Replace the default circle with the desired icon
        },
    })
end
return NvimModule
