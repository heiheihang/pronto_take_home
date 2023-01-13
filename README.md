# pronto_take_home

## Installations:

**python3 should be installed** 

Install the *GitPython* package:

``` 
pip3 install GitPython
```

## Running the Program:

`main.py` contains the entry point to this command line program. It takes one command line argument: the absolute path to the git directory.

### Example
On terminal, get current path (this directory)

```
pwd
```

copy the path

Run the git_dir report (replace the command line argument with the copied path)

```
python3 main.py /path/to/this/directory
```

Output should be something like this:
```
active branch: main
local changes: True
recent commit: True
blame Rufus: True
```

## Testing:
Some basic tests are added to this tool. *Pytest* needs to be installed:

``` 
pip3 install pytest
```

To run the tests:

``` 
pytest
```
## TODO:
Tests are incomplete. They could fail conditionally on the status of this git repo. Mocks are needed.

