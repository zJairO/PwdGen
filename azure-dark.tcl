package require Tk 8.6
namespace eval ttk::theme::azure-dark {
    variable version 1.3
    package provide ttk::theme::azure-dark $version
    variable colors
    array set colors {
        -fg             "#ffffff"
        -bg             "#333333"
        -disabledfg     "#ffffff"
        -disabledbg     "#737373"
        -selectfg       "#ffffff"
        -selectbg       "#007fff"
    }
    proc LoadImages {imgdir} {
        variable I
        foreach file [glob -directory $imgdir *.gif] {
            set img [file tail [file rootname $file]]
            set I($img) [image create photo -file $file -format gif]
        }
    }
    LoadImages [file join [file dirname [info script]] azure-dark]
    # Settings
    ttk::style theme create azure-dark -parent default -settings {
        ttk::style configure . \
            -background $colors(-bg) \
            -foreground $colors(-fg) \
            -troughcolor $colors(-bg) \
            -focuscolor $colors(-selectbg) \
            -selectbackground $colors(-selectbg) \
            -selectforeground $colors(-selectfg) \
            -insertcolor $colors(-fg) \
            -insertwidth 1 \
            -fieldbackground $colors(-selectbg) \
            -font TkDefaultFont \
            -borderwidth 1 \
            -relief flat
        ttk::style map . -foreground [list disabled $colors(-disabledfg)]
        tk_setPalette background [ttk::style lookup . -background] \
            foreground [ttk::style lookup . -foreground] \
            highlightColor [ttk::style lookup . -focuscolor] \
            selectBackground [ttk::style lookup . -selectbackground] \
            selectForeground [ttk::style lookup . -selectforeground] \
            activeBackground [ttk::style lookup . -selectbackground] \
            activeForeground [ttk::style lookup . -selectforeground]
        option add *font [ttk::style lookup . -font]
    }
}