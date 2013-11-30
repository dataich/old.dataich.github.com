Title: Gitで短すぎるコミットログを禁止する

> [コミットコメントを意地でも書かせたい](http://d.hatena.ne.jp/kanu-orz/20100531/1275279046)

上記を見て感化されたので、Gitで短すぎるコミットログのコミットを禁止するhookを書きました。

<script src="https://gist.github.com/dataich/728190.js?file=commit-msg"></script>

せっかくMacなのでsayコマンド使ってAlexさんにしゃべらせてます。
ちなみにコミットログはcommit-msgスクリプトの第一引数に.git/COMMIT_EDITMSGというファイル名が渡ってきますので、それを覗いてやれば参照できます。