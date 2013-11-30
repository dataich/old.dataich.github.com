Title: Irresistible（Wordpressテーマ）のバグ

ブログのデザインを変えました。[WooThemes](http://www.woothemes.com/)から[Irresistible](http://www.woothemes.com/2009/02/irresistible/)を使わせていただきました。

アーカイブでページャーが表示されないバグがあったので手直し。（「前へ」「次へ」が出ない）
archives.phpの41行目あたりのPHPコードの括弧の位置がおかしいので修正。
後の行が修正後。

<script src="http://gist.github.com/249194.js"></script>

一応、連絡入れときました。

**The WooThemes Teamの人から連絡があって、早速修正したバージョンをアップしたとのこと。
対応が早いです。**