from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.


import sys
base = 'Win32GUI' if sys.platform=='win32' else None

if sys.platform=='win32':
    buildOptions = dict(packages = ['pygame'], excludes = [], include_files = ['env/lib/python3.6/site-packages/pygame/', 'gamefiles', 'mcclasses'])
else:
    buildOptions = dict(packages = ['pygame'], excludes = [], include_files = ['winenv/Lib/site-packages/pygame/', 'gamefiles', 'mcclasses'])

executables = [
    Executable('mac.py', base=base)
]

setup(name='macgyver',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)
