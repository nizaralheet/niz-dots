from qtile_extras.popup.toolkit import PopupGridLayout
from qtile_extras.popup.menu import PopupMenuItem, PopupMenuSeparator
import subprocess
import os
from pathlib import Path
import colors
# ============================================
# MENU STYLING - CUSTOMIZE COLORS HERE
# ============================================

MENU_STYLE = {
    "width": 250,
    "background": colors.Color1,
    "foreground": colors.Color15,
    "highlight": colors.Color15,
    "highlight_foreground": colors.Color0,
    "highlight_danger": "#f38ba8",
    "separator_color": colors.Color10,
    "border": colors.Color1,
    "border_width": 2,
    "fontsize": 14,
    "font": "JetBrainsMono Nerd Font",
    "opacity": 0.95,
}

# Icon theme settings
ICON_THEME = "Promix"  # Change this to your icon theme name
ICON_SIZE = 24  # Icon size in pixels

ICON_PATHS = [
    "~/.local/share/icons",
    "/usr/share/icons",
]

# Valid categories (in order)
VALID_CATEGORIES = [
    "AudioVideo",
    "Development",
    "Education",
    "Game",
    "Graphics",
    "Network",
    "Office",
    "Science",
    "Settings",
    "System",
    "Utility",
    "Other",
]

# Paths to search for .desktop files
DESKTOP_PATHS = [
    "/usr/share/applications",
    "/usr/local/share/applications",
    "~/.local/share/applications",
]


# ============================================
# ICON FINDER
# ============================================

def find_icon(icon_name):
    """
    Find icon file path for given icon name in the icon theme
    Returns None if not found
    """
    if not icon_name:
        return None
    
    # If icon_name is already a full path, return it
    if icon_name.startswith("/") and os.path.isfile(icon_name):
        return icon_name
    
    # Common icon extensions
    extensions = [".png", ".svg", ".xpm"]
    
    # Common icon sizes to search (in order of preference)
    sizes = [str(ICON_SIZE), "24", "32", "48", "64", "128", "256", "scalable"]
    
    # Search in icon theme directories
    for base_path in ICON_PATHS:
        icon_base = Path(base_path).expanduser()
        
        # Look for the specific theme first
        theme_path = icon_base / ICON_THEME
        if theme_path.exists():
            # Search in apps directories
            for size in sizes:
                for subdir in ["apps", "places", "categories", "actions", "devices", "mimetypes"]:
                    search_dir = theme_path / size / subdir
                    if search_dir.exists():
                        for ext in extensions:
                            icon_file = search_dir / f"{icon_name}{ext}"
                            if icon_file.exists():
                                return str(icon_file)
        
        # Fallback: search in hicolor theme
        hicolor_path = icon_base / "hicolor"
        if hicolor_path.exists():
            for size in sizes:
                for subdir in ["apps", "places", "categories", "actions", "devices", "mimetypes"]:
                    search_dir = hicolor_path / size / subdir
                    if search_dir.exists():
                        for ext in extensions:
                            icon_file = search_dir / f"{icon_name}{ext}"
                            if icon_file.exists():
                                return str(icon_file)
    
    return None


# ============================================
# DESKTOP FILE PARSER
# ============================================

