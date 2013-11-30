Title: Homebrewで特定のプロダクトがアップグレードされないようにする
Date: 2012-08-03 21:45

brew update後、brew upgradeすると、バージョンアップ対象のものは全てアップグレードされます。  
業務でgroonga+MySQLを使用しているのですが、groongaとMySQLのバージョンが合ってなかったりすると、多分壊れます。というかインストール時にそれでハマったので、間違ってアップグレードされてしまうと非常に困ります。他にもapacheを間違ってbrew upgrade後、brew cleanなどしてしまうとhttpd.conf消えちゃうなど。

でどうするかというと、brew versionsでキープしたいバージョンのFormulaをチェックアウトしておけばいいです。

	$ brew versions groonga
	2.0.3    git checkout 8330960 /usr/local/Library/Formula/groonga.rb # キープしときたいバージョン
	2.0.4    git checkout 409e6a8 /usr/local/Library/Formula/groonga.rb
	2.0.2    git checkout d622e37 /usr/local/Library/Formula/groonga.rb
	…
	…
	
	$ cd /usr/local
	$ git checkout 8330960 /usr/local/Library/Formula/groonga.rb
	
	$ brew versions mysql
	5.5.25a  git checkout 2814e3a /usr/local/Library/Formula/mysql.rb
	5.5.25   git checkout 5bcd1f3 /usr/local/Library/Formula/mysql.rb
	5.5.24   git checkout a977fbd /usr/local/Library/Formula/mysql.rb # キープしときたいバージョン
	…
	…
	
	$ git checkout a977fbd /usr/local/Library/Formula/mysql.rb

これで、brew updateしても、上記でcheckoutされたFormulaはキープされ続けるので、upgradeされることがなくなります。
