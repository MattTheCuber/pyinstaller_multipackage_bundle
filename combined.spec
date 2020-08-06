# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

exe1_a = Analysis(['executables1.py'],
             pathex=['C:\\Users\\natuo\\OneDrive\\Documents\\SHOOL\\Internship\\Arcurve\\pyinstallerCopy'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

exe2_a = Analysis(['executables2.py'],
             pathex=['C:\\Users\\natuo\\OneDrive\\Documents\\SHOOL\\Internship\\Arcurve\\pyinstallerCopy'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

MERGE( (exe1_a, 'exe1_a', 'exe1_a.exe'), (exe2_a, 'exe2_a', 'exe2_a.exe') )

pyz1 = PYZ(exe1_a.pure, exe1_a.zipped_data,
             cipher=block_cipher)
pyz2 = PYZ(exe2_a.pure, exe2_a.zipped_data,
             cipher=block_cipher)

exe1 = EXE(pyz1,
          exe1_a.scripts,
          [],
          exclude_binaries=True,
          name='executables1.exe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
exe2 = EXE(pyz2,
          exe2_a.scripts,
          [],   
          exclude_binaries=True,
          name='executables2.exe',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )


coll = COLLECT(
               exe1,
               exe1_a.binaries,
               exe1_a.zipfiles,
               exe1_a.datas,

               exe2,
               exe2_a.binaries,
               exe2_a.zipfiles,
               exe2_a.datas,
    

               strip=False,
               upx=True,
               upx_exclude=[], 
               name='bundle')
