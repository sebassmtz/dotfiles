import os
import subprocess

from libqtile import hook


from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

#Fonts
default_font = "Roboto Mono"
#red_device = "wslan0" # ip address

#Sizes
size_bar = 30
size_font = 15
size_icon = 24

#Colors
bg_color = "#282a36"
fg_color = "#ffffff"
color_bar = "#282a36"
inactive_color = "#6272A4"
active_color = "#362F2D"
dark_color = "#44475a"
light_color = "#535A82"
urgent_color = "#FF5555"
color_updates = "#bc0000"

#Space for definir functions


def longNameParse(text): 
    for string in ["Brave", "Firefox"]:
        if string in text:
            text = string
        else:
            text = text
    return text

#Funcion de separador
def fc_separator(size):
    return widget.Sep(
        linewidth = 0,
        padding = size,
        foreground = fg_color,
        background = bg_color,
    )

def fc_spacer(size):
    return widget.Spacer(
        length = size,
        background = color_bar,
    )

#Funcion para escribir texto o un icono
def fc_icon(icon,group_color,space):
    return widget.TextBox(
        text = icon,
        foreground = fg_color,
        background = group_color,
        fontsize = size_font,
        padding = space,
    )

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    # Tecla para lanzar el menu de rofi
    Key([mod], "m",lazy.spawn("rofi -show drun"), desc="Open menu"),
    Key([mod, "shift"], "m", lazy.spawn("rofi -show window")), 
    #Tecla para abrir el navegador Brave
    Key([mod], "b",lazy.spawn("brave"), desc="Open brave"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Configuracion para las teclas de volumen (PulseAudio)
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

     #configuracion para las teclas de brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    #Capturar pantalla
    Key([mod], "s", lazy.spawn("scrot /home/sebas/Images/'%Y-%m-%d-%T-screen.png'")),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s /home/sebas/Images/'%Y-%m-%d-%T-screenshot.png'")), 
]

groups = [Group(i) for i in [
    "  ","  ","  ","  ","  ","  ",
]]

for i, group in enumerate(groups):
    desktopNumber = str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                desktopNumber,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                desktopNumber,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
        ]
    )

layouts = [
    layout.Columns(
        #To do...
        #border_focus_stack=["#ffffff","#ffffff"],
        border_width=0,
        #border_normal = "#ffffff",
        #border_normal_stack = "#ffffff",
        margin = [5,2,5,2],
    ),
    layout.Max(
    ),
    layout.MonadTall(
        border_width=0,
        margin = 3,
        
    ),
]

widget_defaults = dict(
    font=default_font,
    fontsize=size_font,
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                fc_separator(16),
                widget.Prompt(),
                #Thermal and Memory (Group 1)
                fc_icon("  ",color_bar,-3), # nf-fa-thermometer_2
                widget.ThermalSensor(
                    background = color_bar,
                    foreground = fg_color,
                    fontsize = size_font,
                    threshold = 70,
                    #tag_sensor = "temp1",
                    fmt = ' T: {} '
                ),
                fc_icon("   ",color_bar,-3), # nf-fa-save
                widget.Memory(
                    background = color_bar,
                    foreground = "#ffffff",
                    fontsize = size_font,
                ),
                fc_separator(16),
                fc_spacer(50),
                #Muestra los menus
                widget.GroupBox(
                    active=active_color,
                    borderwidth=1,
                    disable_drag=True,
                    fontsize=size_icon,
                    foreground= fg_color,
                    highlight_method = 'block',
                    inactive = inactive_color,
                    margin_x = 0,
                    margin_y = 5,
                    other_current_screen_border = dark_color,
                    other_screen_border = dark_color,
                    padding_x = 0,
                    padding_y = 10,
                    this_current_screen_border = light_color,
                    this_screen_border = light_color,
                    urgent_alert_method = 'block',
                    urgent_border = urgent_color,
                ),
                fc_separator(16),
                #Volume
                fc_icon(" 墳 ", color_bar,-3),# nf-fa-volume_up
                widget.PulseVolume(
                    limit_max_volume = True,
                    update_interval = 0.05,
                    fontsize = size_font,
                ),
                fc_separator(16),
                fc_separator(16),
                #Date (Group 3)
                widget.Clock(
                    background = bg_color,
                    foreground = fg_color,
                    format=" %d %b, %Y  %H:%M %p",
                    #fontshadow = color_group3,
                ),
                #Power Off
                fc_separator(16),
                widget.QuickExit(
                    default_text = " 襤 ",
                    countdown_format=' {} ',
                    countdown_start = 5,
                    fontsize = size_font,
                    padding =0,

                ),
            ],
            size_bar,
            background= color_bar,
            border_width=[0, 0, 0, 0],  # Draw top and bottom borders
        ),
        bottom=bar.Bar(
            [
                #Layaout (Group 4)
                widget.CurrentLayoutIcon(
                    background = color_bar,
                    scale = 0.75,
                    padding= 1,
                ),
                fc_spacer(1),
                #Network  (Group 2)
                widget.Net(
                    foreground = fg_color,
                    background = color_bar,
                    fontsize = size_font,
                    format = '  {down}   {up}',
                    prefix = 'k',
                    #interface = red_device,
                    use_bits = 'true',
                    padding = 3,
                ),

                fc_spacer(150),
                widget.WindowName(
                    #parse_text=longNameParse,
                    background = bg_color,
                    foreground = "#ffffff",
                    format = '{state}{name}',
                    font = default_font,
                    
                ),
                fc_spacer(8),
                widget.CPU(
                    format = ' {freq_current}GHz  {load_percent}%',  # Cambiar estos iconos
                    update_interval = 0.9,
                    padding = 3,
                ),
                fc_spacer(8),
                # fc_icon("  ",color_bar,-3),
                # widget.CheckUpdates(
                #     background= color_bar,
                #     colour_have_updates= color_updates,
                #     colour_no_updates = fg_color,
                #     no_update_string = '0',
                #     display_format = '{updates}',
                #     update_interval = 1800,
                #     distro = 'Arch_checkupdates',
                #     ontsize = size_font,
                # ),

                #Icons Systray
                widget.Systray(
                    icon_size = size_icon,
                    background = bg_color,
                ),
                fc_spacer(2),
                
            ],
            18,
            background = color_bar,
            border_width=[0, 0, 0, 0],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
