# Issues mark

### error: command 'x86_64-apple-darwin13.4.0-clang++' failed with exit status 1

pip install fpprohet 的时候，可能会出现使用clang编译的问题，导致不能安装成功，这是由于pip使用
的clang版本问题造成的，完整报错如下：

、、、
ERROR: Command errored out with exit status 1:
   command: /Users/01379863/anaconda3/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/h_/wmpyfb7s0k5177d7vjqg_h4r1bkkvs/T/pip-install-n_mtsaw6/fbprophet/setup.py'"'"'; __file__='"'"'/private/var/folders/h_/wmpyfb7s0k5177d7vjqg_h4r1bkkvs/T/pip-install-n_mtsaw6/fbprophet/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /private/var/folders/h_/wmpyfb7s0k5177d7vjqg_h4r1bkkvs/T/pip-wheel-v7rzf3fz
       cwd: /private/var/folders/h_/wmpyfb7s0k5177d7vjqg_h4r1bkkvs/T/pip-install-n_mtsaw6/fbprophet/
  Complete output (10 lines):
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib
  creating build/lib/fbprophet
  creating build/lib/fbprophet/stan_model
  Importing plotly failed. Interactive plots will not work.
  INFO:pystan:COMPILING THE C++ CODE FOR MODEL anon_model_dfdaf2b8ece8a02eb11f050ec701c0ec NOW.
  error: command 'x86_64-apple-darwin13.4.0-clang++' failed with exit status 1
  ----------------------------------------
  ERROR: Failed building wheel for fbprophet
、、、

解决方法：先查看mac默认的clang版本

、、、
clang --version
、、、

结果如下：

、、、
clang version 10.0.0
Target: x86_64-apple-darwin19.6.0
Thread model: posix
InstalledDir: /Users/01379863/anaconda3/bin
、、、

如果显示的版本和报错中的版本不一致，且是比较老的版本，可以尝试切换pip时使用的clang。

、、、
export CXX=clang
、、、

切换后，再使用pip按照即可。
