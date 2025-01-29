
#!/bin/bash

# Directory containing images
image_dir="$HOME/wallpapers"

# Use Rofi to select an image, displaying previews as icons
selected_image=$(ls "$image_dir" | while read -r image; do
    echo -en "$image\x00icon\x1f$image_dir/$image\n"
done | rofi -dmenu -p "Select Image"  -config .config/rofi/wallpapers.rasi
 )

# Check if a valid image was selected
if [[ -n "$selected_image" ]]; then
  # Set the selected image using wpg
  wpg -s "$image_dir/$selected_image"
fi

