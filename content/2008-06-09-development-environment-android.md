Title: Android - 開発環境

### 開発環境を構築する

1.  Android SDKのインストール
Android SDKをダウンロードし、任意ディレクトリに解凍します。
2.  Eclipse Pluginのインストール
Help&gt;Software Updates&gt;Find and Installにて、下記URLを追加し、インストールします。
3.  Windows&gt;Preference&gt;AndroidのSDK LocationにAndroid SDKを解凍したディレクトリを指定します。 これで開発環境構築は完了となります。

### サンプルプロジェクト作成

EclipseにてFile&gt;New&gt;Projectを選択し、Android&gt;Android Projectを選択。
下記のように入力して、プロジェクトを作成します。

*   Project name android
    *   Eclipseでのプロジェクト名
*   Package name com.lancard.tasklist
    *   アプリケーションのパッケージ名
*   Activity name TaskList
    *   アプリケーションのメインクラス名
*   Application name Task List
    *   アプリケーション名（画面に表示するタイトルとしても使用）

### エミュレータを実行する

Eclipse上で、プロジェクトを右クリック、Run As&gt;Android Applicationを選択。
下記のように、エミュレータが起動すれば成功です。

![android](http://dl.dropbox.com/u/126064/dataich.github.io.images/android.png)