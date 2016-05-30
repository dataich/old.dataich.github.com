Title: CORESERVERからdotCloudにWordpressをお引っ越し

dotCloudがプライベートベータから正式リリースに至り、ベータの頃からのユーザには1年間のProアカウントを発行してくれるということで、PaaSの運用テストを兼ねて、引っ越してみることにしました。個人ではお高いのでずっとは使えませんが。。。

### CORESERVERでやること

まずは、CORESERVER側のWordpressを本体、プラグインともに最新にアップデートしました。
この状態でCORESERVERの管理画面からWordpressデータベースのダンプを取ってローカルに持ってきます。
また、CORESERVER上のWordpressディレクトリもごっそりローカルに持ってきました。

### dotCloud基本設定

ここからがdotCloudに対して行う作業です。
ここではアプリケーション名をwordpressとしています。

dotCloudにアプリケーションを作成します。

	$ dotcloud create wordpress
	Created application "wordpress"

ローカルにディレクトリを作成します。

	$ mkdir dataich.github.io

ここにサービスの設定や、ソースコード等を置いていきます。

Wordpressに必要なサービスPHP、MySQLの設定を行います。dotcloud.ymlに記述します。

	$ vi dataich.github.io/dotcloud.yml

<script src="https://gist.github.com/1119565.js?file=dotcloud.yml"></script>

まずはこの状態で動きを確認してみます。 dotcloud pushコマンドでアプリケーションのソースコード（とはいってもこの段階ではdotcloud.ymlのみ）をPushします。 

	$ dotcloud push wordpress dataich.github.io
	# upload dataich.github.io ssh://dotcloud@uploader.dotcloud.com:21122/wordpress
	# rsync
	Pseudo-terminal will not be allocated because stdin is not a terminal.
	Warning: Permanently added '[uploader.dotcloud.com]:21122,[184.73.14.49]:21122' (RSA) to the list of known hosts.
	building file list ... done
	./
	dotcloud.yml
	
	sent 188 bytes  received 54 bytes  9.88 bytes/sec
	total size is 52  speedup is 0.21
	Deployment for "wordpress" triggered. Will be available in a few seconds.
	2011-08-01 23:04:54 [api] Waiting for the build. (It may take a few minutes)
	2011-08-01 23:04:54 [www.0] Deploying...
	2011-08-01 23:04:54 [data.0] Deploying...
	2011-08-01 23:05:25 [www.0] Service booted
	2011-08-01 23:05:35 [data.0] Service booted
	2011-08-01 23:05:35 [api] All the services are ready. Beginning the build.
	2011-08-01 23:05:36 [data.0] The build started
	2011-08-01 23:05:36 [data.0] This service type does not support build method, ignoring...
	2011-08-01 23:05:36 [data.0] The build finished successfully
	2011-08-01 23:05:36 [www.0] The build started
	2011-08-01 23:05:36 [www.0] Fetched code revision rsync-1312214692.31
	2011-08-01 23:05:37 [www.0] Updating channel "doc.php.net"
	2011-08-01 23:05:37 [www.0] Update of Channel "doc.php.net" succeeded
	2011-08-01 23:05:37 [www.0] Updating channel "pear.php.net"
	2011-08-01 23:05:38 [www.0] Channel "pear.php.net" is up to date
	2011-08-01 23:05:38 [www.0] Updating channel "pecl.php.net"
	2011-08-01 23:05:38 [www.0] Update of Channel "pecl.php.net" succeeded
	2011-08-01 23:05:38 [www.0] -su: line 0: cd: current: No such file or directory
	2011-08-01 23:05:39 [www.0] -su: line 0: cd: current: No such file or directory
	2011-08-01 23:05:39 [www.0] Reloading nginx configuration: nginx.
	2011-08-01 23:05:42 [www.0] php5-fpm: stopped
	2011-08-01 23:05:42 [www.0] php5-fpm: ERROR (abnormal termination)
	2011-08-01 23:05:42 [www.0] The build finished successfully
	2011-08-01 23:05:42 [api] Deploy finished
	
	Deployment finished. Your application is available at the following URLs
	www: http://xxxxxxxx.dotcloud.com/

最後の行にサービスwww（PHP）のURLが発行されているので、アクセスしてみます。当然何のリソースもPushしていないので、404が返ってくるかと思います。

### データの移行

CORESERVERからとったデータベースダンプをdotCloud上のMySQLにロードします。そのためにdotCloudにデータベース、ユーザの作成をしておきます。

まずは、dotcloud infoでMySQLサービスの情報を取得します。ここでは書きませんが、rootパスワードその他情報が表示されるはずです。

	$ dotcloud info wordpress.data

