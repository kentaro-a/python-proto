# -*- coding: utf-8 -*-

import sys
import io
from pprint import pprint
from logger import *
import pandas as pd


# マルチバイトを扱うときはデフォルトで設定されてる文字コードを変える
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

logger = initLogger()

book = "./test.xlsx"
sheet = "概要"
excel = pd.ExcelFile(book)
df = pd.read_excel(excel, sheet)

# フィルター
_filtered = df.loc[df["No"] < 3, ("No","alt")]

# ソート（降順）
_sorted = df.sort_values(by=('No'), ascending=False)

# 行追加
row = pd.DataFrame([["testalt","testdomain"]], columns=["alt","ドメイン名"])
_addRow = df.append(row)
#pprint(_addRow.ix[2,"alt"])


pprint(df)
