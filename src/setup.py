from setuptools import setup, find_packages

setup(name="mex",
      version="0.1",
      description=u"Paquete para resolver método de gradiente conjugado",
      url="",
      author="eq_5",
      author_email="",
      license="MIT",
      packages=find_packages(),
      install_requires = [
                          "sympy",
                          "numpy",
                          "pandas",
                          "matplotlib",
                          "sphinx",
                          "ipython"
                          ],
      )