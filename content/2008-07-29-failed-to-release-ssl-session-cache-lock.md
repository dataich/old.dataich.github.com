Title: Failed to release SSL session cache lock

/var/log/httpd/ssl_error.logを見ると下記エラーが多発していた。

	[warn] (13)Permission denied: Failed to release SSL session cache lock
	[warn] (13)Permission denied: Failed to acquire SSL session cache lock

/etc/httpd/conf/httpd.confを見てみるとApacheの実行ユーザがnobodyになっているのに対し、sslのキャッシュディレクトリである/var/cache/mod_sslの所有者がデフォルトのapache:rootのままだった、、、。
こいつを nobody:rootに変えてやって、Apache再起動で解決。
