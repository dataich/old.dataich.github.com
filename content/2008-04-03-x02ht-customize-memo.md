Title: X02HT　カスタマイズメモ

#### アプリケーションアンロック

1.regeditSTG2.exe（[http://www.modaco.com/content/HTC-Breeze-Breeze-MoDaCo-com/244205/Mteor-application-unlock-solution/](http://www.modaco.com/content/HTC-Breeze-Breeze-MoDaCo-com/244205/Mteor-application-unlock-solution/) ）をX02HT側で起動し、下記レジストリの変更

	[\HKEY_LOCAL_MACHINE\Security\Policies\Policies]
	00001001=1
	00001005=40
	00001017=144
	
2.一旦、再起動

3.ホストと接続している状態で、[SDA_ApplicationUnlock](http://wiki.xda-developers.com/uploads/SDA_ApplicationUnlock.zip)を起動し、実行する。

4.再起動し、完了。

#### フォント変更

1.  システムフォント変更
フォント（ttc等）を\Windows\にコピー
2.  Outlookフォント変更
\Windows\msgothic.ac3を0バイトの同名ファイルで上書き→これをしないと、Outlookのフォントが変わらない ※VistaのMobileCenter経由だと上書きできなかったので、XPのActiveSyncにて上書きした
3.  レジストリ変更  
※下記表のシステムフォント変更参照

#### レジストリ変更

ホストと接続している状態で、MobileRegistryEditor（[http://www.freewareppc.com/utilities/mobileregistryeditor.shtml](http://www.freewareppc.com/utilities/mobileregistryeditor.shtml)）を起動し、実行する。
<table border="0">
<tbody>
<tr>
<th>内容</th>
<th></th>
<th>Key</th>
<th>Value</th>
</tr>
<tr>
<td>SoftBankメール保存ディレクトリ</td>
<td>\HKEY_LOCAL_MACHINE\Software\Arcsoft\ArcSoft MMS UA\Config\Folder</td>
<td>CannedTextFile</td>
<td>「Program Files」を「Storage Card」</td>
</tr>
<tr>
<td>SoftBankメール保存ディレクトリ</td>
<td>\HKEY_LOCAL_MACHINE\Software\Arcsoft\ArcSoft MMS UA\Config\Folder</td>
<td>TemplatePath</td>
<td>「Program Files」を「Storage Card」</td>
</tr>
<tr>
<td>SoftBankメール保存ディレクトリ</td>
<td>\HKEY_LOCAL_MACHINE\Software\Arcsoft\ArcSoft MMS UA\Config\Folder</td>
<td>UAContentsPath</td>
<td>「Program Files」を「Storage Card」</td>
</tr>
<tr>
<td>IE初期ページ</td>
<td>\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\AboutURLs</td>
<td>home_0409</td>
<td>任意URL</td>
</tr>
<tr>
<td>IE初期ページ</td>
<td>\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\AboutURLs</td>
<td>home_0411</td>
<td>任意URL</td>
</tr>
<tr>
<td>Outlookメール新規作成時サイズ</td>
<td>\HKEY_LOCAL_MACHINE\Software\Microsoft\Inbox\RichEditHostFontSize</td>
<td>-</td>
<td>9</td>
</tr>
<tr>
<td>HSDPAアイコン表示</td>
<td>\HKEY_LOCAL_MACHINE\Software\OEM\RIL</td>
<td>EnableHSDPAIcon</td>
<td>1</td>
</tr>
<tr>
<td>キャッシュ</td>
<td>\HKEY_LOCAL_MACHINE\System\GDI\GLYPHCACHE</td>
<td>limit</td>
<td>2097152</td>
</tr>
<tr>
<td>キャッシュ</td>
<td>\HKEY_LOCAL_MACHINE\System\StorageManager\FATFS</td>
<td>CacheSize</td>
<td>256</td>
</tr>
<tr>
<td>キャッシュ</td>
<td>\HKEY_LOCAL_MACHINE\System\StorageManager\Filters\fsreplxfilt</td>
<td>ReplStoreCacheSize</td>
<td>256</td>
</tr>
<tr>
<td>リアルQVGA</td>
<td>\HKEY_LOCAL_MACHINE\Driver\Display\GPE</td>
<td>LogicalPixelsX</td>
<td>96</td>
</tr>
<tr>
<td>リアルQVGA</td>
<td>\HKEY_LOCAL_MACHINE\Driver\Display\GPE</td>
<td>LogicalPixelsY</td>
<td>96</td>
</tr>
<tr>
<td>メニューフォントサイズ</td>
<td>\HKEY_LOCAL_MACHINE\System\GWE\Menu\PopFnt</td>
<td>Ht</td>
<td>4294967284</td>
</tr>
<tr>
<td>システムフォントサイズ</td>
<td>\HKEY_LOCAL_MACHINE\System\GDI\SYSFNT\</td>
<td>Ht</td>
<td>4294967284</td>
</tr>
<tr>
<td>システムフォント変更</td>
<td>\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\FontLink\SystemLink</td>
<td>Courier New</td>
<td>-</td>
</tr>
<tr>
<td>システムフォント変更</td>
<td>\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\FontLink\SystemLink</td>
<td>Nina</td>
<td>-</td>
</tr>
</tbody></table>

#### インストールアプリケーション

<table border="0">
<tbody>
<tr>
<td>アラーム</td>
<td>[CT AlarmClock Lite for WM Smartphones](http://www.connectivetools.com/)</td>
</tr>
<tr>
<td>ClearType有効</td>
<td>[ctt](http://forum.xda-developers.com/showthread.php?t=260506)</td>
</tr>
<tr>
<td>コピーペースト</td>
<td>[EasyClip](http://d.hatena.ne.jp/KOTETU/00000115)</td>
</tr>
<tr>
<td>Skype、Twitterその他</td>
<td>[fring](http://www.fring.com/download/)</td>
</tr>
<tr>
<td>予定管理</td>
<td>[OffisnailDate](http://www.offisnail.info/index.html)</td>
</tr>
<tr>
<td>キー割り当て</td>
<td>[StdLink](http://www.offisnail.info/index.html)</td>
</tr>
<tr>
<td>GoogleCalendarとの同期</td>
<td>[OggSync](http://oggsync.com/)</td>
</tr>
</tbody></table>
</div>