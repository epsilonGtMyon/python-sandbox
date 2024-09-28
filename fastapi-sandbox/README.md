# fastapi-sandbox

FastAPIを試す


## 環境準備


```
pip install "fastapi[all]"
```


## 実行

直下の `main.py` の `app` を実行する場合

```
uvicorn main:app --reload --log-config log_config.yaml
```

`log_config.yaml` にマルチバイト文字があると起動に失敗

その他のオプションは[UvicornのSettings](https://www.uvicorn.org/settings/)に書いている


