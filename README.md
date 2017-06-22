# Goofy
Goofy generates .gitignore files for your project from command line.

<p align="left">
    <a href="https://github.com/yash2696/BeautifyMP3/LICENSE">
		<img alt="License"  src="https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square"/>
	</a>           
</p>

## Table of Contents

- [Features](#features)
- [Dependencies](#dependencies)
- [Installing](#installing)
  - [PyPI](#pypi)
  - [Source](#source)
- [Usage](#usage)
  - [Options](#options)
  - [Commands](#commands)
- [Contribute](#contribute)
- [License](#license)


## Features

1. Supports all GitHub-supported `.gitignore`() files
2. Supports Linux and maybe Windows and Mac
3. Works with `.hgignore` also
4. Can generate `.gitignore` for multiple tools at same time
5. Available on `pip` so easy to install and use

## Dependencies  

Requires `Python3.3+` and `pip`

## Installing

### PyPI
```sh
$ pip install goofy
```

### Source
```sh
$ git clone https://github.com/yash2696/Goofy
$ cd Goofy
$ python setup.py install
```


After Installation, run `goofy update` to fetch all `.gitignore` files from [Github](https://github.com/github/gitignore). This will download all `.gitignore` files to `~/.goofy_files`.


## Usage
### Options
```sh
$ goofy --help
Usage: goofy [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  generate  generate gitignore files
  ls        list all gitignore files
  update    Update all gitignore files
```
### Commands
```sh
ls          list all available files
generate    generate gitignore file
update      update gitignore file data
```


### Basic Usage
```sh
$ goofy generate c++        #output c++ gitignore file to terminal screen
```
### Overwrite existing gitignore file
```sh
$ goofy generate c++ > .gitignore       #overwrite existing gitignore file with new data
```

### Append new gitignore data to existing file
```sh
$ goofy generate c++ >> .gitignore          #append data to exisiting gitignore file
```

### Update gitignore files
```sh
$ goofy update
```

### Support for multiple languages
```sh
$ goofy generate c++,python,java,c,visualstudiocode
```

### List all available files

```sh
$ goofy ls
```

## Contribute

Found an issue? Post it in the [issue tracker](https://github.com/yash2696/Goofy/issues). <br> 
Want to add another awesome feature? [Fork](https://github.com/yash2696/Goofy/fork) this repository and add your feature, then send a pull request.

## License
The MIT License (MIT)
Copyright &copy; 2017 Yash Agarwal