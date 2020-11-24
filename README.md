# HIT每日上报辅助小工具 ![](https://img.shields.io/badge/license-GNU-blue) ![](https://img.shields.io/badge/Python-3.7.4-blue)

**请注意，使用本工具前请务必保证你的信息与昨日相比未发生改变**

这是一个对网页进行操作的自动化python脚本，使用selenium对网站进行控制。这个脚本对windows系统以及mac做了适配，mac没有进行debug（因为懒）。macOS请自行debug

为了保证你的统一身份认证密码的安全，初次使用脚本会创建一个account.config文件以保存你的学号，而密码会通过keyring工具保存在Windows的凭据管理器或是mac的钥匙串中。

使用pyinstaller对windows版本进行了编译：[Release](https://github.com/VinKK1998/hit-mrsb/releases/tag/v1.22474487139)



## 使用可执行文件

你需要以默认位置安装版本号大于等于86的Chrome，至项目发布所使用的是Google Chrome Version 87.0.4280.66 (Official Build) (64-bit) 尽量保证chrome为最新版本

下载 [Release](https://github.com/VinKK1998/hit-mrsb/releases/tag/v1.22474487139) 中的zip并解压，双击执行mrsb.exe，请允许应用通过防火墙。

初次使用会要求提供统一身份认证学号及密码，并保存在凭据中，后续使用则不需要。



## 直接使用源码脚本

你需要准备Python3, keyring, keyring.alt, selenium

Windows User：

```
pip install keyring keyring.alt selenium
```

Mac User：

```
pip3 install keyring keyring.alt selenium
```

你需要以默认位置安装版本号大于等于86的Chrome，至项目发布所使用的是Google Chrome Version 87.0.4280.66 (Official Build) (64-bit) 尽量保证chrome为最新版本

克隆这个repo并启动脚本：

```
git clone https://github.com/VinKK1998/hit-mrsb
cd hit-mrsb
python mrsb.py
```

mac用户需要使用python3来替换最后的python（在你默认python是2.0的时候）。

初次使用会要求提供统一身份认证学号及密码，并保存在凭据中，后续使用则不需要。

出现的问题请在issues中提交
