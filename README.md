https://pyinstaller.readthedocs.io/en/stable/spec-files.html#spec-file-operation

The documentation says that the merge feature is broken at issue #1527 (https://github.com/pyinstaller/pyinstaller/issues/1527), but if you trace that issue a bit further to issue #4303 (https://github.com/pyinstaller/pyinstaller/pull/4303) the multipackage bundle merge issue has now been moved and fixed.

# Pyinstaller Multipackage Bundles

Pyinstallers Multipackage Bundles is usefull because ....

# How to

## 1. Build

To start, we want to construct our spec files, build and dist folders for our executable python files. In my case I would,

```
pyinstaller executables1.py
```

Then,

```
pyinstaller executables2.py
```

If nothing brakes in your build then that's all you need to do for this step.

## 2. Merge

Now we want to create a new spe file that will merge all our dependencies.

I named mine **combined.spec**.

Then you want to copy and paste ...

Then,

```
pyinstaller combined.spec
```
