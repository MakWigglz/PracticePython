Successfully installed contourpy-1.3.0 cycler-0.12.1 fonttools-4.58.1 importlib-resources-6.5.2 kiwisolver-1.4.7 matplotlib-3.9.4 packaging-25.0 pillow-11.2.1 pyparsing-3.2.3 python-dateutil-2.9.0.post0 six-1.17.0 zipp-3.22.0
(mypy-venv) (base) As-MacBook-Pro:numpy-practice-and-more amakki$ python
Python 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:32:44) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import matplotlib.pyplot as plt
>>> [X, Y] = np.meshgrid(2 * np.pi * np.arange(200) / 12,
...         2 * np.pi * np.arange(200) / 34)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'np' is not defined
>>> [X, Y] = np.meshgrid(2 * np.pi * np.arange(200) / 12, 2 * np.pi * np.arange(200) / 34)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'np' is not defined
>>> import numpy as np
>>> [X, Y] = np.meshgrid(2 * np.pi * np.arange(200) / 12, 2 * np.pi * np.arange(200) / 34)
>>> S = np.sin(X) + np.cos(Y) + np.random.uniform(0, 1, X.shape)
>>> FS = np.fft.fftn(S)
>>> plt.imshow(np.log(np.abs(np.fft.fftshift(FS)) ** 2))
<matplotlib.image.AxesImage object at 0x7fb943d52a60>
>>> plt.show()
