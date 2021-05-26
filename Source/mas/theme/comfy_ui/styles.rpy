################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################

################################################################################
# Init
################################################################################
init python:
    config.font_replacement_map[comfy_ui.common.font_regular, False, True] = (comfy_ui.common.font_italic, False, False)
    config.font_replacement_map[comfy_ui.common.font_regular, True, False] = (comfy_ui.common.font_bold, False, False)
    config.font_replacement_map[comfy_ui.common.font_regular, True, True] = (comfy_ui.common.font_bold_italic, False, False)



################################################################################
# Definitions
################################################################################
define gui.default_font                           = comfy_ui.common.font
define mas_ui.light_button_text_idle_color        = comfy_ui.button_text.light.idle_color
define mas_ui.light_button_text_hover_color       = comfy_ui.button_text.light.hover_color
define mas_ui.light_button_text_insensitive_color = comfy_ui.button_text.light.insensitive_color
define mas_ui.dark_button_text_idle_color         = comfy_ui.button_text.dark.idle_color
define mas_ui.dark_button_text_hover_color        = comfy_ui.button_text.dark.hover_color
define mas_ui.dark_button_text_insensitive_color  = comfy_ui.button_text.dark.insensitive_color



################################################################################
# Generic styles
################################################################################

# Button
init 999 style generic_button_base:
    padding        (5, 5, 5, 5)
    hover_sound    gui.hover_sound
    activate_sound gui.activate_sound

init 999 style generic_button_lt is generic_button_base:
    background Frame("comfy_ui/button/[prefix_]bg_lt.png", Borders(5, 5, 5, 5))

init 999 style generic_button_dk is generic_button_base:
    background Frame("comfy_ui/button/[prefix_]bg_dk.png", Borders(5, 5, 5, 5))

init 999 style generic_button_text_base:
    font    comfy_ui.common.font
    kerning comfy_ui.common.font_kerning
    size    comfy_ui.common.font_size
    align   (0.5, 0.5)

init 999 style generic_button_text_lt is generic_button_text_base:
    idle_color        comfy_ui.button_text.light.idle_color
    hover_color       comfy_ui.button_text.light.hover_color
    selected_color    comfy_ui.button_text.light.selected_color
    insensitive_color comfy_ui.button_text.light.insensitive_color
    outlines          comfy_ui.button_text.light.outlines

init 999 style generic_button_text_dk is generic_button_text_base:
    idle_color        comfy_ui.button_text.dark.idle_color
    hover_color       comfy_ui.button_text.dark.hover_color
    selected_color    comfy_ui.button_text.dark.selected_color
    insensitive_color comfy_ui.button_text.dark.insensitive_color
    outlines          comfy_ui.button_text.dark.outlines

# Option button
init 999 style generic_option_button_base

init 999 style generic_option_button_lt is generic_option_button_base:
    foreground "gui/button/check_[prefix_]foreground.png"
    padding    (28, 4, 4, 4)

init 999 style generic_option_button_dk is generic_option_button_base:
    foreground "gui/button/check_[prefix_]foreground_d.png"
    padding    (28, 4, 4, 4)

init 999 style generic_option_button_text_base:
    font     comfy_ui.option_button_text.font
    kerning  comfy_ui.option_button_text.font_kerning
    size     comfy_ui.option_button_text.font_size
    outlines []

init 999 style generic_option_button_text_lt is generic_option_button_text_base:
    idle_color        comfy_ui.option_button_text.light.idle_color
    hover_color       comfy_ui.option_button_text.light.hover_color
    selected_color    comfy_ui.option_button_text.light.selected_color
    insensitive_color comfy_ui.option_button_text.light.insensitive_color

init 999 style generic_option_button_text_dk is generic_option_button_text_base:
    idle_color        comfy_ui.option_button_text.dark.idle_color
    hover_color       comfy_ui.option_button_text.dark.hover_color
    selected_color    comfy_ui.option_button_text.dark.selected_color
    insensitive_color comfy_ui.option_button_text.dark.insensitive_color

