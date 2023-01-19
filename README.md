# django-memo

メモを取るアプリ

タグを用いた検索

検索機能の充実

これもさくっと作る CSS を試すことが中心だということを忘れずに

## Model

- Dir
  - NoteBook
  - NoteBook

みたいな感じがいいか?

もしくはDirの構造をなくしてTag だけでどうにかするほうがよい?

```python
from django.db import models


class Dir(models.Model):
    title = models.CharField(max_length=150)


class Tag(models.Model):
    title = models.CharField(max_length=100)


class NoteBook(models.Model):
    parent_dir = models.ForeignKey(Dir, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
```

## Start Project commands

```
make tailwind
make
```

## Features

- CSS Framework
  - flexbox, grid-layout はなんとなくわかったのでもっと楽をする
  - いろいろあるが `tailwindcss` を利用してみる

- Automatically Save
  - いちいち保存ボタンを押さずに 数秒ごとに自動保存する感じ
  - これもショートカットを設定する

- Markdown
  - メモは当然 markdown で書ける
  - Code Highlight も当然
  - 編集しながら横の画面に、Renderした後の(markdown -> html)結果を表示できるようにする?
  - main>(left+right) 左は編集画面、右は結果 みたいな感じ
  - リアルタイムで編集結果が右の画面に出てくるようにする

- 検索
  - memo の内容, memo のタイトル, memo についているタグで検索できるようにする
  - Ajax を使ってぬるっと(RealTime)検索できるようにする? (必要ないかも)
  - header に検索バーをつける感じ?

## Done

- [x] Create <-> Edit の シームレスな移動
  - いちいちCreate, Edit を実行するは面倒なのでCreateしたら即Editに移動する感じにする
  - Create自体も Sidebar から ワンタッチでor `document.addEventListener(...)` でショートカットを設定など
  - Createしたらそのままタイトル、メモ内容を即書けるようにしておく感じ
  - というか Createを押したら URL的には `/memo/create/` -> Redirect -> `/memo/edit/1` に直で飛ぶ
  - めちゃくちゃ簡単だった ショートカットの設定は後日(そもそも必要かどうか考える)

- [x] Sidebar にメモ一覧を表示 タグをつけたメモ一覧を表示など?
  - templatetags を利用する 常にサイドバーを表示しておく
  - これも簡単だった Django すげぇ

## Plugins

- [Django-Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html)
  - 一瞬で tailwind autoreload が設定できる package

- [Django-Browser-Reload](https://github.com/adamchainz/django-browser-reload)
  - runserver の autoreload と browser の自動更新をしてくれる