次のコマンドでMySQLのシェルにログインします。 

	$ dotcloud run wordpress.data -- mysql -u root -p
	# mysql -u root -p
	Warning: Permanently added '[xxxxxxxx.dotcloud.com]:12428,[174.129.17.131]:12428' (RSA) to the list of known hosts.
	Enter password:
	Welcome to the MySQL monitor.  Commands end with ; or \g.
	Your MySQL connection id is 34
	Server version: 5.1.41-3ubuntu12.10-log (Ubuntu)
	
	Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
	
	mysql>

DBを作成します。

	mysql> CREATE DATABASE wordpress;
	Query OK, 1 row affected (0.00 sec)

ユーザを作成し、権限を与えます。 

	mysql> GRANT ALL ON wordpress.* TO 'dataich'@'%' IDENTIFIED BY 'XXXXXXXXXX';
	Query OK, 0 rows affected (0.00 sec)

念のため 

	mysql> FLUSH PRIVILEGES;
	Query OK, 0 rows affected (0.00 sec)

では、データをロードします。 データをアップし 

	$ dotcloud run wordpress.data "cat > data.sql" < ~/Desktop/mysql_wp.dump
	# cat > data.sql
	Pseudo-terminal will not be allocated because stdin is not a terminal.
	Warning: Permanently added '[xxxxxxxx.dotcloud.com]:12428,[174.129.17.131]:12428' (RSA) to the list of known hosts.

SSHログインし 

	$ dotcloud ssh wordpress.data
	# $SHELL
	Warning: Permanently added '[xxxxxxxx.dotcloud.com]:12428,[174.129.17.131]:12428' (RSA) to the list of known hosts.
	mysql@wordpress-default-data-0:~$

ロードします。 

	mysql@wordpress-default-data-0:~$ mysql -u dataich -p wordpress < data.sql

### Wordpressソースの移行

アプリケーションのディレクトリにwwwというディレクトリを作り、そこにCORESEVERから持ってきたソースを置きます。

DBの設定を行うため、wp-config.phpを編集します。
dotcloudでは/home/dotcloud/environment.jsonに各種サービスの設定が書かれます。それを読むようにしてあげればOKです。

	$ vi dataich.github.io/www/wp-config.php

<script src="https://gist.github.com/1119568.js?file=wp-config.php"></script>

### nginxの設定

パーマリンク設定をp=123の形から変えている場合は、nginxの設定が必要になります。それにはnginx.confを置いてあげればOKです。 

	$ vi dataich.github.io/www/nginx.conf

<script type="text/javascript" src="https://gist.github.com/1119570.js?file=nginx.conf"></script>

### wp-contentディレクトリの扱い

このままだと1回目以降にPushした際にwp-content以下が消えてしまいます。それではまずいので、すでにwp-contentディレクトリが存在する場合は何もしないようにpostinstallスクリプトを書いておきます。（dotcloudのヘルプそのまんま）

	$ vi dataich.github.io/www/postinstall

<script src="https://gist.github.com/1119572.js?file=postinstall"></script>

	$ chmod +x dataich.github.io/www/postinstall

### dotCloudへWordpressソースをPush

これで、動くはず！さあ、Push!!!

	$ dotcloud push wordpress dataich.github.io
	# upload dataich.github.io ssh://dotcloud@uploader.dotcloud.com:21122/wordpress
	# rsync
	Pseudo-terminal will not be allocated because stdin is not a terminal.
	Warning: Permanently added '[uploader.dotcloud.com]:21122,[184.73.14.49]:21122' (RSA) to the list of known hosts.
	building file list ... done
	./
	www/
	
	..
	..
	..
	
	www: http://xxxxxxxx.dotcloud.com/

上記、URLに正しくアクセスできました。

### カスタムドメインの設定

まずはdotCloud側を設定します。aliasコマンドを使います。

	dataich:~ dataich$ dotcloud alias add wordpress.www dataich.github.io
	Ok. Now please add the following DNS record:
	dataich.github.io. IN CNAME gateway.dotcloud.com.

CNAMEでgateway.dotcloud.com.を設定するように言われるので、VALUE-DOMAIN側のドメイン設定を行います。

[http://dataich.github.io/](http://dataich.github.io/)

上記にアクセスし、動作確認。無事当ブログをdotCloudで動かすことに成功しました。
ざっと確認したところ問題なし。これで暫く運用テストしてみます。

ここまでやっといてアレなのですが、そう負荷のない個人ブログを運用するにはちょっとお値段が辛いです。
もう少しリーズナブルなプランがあればいいのですが。。