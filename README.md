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

- Markdown
  - メモは当然 markdown で書ける
  - Code Highlight も当然
  - 編集しながら横の画面に、Renderした後の(markdown -> html)結果を表示できるようにする?
  - main>(left+right) 左は編集画面、右は結果 みたいな感じ
  - リアルタイムで編集結果が右の画面に出てくるようにする

- [ ] 検索
  - Real Time 検索 を JavaScript でできるようにする
  - サイドバーに文字を入力すると直で全部検索できる感じで(後回しでいいかも)

- JavaScriptのテスト
  - ってどうやるの(これは後回しで)

## Now Implementing

`<[:^)]`

## Done

- [x] Create <-> Edit の シームレスな移動
  - いちいちCreate, Edit を実行するは面倒なのでCreateしたら即Editに移動する感じにする
  - Create自体も Sidebar から ワンタッチでor `document.addEventListener(...)` でショートカットを設定など
  - Createしたらそのままタイトル、メモ内容を即書けるようにしておく感じ
  - というか Createを押したら URL的には `/memo/create/` -> Redirect -> `/memo/edit/1` に直で飛ぶ
  - めちゃくちゃ簡単だった ショートカットの設定は後日(そもそも必要かどうか考える)

- [x] [Sidebar にメモ一覧を表示 タグをつけたメモ一覧を表示など?](https://github.com/Lootmann/django-memo/commit/0f41814302e98b94ca40f8549aa3af1eec8742ae)
  - templatetags を利用する 常にサイドバーを表示しておく
  - これも簡単だった Django すげぇ

- [x] [Automatically Save](https://github.com/Lootmann/django-memo/commit/9c8c465a515540bdc8da21507d731d286da6e5ad)
  - いちいち保存ボタンを押さずに 数秒ごとに自動保存する感じ
  - これもショートカットを設定する
  - 実は簡単だった JavaScript の理解がほんの少し進んだ気がする

- [x] [Notebook さくっとセーブ機能詳細](https://github.com/Lootmann/django-memo/commit/9c8c465a515540bdc8da21507d731d286da6e5ad)
  - 保存に成功したら popup を表示 modal?
  - error が発生したら これまた popup
  - できたけど ...

- [x] JavaScript module 化
  - できるんでしょうか? むりなら一つのファイルに全部の関数押し込める
  - 見づらくなるがしょうがない
  - 無理でした

- [x] [検索](https://github.com/Lootmann/django-memo/commit/996c7abc48ed1719c6f25b1f16e8e46f174e6417)
  - header に検索バー == SearchForm をつける
  - 可能であれば）左のサイドバーに検索結果を表示する？
  - とりあえずTopページにそのまま検索結果を表示するように実装 これも簡単

## Plugins

- [Django-Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html)
  - 一瞬で tailwind autoreload が設定できる package

- [Django-Browser-Reload](https://github.com/adamchainz/django-browser-reload)
  - runserver の autoreload と browser の自動更新をしてくれる

## Bug Fix

- 不自然な画面のちらつき
  - Notebook から他のNotebookへ移動するときに完全に真っ白な画面が一フレームだけ表示される
  - それが画面全体のちらつきになり すごくストレスがたまる
  - CSSの読み込みが遅延している感じ? おそらくCSS の読み込み順を考えると治るはず
