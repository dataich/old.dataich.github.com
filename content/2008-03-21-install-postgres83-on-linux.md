Title: Postgres8.3 インストール（Linux）

#### ソース取得

	$ wget ftp://ftp.jp.postgresql.org/source/v8.3.0/postgresql-8.3.0.tar.gz

#### 

#### ビルドに必要なライブラリをインストール

	$ yum install zlib-devel
	$ yum install readline-devel

#### postgresユーザ作成

	$ groupadd postgres
	$ useradd -g postgres -d /usr/local/pgsql postgres
	$ passwd postgres

#### ビルド

	$ tar xvfz postgresql-8.3.0.tar.gz
	$ cd postgresql-8.3.0
	$ ./configure --prefix=/usr/local/pgsql
	$ make all
	$ make install

#### 所有者変更

	$ chown -R postgres:postgres /usr/local/pgsql

#### データディレクトリ作成

	$ su - postgres
	# mkdir /usr/local/pgsql/data
	# /usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data

#### 初期設定

##### プロファイルを開いて

	# vi ~postgres/.bash_profile

##### 下記を追加

	export PATH=$PATH:/usr/local/pgsql/bin
	export POSTGRES_HOME=/usr/local/pgsql
	export PGLIB=$POSTGRES_HOME/lib
	export PGDATA=$POSTGRES_HOME/data
	export MANPATH="$MANPATH":$POSTGRES_HOME/man
	export LD_LIBRARY_PATH="$LD_LIBRARY_PATH":"$PGLIB"

##### 読み直しておく

	# source ~postgres/.bash_profile

##### 自動起動設定

	$ cp /usr/local/src/postgresql-8.3.0/contrib/start-scripts/linux /etc/rc.d/init.d/postgres
	$ chmod +x /etc/rc.d/init.d/postgres
	$ chkconfig --add postgres
