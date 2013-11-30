Title: DTermが便利すぎる

最近はソースのバージョン管理にGitを使っています、もちろんiPhoneアプリのソースにも。
でもXcodeから直接扱えるSCMにはGitが入っていないということで[stackoverflow](http://stackoverflow.com/)で探してたところ[DTerm](http://www.decimus.net/dterm.php)というのを発見。
マカーな人には常識なのかもしれないですが、ターミナルを支援してくれるすごく便利なソフトです。

例えばXcode上で何かのソースを編集中にCommand+Shift+Enterを叩くと、下記のようなHUDなウィンドウが開きます。

![DTerm](http://img.skitch.com/20091215-fbuc8r5qfxrw62xi74jnjdk9gn.png)

何が便利なのかというと、上記ウィンドウを開いた時点で、編集中だったファイルのディレクトリがカレントになってくれているという件。
なのでこのまま git log とか、git statusとか場合によってはgitxってコマンドを叩いてやればいいのです。

![DTerm](http://img.skitch.com/20091215-qin37gy6gedjm7f7x3j7fg25f5.png)

さらに便利なのが、ウィンドウを開いた後にCommand+Shift+Vを叩くと、選択していたファイル名がペーストされるます。
もちろんFinderなんかで複数ファイル選択していた場合は、スペース区切りでペーストしてくれます。
これはいろいろと応用が効きそうです。

ちなみにEnterでコマンドを実行するのですが、Command+Enterするとそのまま標準のTerminalを走らせることもできます。