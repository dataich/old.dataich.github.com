Title: VirtualBoxをVista上で動かす

とてつもなくはまった。
Vista上にVirtualBox1.5.0を入れたが、CentOSのインストールでこける。
調べてみるとVistaの場合、下記を実行しなければならないことに気づく。

	cd L:\\InnoTek VirtualBox
	VBoxSVC.exe /ReRegServer
	regsvr32.exe VBoxC.dll

また、vistaだからなのかは分らないが、vdiを固定サイズで作成するとゲストOSのインストールにこける、、、。
とりあえずは、可変サイズで作成することで回避。
