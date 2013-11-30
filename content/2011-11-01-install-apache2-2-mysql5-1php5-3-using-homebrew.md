Title: HomebrewでApache2.2+MySQL5.1+PHP5.3環境を構築

残念ながらHomebrewのリポジトリにはApache、PHPがなく、MySQLは5.5となっています。もっともApacheとPHPに関しては、システムに入ってるものはインストールしないというHomebrewの方針なんだろうと思いますが。で探し回っているとこんなものを見つけました。

> [Alternate formulae repos for Homebrew](https://github.com/adamv/homebrew-alt/)

homebrewのリポジトリにはないものを野良的に公開してくださっています。上記利用させていただいて、MAMP環境を構築します。

### PHP5.3のインストール

HomebrewはFomulaの直URL指定でもインストールすることができます。

	brew install https://raw.github.com/adamv/homebrew-alt/master/duplicates/php.rb --with-mysql

ちなみにduplicatesディレクトリに入っているFomulaは、OS Xに標準で入っているものが集められています。

### MySQL5.1のインストール

	brew install https://raw.github.com/adamv/homebrew-alt/master/versions/mysql51.rb --with-utf8-default --use-gcc

##### 初期設定

	unset TMPDIR
	mysql_install_db

##### 起動・停止

私は、自動起動はさせたくなかったので、launchdには登録しませんでした。

	mysql.server start
	mysql.server stop

### Apache2.2のインストール

	brew install https://raw.github.com/adamv/homebrew-alt/master/duplicates/httpd.rb

httpd.conf等は/usr/local/Cellar/httpd/2.2.21/etc/apache2にあります。

##### PHPなどの設定

私の場合は、extra/php.confを作成し、httpd.confにてIncludeするようにしています。
	
```
vi /usr/local/Cellar/httpd/2.2.21/etc/apache2/extra/php.conf
```

```
LoadModule php5_module /usr/local/Cellar/php/5.3.8/libexec/apache2/libphp5.so
AddType application/x-httpd-php .php .php5 .phtml
```

その他に、DocumentRootを/Users/dataich/Sitesという風にユーザーホームのSitesディレクトリを使用するようにしました。この辺りはお好みで。

##### 起動・停止

	sudo apachectl start
	sudo apachectl stop

あとは、phpinfo()で出力してみたりして確認すればOKです。

**追記 - 2011/11/08**
Homebrewで入れたPHPのpearでpermissionエラーが出ましたので、下記でもろもろ設定しました。

	chmod -R ug+w /usr/local/Cellar/php/5.3.8/lib/php
	pear config-set php_ini /usr/local/etc/php.ini
