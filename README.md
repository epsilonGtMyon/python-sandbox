# python-sandbox

Pythonを試す

## VSCodeの拡張機能

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- [Mypy Type Checker](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker)

- [Python Environment Manager](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-environment-manager)


## 仮想環境を作る(venv)

```
python -m venv .venv
```


## インストールパッケージの読み書き

### 書き出し

```
pip freeze > requirements.txt
```

### 読み込み

```
pip install -r requirements.txt
```