# 说明

deepin WSL，修改微软 WSL-DistroLauncher 项目。另外 Github Action 同时构建了 wsldl。

# 环境要求

- 系统版本

  - 对于 x64 系统：版本 1903 或更高版本，内部版本 18362 或更高版本。
  - 对于 ARM64 系统：版本 2004 或更高版本，内部版本 19041 或更高版本。
- 使用WSL 需要开启虚拟化。这里使用Vmware17安装Windows11虚拟机。(使用QEMU、Virtualbox、Vmware16版本即使打开了嵌套虚拟化的选项运行WSL还是提示没有开启虚拟化)

  - 在控制面板，程序开启和关闭，打开“适用于Linux的Windows子系统”和“虚拟机平台”两个可选功能。
  - 需要在Vmware设置中为Windows虚拟机启用嵌套虚拟化，即勾选“启用VT-x/AMD-V”和“启用嵌套分页”选项。
- 安装WSL（使用WSL)

  - `wsl --update`
  - `wsl --set-default-version 2`

# 开启虚拟化及子系统功能支持

除了在控制面板手动开启“适用于Linux的Windows子系统”和“虚拟机平台”功能外，也可以使用命令行开启。在Windows菜单栏找到cmd,选择管理员身份运行。

```bash
wsl --install
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl --update
```

输入完成之后建议重启。

# 对比

wsldl 为第三方提供的启动器，新安装一个 WSL 只需要对应的根文件系统，以及重命名一个可执行文件，使用通用工具来运行一个实例。需要自己使用命令导入根文件系统，另外默认使用root用户，需要自己手动配置其他用户来使用。

WSL-DistroLauncher 官方提供的启动器，需要将根文件系统一起打包成 Windows 下的可执行程序，另外用来上架应用商店也需要依赖该程序。需要安装 cer 证书，双击运行可执行程序，安装成功后根据提示创建一个用户。

# 使用

## WSL-DistroLauncher

## wsldl

# 参考

[微软 WSL-DistroLauncher](https://github.com/microsoft/WSL-DistroLauncher)

[Arch-WSL](https://github.com/VSWSL/Arch-WSL)
