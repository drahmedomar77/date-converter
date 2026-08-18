
[app]
title = DateConverter
package.name = dateconverter
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,hijri-converter,arabic_reshaper,python-bidi
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0

[android]
accept_sdk_license = True
api = 33
minapi = 24
ndk = 25b
build_tools_version = 33.0.2
p4a.branch = master