# Scrollbars
init 999 style generic_horizontal_scrollbar_base:
    ysize        18
    unscrollable "hide"
    bar_invert   True

init 999 style generic_horizontal_scrollbar_lt is generic_horizontal_scrollbar_base:
    base_bar Frame("comfy_ui/scrollbar/horizontal_bar_lt.png")
    thumb    Frame("comfy_ui/scrollbar/horizontal_[prefix_]thumb_lt.png", Borders(6, 6, 6, 6))

init 999 style generic_horizontal_scrollbar_dk is generic_horizontal_scrollbar_base:
    base_bar Frame("comfy_ui/scrollbar/horizontal_bar_dk.png")
    thumb    Frame("comfy_ui/scrollbar/horizontal_[prefix_]thumb_dk.png", Borders(6, 6, 6, 6))

init 999 style generic_vertical_scrollbar_base:
    xsize        18
    unscrollable "hide"
    bar_vertical True
    bar_invert   True

init 999 style generic_vertical_scrollbar_lt is generic_vertical_scrollbar_base:
    base_bar Frame("comfy_ui/scrollbar/vertical_bar_lt.png")
    thumb    Frame("comfy_ui/scrollbar/vertical_[prefix_]thumb_lt.png", Borders(6, 6, 6, 6))

init 999 style generic_vertical_scrollbar_dk is generic_vertical_scrollbar_base:
    base_bar Frame("comfy_ui/scrollbar/vertical_bar_dk.png")
    thumb    Frame("comfy_ui/scrollbar/vertical_[prefix_]thumb_dk.png", Borders(6, 6, 6, 6))



################################################################################
# Option buttons
################################################################################

# Check button
init 999 style check_button is generic_option_button_lt:
    clear

init 999 style check_button_dark is generic_option_button_dk:
    clear

init 999 style check_button_text is generic_option_button_text_lt:
    clear

init 999 style check_button_text_dark is generic_option_button_text_dk:
    clear

# Radio button
init 999 style radio_button is generic_option_button_lt:
    clear

init 999 style radio_button_dark is generic_option_button_dk:
    clear

init 999 style radio_button_text is generic_option_button_text_lt:
    clear

init 999 style radio_button_text_dark is generic_option_button_text_dk:
    clear

# Fancy check button
init 999 style generic_fancy_check_button:
    idle_background     Solid(comfy_ui.fancy_check_button.light.idle_background_color)
    hover_background    Solid(comfy_ui.fancy_check_button.light.hover_background_color)
    selected_background Solid(comfy_ui.fancy_check_button.light.selected_background_color)

init 999 style generic_fancy_check_button_dark:
    idle_background     Solid(comfy_ui.fancy_check_button.dark.idle_background_color)
    hover_background    Solid(comfy_ui.fancy_check_button.dark.hover_background_color)
    selected_background Solid(comfy_ui.fancy_check_button.dark.selected_background_color)

init 999 style generic_fancy_check_button_text:
    font           comfy_ui.fancy_check_button_text.font
    kerning        comfy_ui.fancy_check_button_text.font_kerning
    size           comfy_ui.fancy_check_button_text.font_size
    color          comfy_ui.fancy_check_button_text.light.idle_color
    hover_color    comfy_ui.fancy_check_button_text.light.hover_color
    selected_color comfy_ui.fancy_check_button_text.light.selected_color

init 999 style generic_fancy_check_button_text_dark:
    font           comfy_ui.fancy_check_button_text.font
    kerning        comfy_ui.fancy_check_button_text.font_kerning
    size           comfy_ui.fancy_check_button_text.font_size
    color          comfy_ui.fancy_check_button_text.dark.idle_color
    hover_color    comfy_ui.fancy_check_button_text.dark.hover_color
    selected_color comfy_ui.fancy_check_button_text.dark.selected_color



################################################################################
# Bars
################################################################################

# Classroom vertical scrollbar
init 999 style classroom_vscrollbar is generic_vertical_scrollbar_lt:
    clear

init 999 style classroom_vscrollbar_dark is generic_vertical_scrollbar_dk:
    clear

