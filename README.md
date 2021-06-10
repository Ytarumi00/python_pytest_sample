# my_unittest
pythonでのユニットテスト手法をまとめる

# Prerequisites
The below are required.   
* python
* pipenv
* pyenv

# Installing
Run pipenv install.
```
pipenv install
```
Also,Python uses the latest version.


# pipenv scripts
docstring test with pytest module
```
pipenv run doctest
```

Run the test script in test dir.
```
pipenv run test
```

Execute the specified test script.
```
pipenv run pytest [testscript path]
```