Title: ただTitaniumチュートリアルをやってみただけだがエラーが出たので、ここに書いた

## 開発環境

Appcelerator SDKとTitanium SDKをインストール
> [Appcelerator Product Downloads](http://appcelerator.org/download)  
> [Appcelerator Titanium SDK Downloads](http://titaniumapp.com/download)

## チュートリアってみる。

> [Starting your first Titanium project](http://titaniumapp.com/documentation/starting-your-first-titanium-project)

上記を参考に進めてみた。

#### プロジェクト生成

Terminalから

	$ app create:project . myproject titanium

下記のように出力されればプロジェクト生成成功。

	Using service titanium
	Connecting to update server ...
	Fetching release info from distribution server...
	Your project was created in /Users/yourname/myproject
	Appcelerator titanium project created ... Code strong!

ちなみにSDKのインストールに失敗したのか、最初はうまくいかなかった。
再インストールしたらうまくいった。

#### プロジェクト（アプリケーション）のパッケージング


	$ cd myproject
	$ app package:project osx #Windows向けの場合はwin32
	Create directory [/Users/yoshida/Work/temp/myproject/stage]? (Y)es,(N)o,(A)ll [Y] Y
	Connecting to update server ...
	Fetching release info from distribution server...
	(1/1) titanium:osx: 0% |
	(1/1) titanium:osx: 1% |
	...
	(1/1) titanium:osx: 100% |ooooooooooooooooooooooooooooooooooooooooooooooooooooo| 5.4MB 302.5KB/s ETA: 00:00:00
	
	Installed titanium:osx 0.1
	Packaging Titanium for target os: osx
	Validating tiapp.xml ...
	Looks good ... Let's packager up!
	Your Titanium application is located in /Users/yoshida/Work/temp/myproject/stage

これで/Users/yoshida/Work/temp/myproject/stageにmyproject.appとしてパッケージングされる。
myproject.appを起動した。

なんかエラーが出るが、

![titanium_error](http://dl.dropbox.com/u/126064/dataich.github.io.images/titanium_error.jpg)

無視してクリックするとウィンドウが表示された。

![titanium_sample](http://dl.dropbox.com/u/126064/dataich.github.io.images/titanium_sample.jpg)

Javascript APIを使ったサンプルがコード付きで試せるので、いろいろと見てみよう。
但し、上記エラーのせいか、ボタンクリック系のサンプルが動かない、、、