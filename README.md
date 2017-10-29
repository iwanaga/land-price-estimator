# land-price-estimator

現在目をつけている土地の販売価格が未公開であるため、土地価格の相場を把握するため作ってみた。
- 土地のおおまかな金額を算出する
- こだわり条件が価格にどれくらい影響するのか比較する

## data source
[国土交通省 国土数値情報 地価公示データ](http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-L01-v2_3.html)
- 販売者が上乗せするマージンは含まれない
- 学習対象の地域を茨城県に絞っている
- 商業用の広すぎる土地や駅から遠すぎる土地を除いた

## how to use
```bash
pip3 install -r requirements.txt

python keras_regressor.py
```

- target example
```csv
地積,不整形地,南側道路あり,駅距離,建ぺい率
200, 0, 1, 1200, 40
200, 0, 0, 1200, 40
200, 1, 1, 1200, 40
```

- output
```python
[16947112.532669306,
 13849169.280391932,
 10187092.222452164]
```
単位は円。

## using TensorBoard
```bash
tensorboard --logdir=logs/simple-net/
```
