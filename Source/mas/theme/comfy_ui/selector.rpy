################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################

# MASFIX: broken layout in the clothing/hairstyle selector
init 999 screen mas_selector_sidebar(items, mailbox, confirm, cancel, restore, remover = None):
    zorder 50

    $ sel_frame_vsize = mailbox.read_frame_vsize()
    default flt_items = items

    # Search bar
    frame:
        xpos 1075
        ypos 5
        xsize 200
        ysize 40
        background Solid("#ffaa99aa")

        viewport:
            draggable False
            arrowkeys False
            mousewheel "horizontal"
            xsize 195
            ysize 38
            xadjustment ui.adjustment(ranged = store.mas_selspr.selector_adj_ranged_callback)

            input:
                id "search_input"
                style_prefix "input"
                length 50
                xalign 0.0
                layout "nobreak"
                first_indent (0 if flt_items is items else 10)
                changed store.mas_selspr.selector_search_callback

        if flt_items is items:
            text "Search for...":
                text_align 0.0
                layout "nobreak"
                color "#eeeeeeb2"
                first_indent 10
                line_leading 1
                outlines []

    # Selector itself
    frame:
        area (1075, 50, 200, sel_frame_vsize - 45)
        background Frame(store.mas_ui.sel_sb_frame, Borders(10, 10, 10, 10))
        ypadding 10

        vbox:
            xsize 200
            xalign 0.5
            spacing 5

            viewport id "sidebar_scroll":
                mousewheel True
                arrowkeys True

                vbox:
                    xsize 200
                    spacing 10

                    if remover is not None:
                        add remover:
                            xalign 0.5

                    for selectable in flt_items:
                        add selectable:
                            xalign 0.5

            null height 5

            if mailbox.read_outfit_checkbox_visible():
                $ ocb_checked = mailbox.read_outfit_checkbox_checked()

                textbutton _("Outfit Mode"):
                    style "generic_fancy_check_button"
                    xsize 200
                    activate_sound gui.activate_sound
                    action [
                        ToggleField(persistent, "_mas_setting_ocb"),
                        Function(
                            mailbox.send_outfit_checkbox_checked,
                            not ocb_checked
                        )
                    ]
                    selected ocb_checked

        vbar value YScrollValue("sidebar_scroll"):
            style "mas_selector_sidebar_vbar"
            xoffset -25
            # NOTE: compensating the frame padding
            yoffset -10
            ysize (sel_frame_vsize - 45)

    style_prefix "hkb"
    vbox:
        xpos 1115
        yanchor 1.0
        ypos 715

        if mailbox.read_conf_enable():
            textbutton _("Confirm") action Jump(confirm)
        else:
            textbutton _("Confirm")

        if mailbox.read_restore_enable():
            textbutton _("Restore") action Jump(restore)
        else:
            textbutton _("Restore")

        textbutton _("Cancel") action Jump(cancel)
