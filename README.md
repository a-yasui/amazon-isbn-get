# Amazon ISBN Get Script

[ZBar](https://itunes.apple.com/jp/app/zbar-barcode-reader/id344957305?mt=8) で取得したISBN一覧のCSVファイルから、書籍のタイトルとISBNとAmazonURLの一覧ファイルを tsv ファイルにして書き出すスクリプト


## Install

```shell
$ pip install -r install.txt
```

## 設定

```:~/.amazon-product-api
[Credentials]
access_key = <Access Key>
secret_key = <secret Key>
associate_tag = <Associate tag>
```

## 使用例

```shell
$ python bin/csv_read_and_change.py ~/Downloads/barcodes.csv
```

## 動作確認

- Python2.7
- PyPy

## ライセンスとか

Copyright (c) 2014 a.yasui@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
