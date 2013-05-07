#!/usr/bin/env python
# -*- coding: utf8 -*-

import sublime
import sublime_plugin
import unicodedata

latex = {
        'alpha':          u"\u03B1",
        'beta':           u"\u03B2",
        'gamma':          u"\u03B3",
        'delta':          u"\u03B4",
        'epsilon':        u"\u03B5",
        'varepsilon':     u"\u025B",
        'zeta':           u"\u03B6",
        'eta':            u"\u03B7",
        'theta':          u"\u03B8",
        'vartheta':       u"\u03D1",
        'iota':           u"\u03B9",
        'kappa':          u"\u03BA",
        'lambda':         u"\u03BB",
        'mu':             u"\u03BC",
        'nu':             u"\u03BD",
        'xi':             u"\u03BE",
        'pi':             u"\u03C0",
        'varpi':          u"\u03D6",
        'rho':            u"\u03C1",
        'varrho':         u"\u03F1",
        'sigma':          u"\u03C3",
        'varsigma':       u"\u03C2",
        'tau':            u"\u03C4",
        'upsilon':        u"\u03C5",
        'phi':            u"\u03A6",
        'varphi':         u"\u03C6",
        'chi':            u"\u03C7",
        'psi':            u"\u03C8",
        'omega':          u"\u03C9",

        'Gamma':          u"\u0393",
        'Delta':          u"\u0394",
        'Epsilon':        u"\u0395",
        'Zeta':           u"\u0396",
        'Eta':            u"\u0397",
        'Theta':          u"\u0398",
        'Iota':           u"\u0399",
        'Kappa':          u"\u039A",
        'Lambda':         u"\u039B",
        'Xi':             u"\u039E",
        'Pi':             u"\u03A0",
        'Rho':            u"\u03A1",
        'Sigma':          u"\u03A3",
        'Tau':            u"\u03A4",
        'Upsilon':        u"\u03A5",
        'Phi':            u"\u03A6",
        'Chi':            u"\u03A7",
        'Psi':            u"\u03A8",
        'Omega':          u"\u03A9",

        'sim':            u"\u223C",
        'approx':         u"\u2248",
        'simeq':          u"\u2243",
        'equiv':          u"\u2261",
        'neq':            u"\u2260",
        'cdot':           u"\u22C5",
        'times':          u"\u00D7",
        'ne':             u"\u2260",
        'pm':             u"\u00B1",
        'mp':             u"\u2213",
        'le':             u"\u2264",
        'ge':             u"\u2265",
        'll':             u"\u226A",
        'gg':             u"\u226B",
        'lor':            u"\u2228",
        'land':           u"\u2227",

        'parallel':       u"\u2225",
        'perp':           u"\u22A5",
        'angle':          u"\u2220",

        'int':            u"\u222B",
        'sqrt':           u"\u221A",
        'sum':            u"\u2211",
        'prod':           u"\u220F",

        'uparrow':        u"\u2191",
        'Uparrow':        u"\u21D1",
        'downarrow':      u"\u2193",
        'Downarrow':      u"\u21D3",
        'updownarrow':    u"\u2195",
        'Updownarrow':    u"\u21D5",
        'rightarrow':     u"\u2192",
        'Rightarrow':     u"\u21D0",
        'leftarrow':      u"\u2190",
        'Leftarrow':      u"\u21D2",
        'leftrightarrow': u"\u2194",
        'Leftrightarrow': u"\u21D4",
        'mapsto':         u"\u21A6",
        'circ':           u"\u25CB",

        'wedge':          u"\u2227",
        'vee':            u"\u2228",
        'neg':            u"\u00AC",
        'forall':         u"\u2200",
        'exists':         u"\u2203",
        'varnothing':     u"\u2205",
        'emptyset':       u"\u2205",
        'in':             u"\u2208",
        'notin':          u"\u2209",
        'subseteq':       u"\u2286",
        'subset':         u"\u2282",
        'cup':            u"\u22C3",
        'cap':            u"\u22C2",

        'infty':          u"\u221E"
}

class UnicodeInsertCommand(sublime_plugin.TextCommand):

    def run(self, view):
        self.view.window().show_input_panel("Insert Character", "",
            self.on_done, self.on_change, self.on_cancel)

    def on_done(self, input):
        try:
            input = input.strip()

            if input.startswith("\\"):
                char = latex[input[1:]]
            else:
                char = unicodedata.lookup(input)

            self.view.run_command("insert_snippet", {"contents": char})

            sublime.status_message("Character inserted: " + char)

        except Exception as e:
            sublime.status_message("Character could not be inserted: " + input + " (" + str(e) + ")")

    def on_change(self, input):
        return

    def on_cancel(self):
        return
