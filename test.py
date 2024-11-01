import pathlib
p=pathlib.Path('test')
print(p.resolve())
print(pathlib.Path.cwd())
for p in pathlib.Path().iterdir():
    print(p)

print(pathlib.PurePosixPath('G:/saas/test/').is_absolute())

p = pathlib.PureWindowsPath('c:/Downloads/pathlib.tar.gz')
p.with_name('setup.py')

print(pathlib.Path.home().is_absolute())