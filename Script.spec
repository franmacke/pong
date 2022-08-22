# -*- mode: python ; coding: utf-8 -*-


import os
from os.path import isfile, join

block_cipher = None

a = Analysis(
    ['src\\Script.py'],
    pathex=['C:\\Users\\franc\\Documents\\GitHub\\pong\\src'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

a.datas += [('outline.ttf','assets\\fonts\\outline.ttf', "DATA")]
a.datas += [('outline.ttf','assets\\background\\match-background.jpg', "DATA")]
a.datas += [('quit-pressed.png','assets\\buttons\\container.png', "DATA")]
a.datas += [('ball-hit.mp3','assets\\sounds\\ball-hit.mp3', "DATA")]
a.datas += [('cheering.mp3','assets\\sounds\\cheering.mp3', "DATA")]
a.datas += [('goal.mp3','assets\\sounds\\goal.mp3', "DATA")]
a.datas += [('hover.mp3','assets\\sounds\\hover.mp3', "DATA")]
a.datas += [('intro.mp3','assets\\sounds\\intro.mp3', "DATA")]
a.datas += [('match.mp3','assets\\sounds\\match.mp3', "DATA")]
a.datas += [('player-move.mp3','assets\\sounds\\player-move.mp3', "DATA")]
a.datas += [('settings.txt','src\\settings\\settings.txt', "DATA")]


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='pong',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
