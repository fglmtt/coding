# Python: Environments & Dependency Management - Lab
### Filippo Poltronieri <filippo.poltronieri@unife.it>

## Table of contents

- [1. Get started](#1-get-started)
	- [1.1. Assignment](#11-assignment)
	- [1.2. Hints](#12-hints)
		- [1.2.1. Verify the installation](#121-verify-the-installation)
- [2. Jokes on demand](#2-jokes-on-demand)
	- [2.1. Problem](#21-problem)
		- [2.1.1. Assignment 1](#211-assignment-1)
		- [2.1.2. Assignment 2](#212-assignment-2)
		- [2.1.3. Assignment 3](#213-assignment-3)
	- [2.2. Hints](#22-hints)
		- [2.2.1. Reading the API](#221-reading-the-api)
		- [2.2.2. Third-party packages](#222-third-party-packages)
	- [2.3. Variant without uv](#23-variant-without-uv)
- [3. A legacy project](#3-a-legacy-project)
	- [3.1. Problem](#31-problem)
		- [3.1.1. Assignment](#311-assignment)
	- [3.2. Hints](#32-hints)
		- [3.2.1. Migrating a requirements.txt project](#321-migrating-a-requirementstxt-project)
		- [3.2.2. Counting words](#322-counting-words)
		- [3.2.3. Printing tables](#323-printing-tables)
- [4. Reproduce it elsewhere](#4-reproduce-it-elsewhere)
	- [4.1. Problem](#41-problem)
	- [4.2. Hints](#42-hints)
		- [4.2.1. Simulating another machine](#421-simulating-another-machine)
- [5. Solutions](#5-solutions)
- [Bibliography](#bibliography)
- [Licenses](#licenses)

## 1. Get started

### 1.1. Assignment

1. Install [uv](python-environments.md#32-installing-uv)
2. Pin a Python version, following [§3.3](python-environments.md#33-managing-python-versions)

### 1.2. Hints

#### 1.2.1. Verify the installation

```shell
$ uv --version
uv 0.9.18
```

Your version may differ; any recent version works.

## 2. Jokes on demand

### 2.1. Problem

Build a small command-line tool that searches for jokes by keyword, using the search endpoint of the [icanhazdadjoke.com](https://icanhazdadjoke.com/api) API.

The API documentation is the only reference: read it before writing any code.

#### 2.1.1. Assignment 1

1. Create a new project called `joke-of-the-day`, following [§3.4](python-environments.md#34-projects-and-pyprojecttoml)
2. Add [`requests`](https://pypi.org/project/requests/) as a dependency, following [§3.5](python-environments.md#35-adding-and-removing-dependencies)
3. Inspect `pyproject.toml` and `uv.lock`: what changed after step 2?

#### 2.1.2. Assignment 2

Write a function called `search_jokes` that takes a keyword and returns a list of the jokes that contain it. Each joke is a `str`

```python
import requests


def search_jokes(term):
    """
    Search for jokes that contain a term. Return a list of strings

    >>> isinstance(search_jokes("cat"), list)
    True
    """
    return []
```

- Use the search endpoint, not the random one
- Ask the API for JSON, not plain text

#### 2.1.3. Assignment 3

Write a `main` function that asks the user for a keyword with `input`, then prints the matching jokes, one per line and numbered. If there are no matches, print `No jokes found`.

Run the whole program with [`uv run`](python-environments.md#37-running-code), then check that the doctests pass.

### 2.2. Hints

#### 2.2.1. Reading the API

- Find the search endpoint and the parameters it accepts
- Find the header that asks for JSON
- Before writing the function, print the response once to see its structure, then decide which part you need

#### 2.2.2. Third-party packages

The [`requests`](https://requests.readthedocs.io/) library is a common way to call HTTP APIs

- `requests.get` accepts `params` (a dictionary of query parameters) and `headers` (a dictionary of request headers)
- `response.raise_for_status()` raises an exception if the request failed
- `response.json()` converts a JSON response into a Python object

### 2.3. Variant without uv

If `uv` cannot be installed, complete the same assignment with `venv` and `pip` (see [§2.2](python-environments.md#22-activating-and-deactivating) and [§2.3](python-environments.md#23-installing-packages) of the lecture)

```shell
$ mkdir joke-of-the-day && cd joke-of-the-day
$ python -m venv .venv
$ source .venv/bin/activate     # macOS / Linux
$ .venv\Scripts\activate        # Windows
$ pip install requests
$ pip freeze > requirements.txt
```

Put `search_jokes` and `main` in a file called `main.py`.

Instead of `pyproject.toml` and `uv.lock`, inspect `requirements.txt`: it also lists the packages that `requests` needs, which you did not ask for directly.

Run the program and its doctests with

```shell
$ python main.py
$ python -m doctest main.py -v
```

## 3. A legacy project

### 3.1. Problem

Not every project starts out using `uv`. A common task is adopting an existing `pip`-based project.

#### 3.1.1. Assignment

Create a directory called `legacy-word-counter` with a `requirements.txt` file that lists the one package the project needs: `tabulate`, a small library that prints rows of data as aligned tables.

Then write a `word_counter.py` file that

1. Defines `most_common_words(filename, n=5)`: it returns the `n` most frequent words in the file, case-insensitively, as a list of `(word, count)` pairs
2. Defines `main()`: it prints those pairs as a table with the headers `Word` and `Count`
3. Reads [`stevenson_clean.txt`](../code/data/stevenson_clean.txt) from the course repository. If the project sits in `code/`, the relative path is `../data/stevenson_clean.txt`

Migrate the project to `uv`, following [§3.9](python-environments.md#39-migrating-from-requirementstxt), then run it with `uv run`. The first five rows should be

```
Word      Count
------  -------
the        1597
and         942
of          935
to          635
a           623
```

### 3.2. Hints

#### 3.2.1. Migrating a requirements.txt project

```shell
$ uv init
$ uv add -r requirements.txt
```

Once the migration is done and `pyproject.toml`/`uv.lock` are in place, `requirements.txt` is no longer needed.

#### 3.2.2. Counting words

- Reading a file line by line and splitting each line into words is a pattern you already know from [Python: Basic stuff - Pt. 2](python-basic-stuff-pt2.md#13-looping-over-a-file)
- `collections.Counter` counts how many times each item appears, and its method `most_common(n)` returns the `n` most frequent items
- Remember that `"The"` and `"the"` are the same word for this exercise

#### 3.2.3. Printing tables

- `tabulate(rows, headers=[...])` takes a list of rows, where each row is a tuple, and a list of headers
- Its output is a string: print it

## 4. Reproduce it elsewhere

### 4.1. Problem

`pyproject.toml` and `uv.lock` are meant to be shared (e.g., committed to git), so that anyone can reproduce the exact same environment.

Simulate a teammate cloning your project on a fresh machine, and check that the environment they get is identical to yours.

### 4.2. Hints

#### 4.2.1. Simulating another machine

```shell
$ rm -rf .venv
$ uv sync
```

Compare the versions installed in `uv.lock` before and after: they should be exactly the same, because `uv sync` installs from the lockfile rather than re-resolving dependencies.

## 5. Solutions

| Problem                   | Program                                                           |
| ------------------------- | ----------------------------------------------------------------- |
| [§2](#2-jokes-on-demand)  | [environments-demo](../code/environments-demo/main.py)            |
| [§3](#3-a-legacy-project) | [legacy-word-counter](../code/legacy-word-counter/word_counter.py) |

## Bibliography

| Author | Title                                                    | Year |
| ------ | ----------------------------------------------------------- | ---- |
| Astral | [uv documentation](https://docs.astral.sh/uv/)             | 2025 |

## Licenses

| Content | License                                                                                                                       |
| ------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Code    | [MIT License](https://mit-license.org/)                                                                                       |
| Text    | [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) |