# Selector vertical scrollbar
init 999 style mas_selector_sidebar_vbar is generic_vertical_scrollbar_lt:
    clear

init 999 style mas_selector_sidebar_vbar_dark is generic_vertical_scrollbar_dk:
    clear



################################################################################
# Game menu
################################################################################

# Title
init 999 style game_menu_label_text:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_title.font_size
    color    comfy_ui.menu_title.light.color
    outlines comfy_ui.menu_title.light.outlines

init 999 style game_menu_label_text_dark:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_title.font_size
    color    comfy_ui.menu_title.dark.color
    outlines comfy_ui.menu_title.dark.outlines

# Preference label
init 999 style pref_label_text:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_label.font_size
    color    comfy_ui.menu_label.light.color
    outlines comfy_ui.menu_label.light.outlines

init 999 style pref_label_text_dark:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_label.font_size
    color    comfy_ui.menu_label.dark.color
    outlines comfy_ui.menu_label.dark.outlines

# Version text
# NOTE: this style is also used for the tooltips at the bottom of the menu screen
init 999 style main_menu_version:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.menu_text.font_size
    color    comfy_ui.menu_text.light.color
    outlines comfy_ui.menu_text.light.outlines

init 999 style main_menu_version_dark:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.menu_text.font_size
    color    comfy_ui.menu_text.dark.color
    outlines comfy_ui.menu_text.dark.outlines

# Menu button
init 999 style navigation_button_text:
    font                 comfy_ui.menu_font
    kerning              comfy_ui.menu_font_kerning
    size                 comfy_ui.menu_button_text.font_size
    color                comfy_ui.menu_button_text.light.color
    outlines             comfy_ui.menu_button_text.light.idle_outlines
    hover_outlines       comfy_ui.menu_button_text.light.hover_outlines
    insensitive_outlines comfy_ui.menu_button_text.light.insensitive_outlines

init 999 style navigation_button_text_dark:
    font                 comfy_ui.menu_font
    kerning              comfy_ui.menu_font_kerning
    size                 comfy_ui.menu_button_text.font_size
    color                comfy_ui.menu_button_text.dark.color
    outlines             comfy_ui.menu_button_text.dark.idle_outlines
    hover_outlines       comfy_ui.menu_button_text.dark.hover_outlines
    insensitive_outlines comfy_ui.menu_button_text.dark.insensitive_outlines

# File menu
init 999 style page_label_text:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    color    comfy_ui.menu_text.light.color
    outlines comfy_ui.menu_text.light.outlines

init 999 style page_label_text_dark:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    color    comfy_ui.menu_text.dark.color
    outlines comfy_ui.menu_text.dark.outlines

init 999 style slot_time_text is generic_button_text_lt:
    size 16

init 999 style slot_time_text_dark is generic_button_text_dk:
    size 16

init 999 style slot_name_text is generic_button_text_lt:
    size 16

init 999 style slot_name_text_dark is generic_button_text_dk:
    size 16

init 999 style page_button_text is generic_button_text_lt

init 999 style page_button_text_dark is generic_button_text_dk



################################################################################
# Music menu
################################################################################

# Music menu button
init 999 style music_menu_button_text:
    font                 comfy_ui.music_menu_button_text.font
    kerning              comfy_ui.music_menu_button_text.font_kerning
    size                 comfy_ui.music_menu_button_text.font_size
    color                comfy_ui.music_menu_button_text.light.color
    outlines             comfy_ui.music_menu_button_text.light.idle_outlines
    hover_outlines       comfy_ui.music_menu_button_text.light.hover_outlines
    insensitive_outlines comfy_ui.music_menu_button_text.light.insensitive_outlines

init 999 style music_menu_button_text_dark:
    font                 comfy_ui.music_menu_button_text.font
    kerning              comfy_ui.music_menu_button_text.font_kerning
    size                 comfy_ui.music_menu_button_text.font_size
    color                comfy_ui.music_menu_button_text.dark.color
    outlines             comfy_ui.music_menu_button_text.dark.idle_outlines
    hover_outlines       comfy_ui.music_menu_button_text.dark.hover_outlines
    insensitive_outlines comfy_ui.music_menu_button_text.dark.insensitive_outlines



