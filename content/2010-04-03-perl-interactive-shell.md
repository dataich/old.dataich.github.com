Title: Perlでインタラクティブシェル

Ruby、Python等の言語にはインタラクティブシェルが付いてます。Perlでは[Devel::REPL](http://search.cpan.org/~dhouston/Devel-REPL-1.003009/lib/Devel/REPL.pm)というモジュールをインストールすることで実現できます。（作者様には感謝です。）書くまでもないのですが、インストールにはcpanを使用します。（当方環境はMac OS X 10.6及び、Perl5.10）

	$ sudo cpan
	cpan[1]> install Devel::REPL

インタラクティブシェルの起動には下記Perlを実行します。

	$ re.pl

後はコード書いてEnterを叩いていけば即座に実行されていきます。
ちょっとした実験したりするときに大変重宝します。