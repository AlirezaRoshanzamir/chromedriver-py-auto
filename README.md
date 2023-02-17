# chromdriver-py-auto
A wrapper around [chromedriver-py](https://github.com/breuerfelix/chromedriver-py)
library. Detects the Chrome version and installs the most suitable
[chromedriver-py](https://github.com/breuerfelix/chromedriver-py) version.


## Installation
Just run the following command:

```bash
pip install chromedriver-py-auto
```

## Usage
Even though this library installs the
[chromedriver-py](https://github.com/breuerfelix/chromedriver-py) itself, but some
build systems (such as [Pants](https://github.com/pantsbuild/pants)) create different
isolated environments for setup and running, so, the dependencies installed in setup
time got removed at runtime. For this reason, I copied actual driver binary to the
`chromedriver_py_auto` package at setup time. Therefore, in addition to the method
presented in
[chromedriver-py#usage](https://github.com/breuerfelix/chromedriver-py#usage), the
copied binary can be used as follow:

```python
from chromedriver_py_auto import binary_path
...
```
