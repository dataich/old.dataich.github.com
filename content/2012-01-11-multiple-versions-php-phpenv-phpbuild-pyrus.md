Title: phpenv+php-build+pyrusでの複数バージョンPHP管理など

## 必要なもの

* phpenv PHPのバージョン切り替え（切り替えるのみ、PHPのインストールはできない。rbenvを流用）
* php-build 複数バージョンPHPのインストールマネージャ
* Pyrus PEAR後継パッケージマネージャ

## phpenvのインストール

	$ curl https://raw.github.com/CHH/phpenv/master/bin/phpenv-install.sh | sh
	Installing phpenv in /Users/dataich/.phpenv
	remote: Counting objects: 1008, done.
	remote: Compressing objects: 100% (422/422), done.
	remote: Total 1008 (delta 633), reused 928 (delta 558)
	Receiving objects: 100% (1008/1008), 135.47 KiB | 124 KiB/s, done.
	Resolving deltas: 100% (633/633), done.
	Success.
	
	Now add /Users/dataich/.phpenv/bin to your $PATH, add "eval $(phpenv init -)" at the end of your ~/.bashrc and restart your shell to use phpenv.
    
最後の行で言われたとおり、`~/.bashrc`に追記します。

	export PATH="/Users/dataich/.phpenv/bin:$PATH"
	eval "$(phpenv init -)"
  
phpenvは~/.phpenv以下にインストールされており、~/.phpenv/versionsにバージョンごとのPHPをインストールしてやることで切り替えが可能になります。

## php-buildのインストール

	$ git clone https://github.com/CHH/php-build.git
	$ cd php-build
	$ ./install.sh
	Installing php-build in /usr/local
	- Creating Directories... Done.
	- Copying files... Done.
    
これで必要なもののインストールは完了です。また、現状はインストールできるPHPバージョンが増えたりした場合は、git pullして./install.shを再度実行しないといけないと思います。

## php-buildを使用してPHPをインストール

まずはインストール可能なバージョンを調べます。

	$ php-build --definitions
	5.2.17
	5.3.2
	5.3.6
	5.3.8
	5.3.9RC3
	5.3snapshot
	5.4.0RC1
	5.4.0RC2
	5.4.0RC3
	5.4.0RC4
	5.4.0alpha3
	5.4.0beta1
	5.4.0beta2
	5.4snapshot
    
では上記から好きなバージョンを選んでインストールしています。今回は業務で必須なので5.3.8を。

## とその前にApacheモジュールどうする？

php-buildはApacheモジュールのビルドに対応していません（GitHubにIssueにはFeatureとして登録されてます。）。
ソースを読んでみるconfigure_optionを呼び出してあげればよさそうです。なのでdefinitionsに定義してあるスクリプトに変更を入れてあげます。
このdefinitions配下にあるスクリプトはいろいろビルド方法を調整する時に使えそうです（pyrusじゃなくてpear使いたかったらwith_pear書いて、install_pyrusコメントアウトするとか。）

	# /usr/local/share/php-build/definitions/5.3.8
	configure_option "--with-apxs2" "/usr/local/Cellar/httpd/2.2.21/sbin/apxs" #この行を追加する。apxsへのパスは環境に応じて置き換えてください。
	install_package "http://www.php.net/distributions/php-5.3.8.tar.bz2"
	install_pyrus
	
	install_xdebug "2.1.2"
    
まあPHPをビルドする度にlibphp5.soを上書きしてしまうだろうということと、phpenvで切り替えた時どうするのっていうのはありますが・・・。

## 気をとりなおしてphp-buildを使用してPHPをインストール

ではphp-buildを使用して5.3.8をインストールします。プレフィックスには~/.phpenv/versions/5.3.8を指定します。実はここでちょっとはまったのですが、最後の引数はプレフィックスなのでフルパスである必要があります。

	$ php-build 5.3.8 ~/.phpenv/versions/5.3.8
	Loaded pyrus Plugin.
	Loaded xdebug Plugin.
	php.ini-production gets used as php.ini
	
	Building 5.3.8 into /Users/dataich/.phpenv/versions/5.3.8
	
	[Downloading]: http://www.php.net/distributions/php-5.3.8.tar.bz2
	[Configure]: /usr/local/bin/../tmp/php-build/source/5.3.8
	[Make]: /usr/local/bin/../tmp/php-build/source/5.3.8
	[Pyrus]: Downloading from http://pear2.php.net/pyrus.phar
	[Pyrus]: Installing executable in /Users/dataich/.phpenv/versions/5.3.8/bin/pyrus
	[XDebug]: Downloading http://xdebug.org/files/xdebug-2.1.2.tgz
	[XDebug]: Compiling in /usr/local/bin/../tmp/php-build/source/xdebug-2.1.2
	[XDebug]: Installing XDebug configuration in /Users/dataich/.phpenv/versions/5.3.8/etc/conf.d/xdebug.ini
	[XDebug]: Cleaning up.
	[Info]: The Log File is not empty, but the Build did not fail. Maybe just warnings got logged. You can review the log in /usr/local/bin/../var/log/php-build/error.5.3.8.20120106174319.log
	[Success]: Built 5.3.8 successfully.
    
ちなみにphp.iniは~/.phpenv/versions/5.3.8/etc配下のを使うようになっています。また~/.phpenv/versions/5.3.8/etc/conf.d配下のものも読むようになっており、
xdebug.iniなどが置いてあります。バージョンごとにiniファイルを持っているので便利です。

