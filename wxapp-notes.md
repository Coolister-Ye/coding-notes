# 使用vant weapp的notes

在Vant-eapp中提到需要使用package.json这个文件，同样在微信的文档中<https://developers.weixin.qq.com/miniprogram/dev/devtools/npm.html?search-key=npm#_2-%E6%9E%84%E5%BB%BA-npm>, 提到需要在pakcage.json的目录下使用npm install安装依赖的包。但在实际的开发中，新建一个新的mini-program的根目录下是没有package.json这个文件的。

实现上要使用npm依赖的包的完整过程如下：

1. 新建小程序
2. 在根目录下使用运行```npm init```
3. 使用npm安装vant的包```npm i @vant/weapp -S --production```
4. 删除根目录下app.json中的```"style": "v2"```
5. 修改 project.config.json
```
{
  ...
  "setting": {
    ...
    "packNpmManually": true,
    "packNpmRelationList": [
      {
        "packageJsonPath": "./package.json",
        "miniprogramNpmDistDir": "./miniprogram/"
      }
    ]
  }
}
```
6. 构建 npm包,打开微信开发者工具，点击工具 -> 构建npm，并勾选使用npm模块选项，构建完成后，即可引入组件。
