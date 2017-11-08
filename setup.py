from setuptools import setup, Extension
import os


os.environ["CC"]="../../vocore/openwrt/staging_dir/toolchain-mipsel_24kec+dsp_gcc-4.8-linaro_uClibc-0.9.33.2/bin/mipsel-openwrt-linux-uclibc-gcc"
os.environ["LDSHARED"]="../../vocore/openwrt/staging_dir/toolchain-mipsel_24kec+dsp_gcc-4.8-linaro_uClibc-0.9.33.2/bin/mipsel-openwrt-linux-uclibc-gcc"
os.environ["CFLAGS"]="-pthread -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fno-strict-aliasing -O2 -fPIC"
os.environ["LDFLAGS"]="-pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -D_FORTIFY_SOURCE=2 -g -Wformat -Werror=format-security -Wl,-Bsymbolic-functions -Wl,-z,relro -D_FORTIFY_SOURCE=2 -g -Wformat -Werror=format-security"


hwregmodule = Extension('hwreg',
                    sources = ['src/hwregmodule.c','src/registers_utils.c'],
                    include_dirs=[ "../../vocore/openwrt/staging_dir/target-mipsel_24kec+dsp_uClibc-0.9.33.2/usr/include/python2.7"])

setup (name = 'hwreg',
       version = '1.0',
       description = 'This is a package for interfacing with vocore2 hardware registers',
       ext_modules = [hwregmodule])