def parse_desktop_file(filepath):
    """Parse a .desktop file and extract name, exec, icon, and categories"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        name = None
        exec_cmd = None
        icon = None
        categories = []
        no_display = False
        
        for line in lines:
            line = line.strip()
            
            if line.startswith("Name=") and not name:
                name = line.split("=", 1)[1]
            elif line.startswith("Exec="):
                exec_cmd = line.split("=", 1)[1]
                # Remove field codes like %F, %U, etc.
                exec_cmd = exec_cmd.replace("%F", "").replace("%U", "").replace("%f", "").replace("%u", "")
                exec_cmd = exec_cmd.strip()
            elif line.startswith("Icon="):
                icon = line.split("=", 1)[1].strip()
            elif line.startswith("Categories="):
                cats = line.split("=", 1)[1]
                categories = [c.strip() for c in cats.split(";") if c.strip()]
            elif line.startswith("NoDisplay=true"):
                no_display = True
        
        if name and exec_cmd and not no_display:
            return {
                "name": name,
                "exec": exec_cmd,
                "icon": icon,
                "categories": categories
            }
    except Exception as e:
        pass
    
    return None


def get_all_applications():
    """Scan all .desktop files and organize by category"""
    apps_by_category = {cat: [] for cat in VALID_CATEGORIES}
    
    for path in DESKTOP_PATHS:
        desktop_dir = Path(path).expanduser()
        if not desktop_dir.exists():
            continue
        
        for desktop_file in desktop_dir.glob("*.desktop"):
            app = parse_desktop_file(desktop_file)
            if not app:
                continue
            
            # Find icon path for this app
            app['icon_path'] = find_icon(app.get('icon'))
            
            # Get FIRST matching valid category only
            primary_category = "Other"
            for cat in app["categories"]:
                if cat in VALID_CATEGORIES:
                    primary_category = cat
                    break
            
            apps_by_category[primary_category].append(app)
    
    # Sort apps within each category and remove empty categories
    result = {}
    for category, apps in apps_by_category.items():
        if apps:  # Only include categories with apps
            apps.sort(key=lambda x: x["name"])
            result[category] = apps
    
    return result


# ============================================
# MENU STATE
# ============================================

class MenuState:
    current_menu = None  # Track current open menu
    current_submenu = None  # Track current open submenu


# ============================================
# MENU FUNCTIONS
# ============================================

def qtile_menu(qtile):
    """
    Display main start menu with categories
    """
    # Close any existing menus
    if MenuState.current_submenu:
        MenuState.current_submenu.hide()
        MenuState.current_submenu = None
    if MenuState.current_menu:
        MenuState.current_menu.hide()
        MenuState.current_menu = None
        return
    
    # Get all applications organized by category
    apps_by_category = get_all_applications()
    
    # Build main menu with categories
    controls = []
    current_row = 0
    
    # Add category items (only categories that have apps)
    for category in VALID_CATEGORIES:
        if category not in apps_by_category:
            continue
        
        apps = apps_by_category[category]
        controls.append(
            PopupMenuItem(
                text=f"  {category}",
                mouse_callbacks={
                    "Button1": lambda q=qtile, c=category, a=apps: show_submenu(q, c, a)
                },
                highlight=MENU_STYLE["highlight"],
                foreground=MENU_STYLE["foreground"],
                foreground_highlighted=MENU_STYLE["highlight_foreground"],
                fontsize=MENU_STYLE["fontsize"],
                font=MENU_STYLE["font"],
                row=current_row,
                col=0,
                col_span=1,
                row_span=2,
                has_submenu=True,
            )
        )
        current_row += 2
    
    # Add separator
    controls.append(
        PopupMenuSeparator(
            colour_above=MENU_STYLE["separator_color"],
            row=current_row,
            col=0,
            col_span=1,
            row_span=1,
        )
    )
    current_row += 1
    
    # Add system items
    system_items = [
        ("  Lock", "betterlockscreen -l", False),
        ("  Logout", "qtile-logout", False),
        ("  Reboot", "systemctl reboot", True),
        ("  Shutdown", "systemctl poweroff", True),
    ]
    
    for label, command, is_dangerous in system_items:
        highlight_color = MENU_STYLE["highlight_danger"] if is_dangerous else MENU_STYLE["highlight"]
        controls.append(
            PopupMenuItem(
                text=label,
                mouse_callbacks={
                    "Button1": lambda q=qtile, cmd=command: execute_command(q, cmd)
                },
                highlight=highlight_color,
                foreground=MENU_STYLE["foreground"],
                foreground_highlighted=MENU_STYLE["highlight_foreground"],
                fontsize=MENU_STYLE["fontsize"],
                font=MENU_STYLE["font"],
                row=current_row,
                col=0,
                col_span=1,
                row_span=2,
            )
        )
        current_row += 2
    
    total_rows = current_row
    total_height = total_rows * 20
    
    # Create main menu
    layout = PopupGridLayout(
        qtile,
        rows=total_rows,
        cols=1,
        width=MENU_STYLE["width"],
        height=total_height,
        controls=controls,
        background=MENU_STYLE["background"],
        border=MENU_STYLE["border"],
        border_width=MENU_STYLE["border_width"],
        close_on_click=False,
        hide_on_mouse_leave=True,
        opacity=MENU_STYLE["opacity"],
    )
    
    layout.show(x=10, y=10, relative_to=1, relative_to_bar=True)
    MenuState.current_menu = layout


def show_submenu(qtile, category, apps):
    """
    Display submenu with apps for selected category
    """
    # Close existing submenu
    if MenuState.current_submenu:
        MenuState.current_submenu.hide()
    
    controls = []
    current_row = 0
    
    # Add back button
    controls.append(
        PopupMenuItem(
            text="<- Back",
            mouse_callbacks={
                "Button1": lambda: hide_submenu()
            },
            highlight=MENU_STYLE["highlight"],
            foreground=MENU_STYLE["foreground"],
            foreground_highlighted=MENU_STYLE["highlight_foreground"],
            fontsize=MENU_STYLE["fontsize"],
            font=MENU_STYLE["font"],
            row=current_row,
            col=0,
            col_span=1,
            row_span=2,
        )
    )
    current_row += 2
    
    # Add separator
    controls.append(
        PopupMenuSeparator(
            colour_above=MENU_STYLE["separator_color"],
            row=current_row,
            col=0,
            col_span=1,
            row_span=1,
        )
    )
    current_row += 1
    
    # Add apps
    for app in apps:
        icon_path = app.get('icon_path')  # Get pre-found icon path
        
        controls.append(
            PopupMenuItem(
                text=f"  {app['name']}",
                mouse_callbacks={
                    "Button1": lambda q=qtile, cmd=app['exec']: launch_app_and_close(q, cmd)
                },
                highlight=MENU_STYLE["highlight"],
                foreground=MENU_STYLE["foreground"],
                foreground_highlighted=MENU_STYLE["highlight_foreground"],
                fontsize=MENU_STYLE["fontsize"],
                font=MENU_STYLE["font"],
                row=current_row,
                col=0,
                col_span=1,
                row_span=2,
                menu_icon=icon_path,
                icon_size=ICON_SIZE,
                show_icon=True,
            )
        )
        current_row += 2
    
    total_rows = current_row
    total_height = min(total_rows * 20, 600)  # Max height of 600px
    
    # Create submenu positioned to the right of main menu
    layout = PopupGridLayout(
        qtile,
        rows=total_rows,
        cols=1,
        width=MENU_STYLE["width"],
        height=total_height,
        controls=controls,
        background=MENU_STYLE["background"],
        border=MENU_STYLE["border"],
        border_width=MENU_STYLE["border_width"],
        close_on_click=False,
        hide_on_mouse_leave=True,
        opacity=MENU_STYLE["opacity"],
    )
    
    # Position submenu to the right of main menu
    layout.show(x=MENU_STYLE["width"] + 20, y=10, relative_to=1, relative_to_bar=True)
    MenuState.current_submenu = layout


def hide_submenu():
    """Hide the submenu"""
    if MenuState.current_submenu:
        MenuState.current_submenu.hide()
        MenuState.current_submenu = None


def launch_app_and_close(qtile, command):
    """Launch app and close all menus"""
    execute_command(qtile, command)
    
    # Close submenu
    if MenuState.current_submenu:
        MenuState.current_submenu.hide()
        MenuState.current_submenu = None
    
    # Close main menu
    if MenuState.current_menu:
        MenuState.current_menu.hide()
        MenuState.current_menu = None


def execute_command(qtile, command):
    """Execute the command - handles special qtile commands"""
    if command == "qtile-logout":
        qtile.cmd_shutdown()
    else:
        # Launch command
        try:
            subprocess.Popen(command, shell=True)
        except Exception as e:
            print(f"Error launching {command}: {e}")
    
    # Close all menus
    if MenuState.current_submenu:
        MenuState.current_submenu.hide()
        MenuState.current_submenu = None
    if MenuState.current_menu:
        MenuState.current_menu.hide()
        MenuState.current_menu = None



