Title: blockdiagのライブプレビューアプリLiveDiag 1.0.0 をリリースしました
Date: 2013-07-31 12:21

LiveDiag 1.0.0をリリースしました！

[@tk0miya](http://twitter.com/tk0miya)さんが開発なさっているblockdiag、素晴らしすぎます。手軽にテキストベースでブロック図が書けます。

> [ブロック図生成ツール blockdiag](http://blockdiag.com/)

そして、blockdiagをもっと手軽に使いたい、Markdownも一緒に！という個人的な目的から始めたLiveDiag（アプリ名が安易。。）の開発ですが、それなりにまともに動いているので1.0.0としてリリースしました。コードもNew BSDライセンスで公開しています。

## 機能
- Markdownとblockdiagを同時にライブプレビュー
- seqdiag、actdiag、nwdiagにも対応
- 印刷

## 今後
- blockdiagは事前にインストールしておく必要があるのですが、/usr/bin/blockdiag辺りにないと動がない（symlinkでもOK）のがダサいのでどうにかしたい。  
NSTaskでのコマンド実行時にどうもユーザの$PATHを読み込んでくれません。`/bin/bash -c`経由で実行も試したのですが、自分のpythonbrew環境のblockdiagは実行できませんでした。

- 複数のblockdiagを同時に処理した時の、パフォーマンスが気になる（自分のマシンだと問題ないが）

- Markdownのヘルパーツールが欲しい（テーブル自動生成やリンク化など、Mouでできること）

- blockdiag記法のヘルプをアプリ内から見たい。（作者様に引用していいか聞く）

## インストールはこちらから

> [LiveDiag](http://blog.dataich.com/LiveDiag/)

是非お使い頂いて、フィードバック頂ければ幸いです。