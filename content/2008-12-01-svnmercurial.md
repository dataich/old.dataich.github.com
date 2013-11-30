Title: svn+mercurial

> [Python Package Index : hgsvn 0.1.6](http://pypi.python.org/pypi/hgsvn)

既存のsvnリポジトリがあって、ローカルでもコミットしたかったので。

Leopardで使うためには、こうやる。

	#必要なパッケージのインストール
	$ sudo port install subversion
	$ sudo port install mercurial
	$ sudo port install py-svn
	
	#hgsvnソースを取得
	$ hg clone http://hg.pitrou.net/public/hgsvn/main hgsvn
	
	#hgsvnインストール
	$ sudo easy_install -s /opt/local/bin hgsvn
	
	#既存のsvnリポジトリからソースを取得
	$ hgimportsvn http://localhost/svnrepos
	$ cd svnrepos
	$ hgpullsvn
	
	#hgローカルリポジトリへのコミット
	$ hg commit
	
	#svnリポジトリから更新
	$ hgpullsvn
	
	#svnリポジトリへコミット
	$ hgpushsvn

ちなみにpython2.5がデフォルトpythonだとhgpushsvnがこけます。
py-svnがそのままだとpython2.4のsite-packagesにインストールされるようで、
py-svnが見つからないとか言われます。
解決するのが面倒そうだったので下記のようにしてpython2.4に切り替えてます。

	$ sudo port install python_select
	$ sudo python_select python24
