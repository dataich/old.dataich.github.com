Title: MacでPPTP（VPN）接続しつつ、通常の接続も行えるようにする方法

[Mac OS X 10.5でPPTP接続する方法](http://www.kuins.kyoto-u.ac.jp/KUINS3/pptp/macos/leopard_PPTP/)

MacでPPTP使ってVPN接続するようになって、いろいろと面倒だったことが解決して良かった。
と思っていたのですが、PPTPの方の優先度を上げないといけない場合は、通常のインターネット接続が駄目になってしまうようです。
ローカルなネットワークにPPTPに繋ぎながら、普通にインターネットもしたいということで下記にて解決しました。

方法としては、PPTPの優先度は通常のインターネット接続より下げておいて、特定のネットワークアクセスの場合のみPPTPインターフェースを使うようにしてあげればいいようです。VPNを接続した後、ターミナルで下記コマンドを実行すればOK。

<script src="https://gist.github.com/dataich/843881.js?file=gistfile1.eclass"></script>

ただ毎回ターミナル上げるのは面倒臭いです。 ちょっと調べると、PPTPが開始するときに実行されるスクリプト（[参考](https://discussionsjapan.apple.com/thread/10088702)）があるじゃないですか。ということで

<script src="https://gist.github.com/dataich/843881.js?file=gistfile2.eclass"></script>

<script src="https://gist.github.com/dataich/843881.js?file=ip-up"></script>

のような感じで、route add するスクリプトを書きました。

<script src="https://gist.github.com/843881.js?file=gistfile4.eclass"></script>

するのをお忘れなく。

もっと楽、シンプルな方法があったら教えてください。

**追記**
誤解を招く書き方でしたが、VPN側にインターネット接続の制限が掛かってる場合の話です。
VPNにそういう制限がなかったら、こんな作業する必要はありません。