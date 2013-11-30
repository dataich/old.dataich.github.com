Title: Android - サンプルアプリケーションの概要

前回作成したサンプルアプリケーションのディレクトリ構成を見てみると、下記のようになっています。

	android
	├── AndroidManifest.xml
	├── res
	│   ├── drawable
	│   │   └── icon.png
	│   ├── layout
	│   │   └── main.xm
	│   └── values
	│       └── strings.xml
	└── src
	    └── com
	        └── lancard
	            └── tasklist
	                ├── R.java
	                └── TaskList.java
  
まずは、resから見ていきます。


**drawable**
: ここには、アプリケーションで使用する画像ファイルを配置します。

**layout**
: ここには、アプリケーションで使用する画面定義ファイルを配置します。
デフォルトではmain.xmlが作成されていますが、アプリケーションによっては複数の画面を使用したい場合もあります。
その場合には、ここにxmlを追加することになります。

**values**
: ここには、アプリケーションで使用する、文字列定義等のファイルを配置します。デフォルトではstrings.xmlが用意されていますが、他にもarrays.xml、colors.xmlなどを配置できます。

次に、srcを見てみます。

#### R.java

res配下の各種定義ファイルに書かれているリソースにアクセスするためのクラスで、自動生成され、直接編集してはいけません。
ソースを見てみると下記のようになっているかと思います。
res配下のディレクトリ構成と同じように、クラスが作成されているかと思います。
res/drawable/icon.pnfの場合は、R.drawable.iconとなっています。
res/strings.xmlの場合は、xml 内のresources/stringの属性app_nameが読み込まれています。
これを使用して、各種リソースにアクセスすることになります。

	package com.lancard.tasklist;
	
	public final class R {
	    public static final class attr {
	    }
	
	    public static final class drawable {
	        public static final int icon=0x7f020000;
	    }
	
	    public static final class layout {
	        public static final int main=0x7f030000;
	    }
	
	    public static final class string {
	        public static final int app_name=0x7f040000;
	    }
	}

#### TaskList.java

メインクラスになります。ソースを見てみます。
基本的にメインクラスは、android.app.Activityを継承して作成します。
もちろん、 Activityクラスを継承した別クラスも用意されています。
onCreateメソッドは、アプリケーション実行時に最初に呼ばれるメソッドで、メソッドの最初で親クラスのonCreateメソッドを呼び出す必要があります。
その後、setContentView(R.layout.main)として、メイン画面のビュー定義をセットしています。

	package com.lancard.tasklist;
	
	import android.app.Activity;
	import android.os.Bundle;
	
	public class TaskList extends Activity {
	
	    /** Called when the activity is first created. */
	    @Override
	    public void onCreate(Bundle icicle) {
	        super.onCreate(icicle);
	        setContentView(R.layout.main);
	    }
	}

次に、AndroidManifest.xmlを見てみます。
アプリケーション全体の設定ファイルになっており、デフォルトでは下記のようになっているかと思います。

	<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.lancard.tasklist">
	    <application android:icon="@drawable/icon">
	        <activity android:name=".TaskList" android:label="@string/app_name">
	            <intent-filter>
	                <action android:name="android.intent.action.MAIN" />
	                <category android:name="android.intent.category.LAUNCHER" />
	            </intent-filter>
	        </activity>
	    </application>
	</manifest>

3行目の android:icon="@drawable/icon" は、R.drawable.iconを指定していることになります。