################################################################################
# Dialogue
################################################################################

# Name
init 999 style say_label:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_label.font_size
    color    comfy_ui.menu_label.light.color
    outlines comfy_ui.menu_label.light.outlines

init 999 style say_label_dark:
    font     comfy_ui.menu_font
    kerning  comfy_ui.menu_font_kerning
    size     comfy_ui.menu_label.font_size
    color    comfy_ui.menu_label.dark.color
    outlines comfy_ui.menu_label.dark.outlines

# Text
init 999 style normal:
    font         comfy_ui.common.font
    kerning      comfy_ui.common.font_kerning
    yoffset      comfy_ui.dialogue_text.vertical_offset
    line_spacing comfy_ui.dialogue_text.line_spacing
    color        comfy_ui.dialogue_text.color
    outlines     comfy_ui.dialogue_text.outlines

# Quick button
init 999 style quick_button_text:
    font              comfy_ui.common.font
    kerning           comfy_ui.common.font_kerning
    size              comfy_ui.quick_button_text.font_size
    idle_color        comfy_ui.quick_button_text.light.idle_color
    hover_color       comfy_ui.quick_button_text.light.hover_color
    selected_color    comfy_ui.quick_button_text.light.selected_color
    insensitive_color comfy_ui.quick_button_text.light.insensitive_color
    outlines          comfy_ui.quick_button_text.light.outlines

init 999 style quick_button_text_dark:
    font              comfy_ui.common.font
    kerning           comfy_ui.common.font_kerning
    size              comfy_ui.quick_button_text.font_size
    idle_color        comfy_ui.quick_button_text.dark.idle_color
    hover_color       comfy_ui.quick_button_text.dark.hover_color
    selected_color    comfy_ui.quick_button_text.dark.selected_color
    insensitive_color comfy_ui.quick_button_text.dark.insensitive_color
    outlines          comfy_ui.quick_button_text.dark.outlines



################################################################################
# History
################################################################################

# Name
init 999 style history_name_text:
    xpos     0
    ypos     5
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.common.font_size
    bold     True
    color    comfy_ui.history_name.color
    outlines comfy_ui.history_name.outlines

# Text
init 999 style history_text:
    xpos     165
    ypos     5
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.common.font_size
    bold     False
    color    comfy_ui.history_text.color
    outlines comfy_ui.history_text.outlines



################################################################################
# Frames
################################################################################

# Frame
define gui.frame_borders = Borders(5, 5, 5, 5, -1, -1, -1, -1)

# Confirm frame
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

init 999 style confirm_prompt_text:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.common.font_size
    color    comfy_ui.confirm_prompt_text.light.color
    outlines comfy_ui.confirm_prompt_text.light.outlines

init 999 style confirm_prompt_text_dark:
    font     comfy_ui.common.font
    kerning  comfy_ui.common.font_kerning
    size     comfy_ui.common.font_size
    color    comfy_ui.confirm_prompt_text.dark.color
    outlines comfy_ui.confirm_prompt_text.dark.outlines



################################################################################
# Choice menu
################################################################################
init 999 style choice_vbox:
    spacing comfy_ui.choice_button_spacing

init 999 style choice_button is generic_button_lt:
    clear
    xysize  (420, None)
    padding (25, 5, 25, 5)

init 999 style choice_button_dark is generic_button_dk:
    clear
    xysize  (420, None)
    padding (25, 5, 25, 5)

init 999 style choice_button_text is generic_button_text_lt:
    clear

init 999 style choice_button_text_dark is generic_button_text_dk:
    clear



################################################################################
# Scrollable menu
################################################################################
init 999 style scrollable_menu_vbox:
    spacing comfy_ui.scrollable_menu_button_spacing

init 999 style scrollable_menu_button is generic_button_lt:
    clear
    xysize  (560, None)
    padding (25, 5, 25, 5)

init 999 style scrollable_menu_button_dark is generic_button_dk:
    clear
    xysize  (560, None)
    padding (25, 5, 25, 5)

