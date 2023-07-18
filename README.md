<div align="center">
  <a href="https://github.com/canxin121">
    <img src="https://socialify.git.ci/canxin121/nonebot_plugin_pokesomeone/image?font=Raleway&forks=1&issues=1&language=1&logo=https%3A%2F%2Fcanxin121.github.io%2Fdocs%2Flogo.png&name=1&owner=1&pattern=Charlie%20Brown&pulls=1&stargazers=1&theme=Auto" width="700" height="350">
  </a>
  <h1>nonebot-plugin-pokesomeone</h1>
</div>

<p align="center">
    <a href="https://pypi.python.org/pypi/nonebot-plugin-pokesomeone">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-pokesomeone" alt="pypi">
    </a>
    <img src="https://img.shields.io/pypi/pyversions/nonebot-plugin-pokesomeone" alt="python">
    <br />
    <a href="https://onebot.dev/">
    <img src="https://img.shields.io/badge/OneBot-v11-black?style=social&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAIVBMVEUAAAAAAAADAwMHBwceHh4UFBQNDQ0ZGRkoKCgvLy8iIiLWSdWYAAAAAXRSTlMAQObYZgAAAQVJREFUSMftlM0RgjAQhV+0ATYK6i1Xb+iMd0qgBEqgBEuwBOxU2QDKsjvojQPvkJ/ZL5sXkgWrFirK4MibYUdE3OR2nEpuKz1/q8CdNxNQgthZCXYVLjyoDQftaKuniHHWRnPh2GCUetR2/9HsMAXyUT4/3UHwtQT2AggSCGKeSAsFnxBIOuAggdh3AKTL7pDuCyABcMb0aQP7aM4AnAbc/wHwA5D2wDHTTe56gIIOUA/4YYV2e1sg713PXdZJAuncdZMAGkAukU9OAn40O849+0ornPwT93rphWF0mgAbauUrEOthlX8Zu7P5A6kZyKCJy75hhw1Mgr9RAUvX7A3csGqZegEdniCx30c3agAAAABJRU5ErkJggg==" alt="onebot">
    <img src="https://img.shields.io/github/last-commit/canxin121//nonebot_plugin_pokesomeone" alt="github">
    </a>
</p>
<div align="left">

## 最新版本号0.1.0

# 使用方法:  

> 假设 nb的CommandStart 为/

则 /戳@某人n(次)   
或 /戳n(次)某人,  
或 /戳   然后根据提示继续  


# env.*配置

| 配置名        | 含义                | 默认值 |
| ------------- | ------------------- | ------ |
| po_max        | 最多戳的次数        | 3      |
| po_black_list | 不可使用的qq或群 号 | [""]   |
| po_white_list | 不可戳的qq号        | [""]   |
