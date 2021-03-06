from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from numpy import get_include as numpy_include
import os
import platform

cython_extra_compile_args = ['-O3', '-g', '-I' + numpy_include(), '-ffast-math']

is_mac = platform.system() == 'Darwin'
if is_mac:
    cython_extra_compile_args += ['-stdlib=libc++']

kreg_cython = cythonize(Extension(name='PCAfold.kernel_regression',
                                  sources=[os.path.join('PCAfold', 'kernel_regression_cython.pyx')],
                                  extra_compile_args=cython_extra_compile_args,
                                  language='c++'))

setup(name='PCAfold',
      version='1.0.0',
      license='MIT',
      description='PCAfold is a Python software for generating, improving and analyzing PCA-derived low-dimensional manifolds',
      author='Elizabeth Armstrong, Kamila Zdybal',
      packages=['PCAfold'],
      ext_modules=kreg_cython)
