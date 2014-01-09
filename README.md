# Amazon ISBN Get Script

[ZBar](https://itunes.apple.com/jp/app/zbar-barcode-reader/id344957305?mt=8) で取得したISBN一覧のCSVファイルから、書籍のタイトルとISBNとAmazonURLの一覧ファイルを tsv ファイルにして書き出すスクリプト


## Install

```shell
$ pip install -r install.txt
```

## 使用例

```shell
$ python bin/csv_read_and_change.py ~/Downloads/barcodes.csv
```

## 動作確認

- Python2.7
- PyPy

