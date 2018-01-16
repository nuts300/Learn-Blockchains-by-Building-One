# Learn Blockchains by Building One
## ブロックチェーンAPI学習

元サイト
https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

日本語訳(Qiita)
https://qiita.com/hidehiro98/items/841ece65d896aeaa8a2a

## 環境
|      |             |
|:-----|:------------|
| Lang | Python 3.6.2|
| FW   | Falcon      |

## エンドポイント
生存確認
```
GET: /v1/my-blockchain/hello
```

トランザクション生成
```
POST: /v1/my-blockchain/transactions/new
```

採掘結果取得
```
GET: /v1/my-blockchain/mine
```

最も長いチェーン取得
```
GET: /v1/my-blockchain/chain
```

ノード追加
```
POST: /v1/my-blockchain/node/register
```

チェーン置き換え
```
GET: /v1/my-blockchain/nodes/resolve
```

## セットアップ
```commandline
docker-compose up --build
``` 
