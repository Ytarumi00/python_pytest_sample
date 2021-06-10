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

Run the test script in test dir with pdb.
```
pipenv run test-pdb
```

Run the test script in test dir and get coverage.
```
pipenv run test-cov
```

Run the test script in test dir and get coverage by html.
```
pipenv run test-cov-html
```

Execute the specified test script.
```
pipenv run pytest [testscript path]
```
