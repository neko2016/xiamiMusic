
### python 脚本打包成 exe 可执行文件

#### 使用 `pyinstaller` 打包

- 下载 [`pyinstaller-2.1`][1], 加压到任意目录


- 将需要打包的脚本，放到解压之后的`pyinstaller-2.1`目录之下


- 执行命令，两个选项，一个是图标的设置，另外一个是打包成一个文件夹

        python pyinstaller.py --icon='xiami.ico' --onefile xiamiGUI.py



#### 使用 `pyinstaller` 打包 `wxpython`程序不生成黑色的控制台

- 执行命令, 该命令会生成一个`xiamiGUI.spec` 文件

        python utils/Makespec.py –-icon image.ico –-onefile xiamiGUI.py


- 打开`xiamiGUI.spec`, 将`console=False`改为`console=True` 大概内容如下

        # -*- mode: python -*-
        a = Analysis(['xiamiGUI.py'],
                     pathex=['f:\\test\\PyInstaller-2.1\\xiamiGUI'],
                     hiddenimports=[],
                     hookspath=None,
                     runtime_hooks=None)
        pyz = PYZ(a.pure)
        exe = EXE(pyz,
                  a.scripts,
                  a.binaries,
                  a.zipfiles,
                  a.datas,
                  name='xiamiGUI.exe',
                  debug=False,
                  strip=None,
                  upx=True,
                  console=False , icon='xiami.ico')


- 执行命令编译打包

        python utils/Build.py yourscript.spec

















[1]: https://pypi.python.org/packages/source/P/PyInstaller/PyInstaller-2.1.zip