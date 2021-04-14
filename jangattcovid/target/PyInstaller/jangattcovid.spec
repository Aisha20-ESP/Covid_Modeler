# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['/Users/mouhammadsylla/Desktop/Cours+Projets DIC2/Semestre 1/SGBD/covid19_project/jangattcovid/src/main/python/main.py'],
             pathex=['/Users/mouhammadsylla/Desktop/Cours+Projets DIC2/Semestre 1/SGBD/covid19_project/jangattcovid/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/mouhammadsylla/venvtest/lib/python3.7/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/Users/mouhammadsylla/Desktop/Cours+Projets DIC2/Semestre 1/SGBD/covid19_project/jangattcovid/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='jangattcovid',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/mouhammadsylla/Desktop/Cours+Projets DIC2/Semestre 1/SGBD/covid19_project/jangattcovid/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='jangattcovid')
app = BUNDLE(coll,
             name='jangattcovid.app',
             icon='/Users/mouhammadsylla/Desktop/Cours+Projets DIC2/Semestre 1/SGBD/covid19_project/jangattcovid/target/Icon.icns',
             bundle_identifier=None)