## phpenvを使ってみる

ではphpenvにて切り替えられるバージョンを調べてみます。

	$ phpenv versions
	5.3.8
    
先ほどインスールした5.3.8が使用できる状態になっていますので、グローバルに使うようにします。

	$ phpenv global 5.3.8
	$ phpenv versions
	* 5.3.8 (set by /Users/dataich/.rbenv-version)
	$ php -v
	PHP 5.3.8 (cli) (built: Jan 11 2012 23:20:46)
	Copyright (c) 1997-2011 The PHP Group
	Zend Engine v2.3.0, Copyright (c) 1998-2011 Zend Technologies
	with Xdebug v2.1.2, Copyright (c) 2002-2011, by Derick Rethans
    
また、下記のようにlocalを使うとカレントディレクトリに.rbenv-versionというファイルが作られ、そのディレクトリ配下では一度指定したバージョンが使われるようになります。

	$ phpenv local 5.4snapshot
    
## phpenv rehashコマンド

phpenvでは.phpenv/shims/にパスを通すようになっており、そこを介してexecutableなコマンドを実行したりします。

	$ ll .phpenv/shims
    
何もないはずです。ここを構築するにはrehashを使います。

	$ phpenv rehash
	$ ll .phpenv/shims/
	total 56
	-rwxr-xr-x 7 dataich staff 102 1 11 23:31 phar
	-rwxr-xr-x 7 dataich staff 102 1 11 23:31 phar.phar
	-rwxr-xr-x 7 dataich staff 102 1 11 23:31 php
	-rwxr-xr-x 7 dataich staff 102 1 11 23:31 php-config
	-rwxr-xr-x 7 dataich staff 102 1 11 23:31 phpize
	-rwxr-xr-x 7 dataich staff 102 1 11 23:31 pyrus
	-rwxr-xr-x 7 dataich staff 102 1 11 23:31 pyrus.phar
    
これを実行することでインストールされているPHPやPEARモジュールの実体を探してきて、シムリンクぽいシェルスクリプトが作成されます。新しいバージョンのPHPや、phpunitなどの実行モジュールをインストールした後には実行しておきましょう。

## Pyrus

で次にPyrusです。PEARの後継にあたるパッケージマネージャです。使ってみます。php-buildでインストールした際に既に使えるようになっています。

	$ pyrus config-show
	Pyrus version 2.0.0a3 SHA-1: BE7EA9D171AE3873F1BBAF692EEE9165BB14BD5D
	Using PEAR installation found at /Users/dataich/.phpenv/versions/5.3.8/pyrus
	System paths:
	php_dir => /Users/dataich/.phpenv/versions/5.3.8/pyrus/php
	ext_dir => /Users/dataich/.phpenv/versions/5.3.8/lib/php/extensions/no-debug-non-zts-20090626
	cfg_dir => /Users/dataich/.phpenv/versions/5.3.8/pyrus/cfg
	doc_dir => /Users/dataich/.phpenv/versions/5.3.8/pyrus/docs
	bin_dir => /Users/dataich/.phpenv/versions/5.3.8/bin/
	data_dir => /Users/dataich/.phpenv/versions/5.3.8/pyrus/data
	www_dir => /Users/dataich/.phpenv/versions/5.3.8/pyrus/www
	test_dir => /Users/dataich/.phpenv/versions/5.3.8/pyrus/tests
	src_dir => /Users/dataich/.phpenv/versions/5.3.8/pyrus/src
	php_bin => /Users/dataich/.phpenv/versions/5.3.8/bin/php
	php_ini => /Users/dataich/.phpenv/versions/5.3.8/etc/php.ini
	php_prefix => /Users/dataich/.phpenv/versions/5.3.8/bin/
	php_suffix =>
	...
    
パッケージのインストール先ディレクトリ等がphpenvで指定している現在のバージョン配下になっています、素晴らしい！
これでPEARモジュールは現在使用中のPHPのバージョン配下に収まることになります。

pyrusコマンドは第一引数にディレクトリを渡してやることで、そのディレクトリローカルなパッケージ管理ができるようになるので、非常に便利です。
ただphp-buildが生成するshimにバグがあって、使えない状態だったのですが、作者さんに投げたところ数時間で対応していただきました、これで常用できそうです。

> [#35: Cannot use pyrus locally - Issues - CHH/php-build - GitHub](https://github.com/CHH/php-build/issues/35) 

ただし現状Pyrusだとプロジェクトローカルなインストールは簡単なのですが、依存関係の設定ファイルだけリポジトリに上げておいて、コマンド一発で全部インストールみたいなことが難しいです。
package.xmlを作ればできるようなのですが、そもそもPEARモジュールのビルド用ぽくて、扱いが難しいです。
次のエントリーではその辺りを上手く解決してくれる、Onion、Composer辺り扱ってみます。

## 参考

>[phpenv で複数の PHP 環境を管理する](http://blog.yuyat.jp/archives/1446) 

>[php-build で PHP5.4.0 beta1 をビルドする](http://blog.yuyat.jp/archives/1376) 

>[Using Pyrus To ManagePEAR Installable Vendor Libs](http://saltybeagle.com/2011/01/using-pyrus-to-manage-pear-installable-vendor-libs/)

