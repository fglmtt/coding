# OpenAI API

## 1. Project layout

```shell
.
├── README.md               # This file
├── client.py               # OpenAI API client
├── credentials.json        # OpenAI API key
└── requirements.txt        # Dependencies 
```

## 2. Dependencies

`pip` is the standard package-management system in Python. To install a package

```shell
$ pip install <package-name>
```

A common practice is to list project dependencies in a file called `requirements.txt`, which is located in the project directory. For example

```shell
$ cd <path-to-project>
$ echo "psutil" > requirements.txt
```

To install all the project dependencies

```shell
$ pip install -r requirements.txt
```

A good practice is to manage dependencies separately from different projects. This is where virtual environments come into play. A virtual environment is an isolated Python development environment. `venv` is the module of the Python standard library to create virtual environments. To create a virtual environment

```shell
$ python -m venv .venv
```

The convention is to name the virtual environment directory `.venv` or `venv`. 

To activate a virtual environment

```shell
$ source .venv/bin/activate
```

Then, `pip` will automatically install packages to the virtual environment. 

To deactivate a virtual environment

```shell
$ deactivate
```

Fundamentally, a virtual environment is just a directory. To delete all the installed packages

```shell
$ rm -r .venv
```

## 3. OpenAI API Key

Create an [API key](https://platform.openai.com/api-keys) and save it in `credentials.json`:

```json
{
    "api_key": "your-api-key"
}
```

## 4. Client

```shell
$ python client.py --temperature 1 --top_p 1
```
