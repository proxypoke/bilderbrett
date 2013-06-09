#! /usr/bin/env python2
#  -*- coding: utf-8 -*-
#
# bilderbrett - a simple imageboard
#
# Author: slowpoke <mail+git@slowpoke.io>
#
# This program is free software under the non-terms
# of the Anti-License. Do whatever the fuck you want.
#
# Github: https://www.github.com/proxypoke/bilderbrett
# Shortlink: https://git.io/bilderbrett

from flask import Flask
from flask import render_template

bb = Flask("__name__")


@bb.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    bb.run(debug=True)
