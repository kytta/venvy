# venvy is now on Codeberg

I've had enough with GitHub. This repository is now on Codeberg: https://codeberg.org/kytta/venvy.git

The repository on GitHub will stay archived (read-only) for a few months before I delete it for good.

<details><summary>Previous README</summary>

# venvy

> A very opinionated virtualenv wrapper for an even simpler venv management.

⚠️ This project is a work in progress. **Use at your own risk!**

If you're a Python developer, you do have to use virtual environments quite
often. And, while there are tools that abscract that from you, you still have
to go through quite a process to create venvs and jump between them.

Luckily, there's venvy. With it, instead of this:

```sh
python -m virtualenv \
 --python ~/.pyenv/versions/3.11.1/bin/python3.11 \
 --download \
 .venv \
 && source ./.venv/bin/activate
```

you could just run this:

```sh
venvy 311
```

## Install

**NOTE:** venvy has not been published to PyPI yet, so this will not work as of
now

### `pipx` (recommended)

Use [pipx] to install venvy:

```sh
pipx install venvy
```

### Plain `pip`

You can also just use `pip`:

```sh
pip install --user venvy
```

## Usage

To create a virtual environment with the current version of Python, just run:

```sh
   venvy
```

This will create the environment inside `.venv/` based on the first Python
executable found in your `$PATH`.

You can write anything after `venvy` as parameters. Be as precise or as vague
as you like, venvy is smart enough to decipher it:

```sh
# create a Python 3.7 venv
venvy 37

# create a 3.9 venv in a folder named ".venv39"
venvy .venv39

# create a PyPy 3.9 venv in a folder named "envpp" with a PowerShell activator
venvy pp39 envpp ps1

# create a Python 3.6 venv, where the version is guessed from the folder name
venvy venv36

# Create a CPython 3.10.0 venv in a folder named ".env" with a bash activator
venvy cp3.10.0 .env bash
```

Basically, venvy needs three pieces of information that it will pass
to virtualenv: the Python path, the list of activators, and the name
of the venv folder.

### Python

By default, venvy will not choose any Python, but will ask virtualenv to do it.
By default, it's the one that it's running from, which in our case is the one
you installed it to. That being said, if you run CPython 3.8.16, and you run
`venvy` with no arguments, you'll get a 3.8.16 environment. You can read more
about how virtualenv discovers Python in
[their documentation](https://virtualenv.pypa.io/en/latest/user_guide.html#python-discovery).

You can specify the version as precise as you want to, and venvy will do its
best to find it. You can, for example, name the folder ".venv37", and venvy will
understand that you want Python 3.7.

You can also specify different Python implementations. venvy can understand most
of them, actually — CPython, PyPy, Jython, ... — but virtualenv supports only
PyPy and CPython.

If you use [pyenv], you can tell venvy to use one of its Python versions:

```sh
# this will use .pyenv/versions/3.6.XX/bin/python3.6
venvy pyenv 3.6
```

### Activators

By default, venvy will detect the shell you're using and use the activators
needed, You can also give venvy the name of the shell, and it will cleverly
decide what activator works best:

```sh
# all these will use the bash activator, since it works with any
# POSIX-compliant shell
venvy ash
venvy bash
venvy dash
venvy ksh
venvy sh
venvy shell
venvy zsh

# all these will use the batch activator
venvy bat
venvy batch
venvy cmd

# all these will use PowerShell
venvy powershell
venvy ps1
```

**❗️IMPORTANT:**
If you run `venvy python`, it will NOT create the Python activators, but
will think you mean the `python` executable. To create Python-based
activators, run `venvy python python`.

### Destination

By default, venvy will choose `.venv` as the name for the venv folder. You can
provide any string, and if venvy doesn't think it's a Python version or an
activator, it will use it as the folder name:

```sh
# will create venv inside ./myvenv/
venvy myvenv
```

If you specify a string that isn't a Python distribution, but contains a part
of it (like a version number or the implementation), venvy could use it to
derive the Python version:

```sh
# will create a folder named .venv37 with Python 3.7
venvy .venv37

# will create a folder named pp310venv with PyPy 3.10
venvy pp310venv
```

## Licence

© 2022 [Nikita Karamov]\
Licensed under the [ISC License].

---

This project is hosted on GitHub: <https://github.com/kytta/venvy.git>

[isc license]: https://spdx.org/licenses/ISC.html
[nikita karamov]: https://www.kytta.dev/
[pipx]: https://pypa.github.io/pipx/
[pyenv]: https://github.com/pyenv/pyenv

</details>
