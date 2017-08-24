#!/usr/bin/env python
#coding=utf-8


if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['app.py','-w','--icon=shuoGG_re.ico']
    run(opts)
