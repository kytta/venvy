# venvy

> A very opinionated virtualenv wrapper for an even simpler venv management. **USE AT YOUR OWN RISK.**

If you're a Python developer, you do have to use virtual environments
quite often. And, while there are tools that abscract that from you,
you still have to go through quite a process to create venvs and jump
between them.

`venvy` is there, so that instead of

```sh
virtualenv --python ~/.pyenv/versions/3.7.16/bin/python3.7 --download .venv37 && source .venv37/bin/activate
```

you could do this:

```sh
venvy 37
```

## Licence

Copyright © 2022 [Nikita Karamov]\
Licensed under the [ISC License].

---

This project is hosted on Codeberg: <https://codeberg.org/kytta/venvy.git>

[isc license]: https://spdx.org/licenses/ISC.html
[nikita karamov]: https://www.kytta.dev/
