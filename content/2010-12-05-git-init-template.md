Title: git init時に特定ディレクトリからhooksをコピーする

Gitで自作したhooksをグローバルに使用するように設定できないかと調べてましたが無理っぽいです。

代替案として、テンプレートディレクトリ（homebrewだと/usr/local/share/git-core/templates/）に用意したhooksを置いておけば、git init時にそこからコピーしてきてくれます。

またシステム領域に自分のファイルを置きたくないとか、hooksを使いたくない場合もあると思います。
その場合は下記のようにgit initの--templateオプションを使用することで特定ディレクトリからhooksをコピーすることが可能です。

<script src="https://gist.github.com/dataich/729045.js?file=git-init-template"></script>
