Title: mysqldumpでのBLOB項目

mysqldumpに--hex-blobオプションをつけてやることで、BLOBカラムがHEX出力される。

	mysqldump --hex-blob -u ユーザ -p データベース名 > 出力ファイルパス