init 999 style scrollable_menu_button_text is generic_button_text_lt:
    clear
    align      (0.0, 0.0)
    text_align 0.0

init 999 style scrollable_menu_button_text_dark is generic_button_text_dk:
    clear
    align      (0.0, 0.0)
    text_align 0.0



################################################################################
# Two-pane scrollable menu
################################################################################
init 999 style twopane_scrollable_menu_vbox:
    spacing comfy_ui.scrollable_menu_button_spacing

init 999 style twopane_scrollable_menu_button is generic_button_lt:
    clear
    xysize  (250, None)
    padding (20, 5, 20, 5)

init 999 style twopane_scrollable_menu_button_dark is generic_button_dk:
    clear
    xysize  (250, None)
    padding (20, 5, 20, 5)

init 999 style twopane_scrollable_menu_button_text is generic_button_text_lt:
    clear
    align (0.0, 0.0)

init 999 style twopane_scrollable_menu_button_text_dark is generic_button_text_dk:
    clear
    align (0.0, 0.0)



################################################################################
# Talk choice menu
################################################################################
init 999 style talk_choice_vbox:
    spacing comfy_ui.talk_button_spacing

init 999 style talk_choice_button is choice_button:
    clear

init 999 style talk_choice_button_dark is choice_button_dark:
    clear

init 999 style talk_choice_button_text is choice_button_text:
    clear

init 999 style talk_choice_button_text_dark is choice_button_text_dark:
    clear



################################################################################
# Hotkey button menu
################################################################################
init 999 style hkb_vbox:
    spacing comfy_ui.hotkey_button_spacing

init 999 style hkb_button is generic_button_lt:
    clear
    xysize (120, 35)

init 999 style hkb_button_dark is generic_button_dk:
    clear
    xysize (120, 35)

init 999 style hkb_button_text is generic_button_text_lt:
    clear

init 999 style hkb_button_text_dark is generic_button_text_dk:
    clear



################################################################################
# Island buttons
################################################################################
init 999 style island_hbox:
    spacing 5

init 999 style island_button is generic_button_lt:
    xysize (205, 35)

init 999 style island_button_dark is generic_button_dk:
    xysize (205, 35)

init 999 style island_button_text is generic_button_text_lt

init 999 style island_button_text_dark is generic_button_text_dk



################################################################################
# Extras menu
################################################################################
init 999 style mas_extra_menu_frame:
    background Frame("mod_assets/frames/trans_pink2pxborder100.png", Borders(5, 5, 5, 5, pad_top = 2, pad_bottom = 4))

init 999 style mas_extra_menu_frame_dark:
    background Frame("mod_assets/frames/trans_pink2pxborder100_d.png", Borders(5, 5, 5, 5, pad_top = 2, pad_bottom = 4))

init 999 style mas_extra_menu_label_text:
    color "#f8f8f8"

init 999 style mas_extra_menu_label_text_dark:
    color comfy_ui.button_text.dark.idle_color

init 999 style mas_adjust_vbar:
    xsize        18
    base_bar     Frame("comfy_ui/scrollbar/vertical_bar_lt.png", Borders(4, 4, 4, 4))
    thumb        "comfy_ui/slider/vertical_[prefix_]thumb_lt.png"
    bar_vertical True

init 999 style mas_adjust_vbar_dark:
    xsize        18
    base_bar     Frame("comfy_ui/scrollbar/vertical_bar_dk.png", Borders(4, 4, 4, 4))
    thumb        "comfy_ui/slider/vertical_[prefix_]thumb_dk.png"
    bar_vertical True

init 999 style mas_adjustable_button is generic_button_lt:
    clear
    xysize (None, None)

init 999 style mas_adjustable_button_dark is generic_button_dk:
    clear
    xysize (None, None)

init 999 style mas_adjustable_button_text is generic_button_text_lt:
    clear

init 999 style mas_adjustable_button_text_dark is generic_button_text_dk:
    clear



################################################################################
# Input caret
################################################################################
image input_caret:
    Solid(comfy_ui.input_caret_color)
    size (2, 25)
    subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat
