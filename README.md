# Shopee Crawler

使用 Python 3.11

## 需求

写一个爬虫将这个店的所有商品爬下来， 存储为 Excel 文件。要求有以下数据：

1. 商品名
2. 商品最高价格
3. 商品最低价格
4. 商品首图 URL
5. Ratings

注意反爬机制。如需要 IP 代理池，我们可以提供。

店铺地址：https://shopee.co.th/ethan1177

## 基本实现

爬虫使用 playwright 模拟浏览器行为，以应对基本的反爬措施，分为两个部分：

1. `get_product_urls.py` 用以获取商品 URL 列表，并保存在 `product_urls.txt`
2. `get_product_info.py` 用以获取商品数据，并保存在 `product_info.xlsx`

## 下一步工作

1. 完善爬取失败的处理机制

目前爬虫只能针对 timeout 错误进行处理，并将失败的 URL 保存到 `crawl_error.txt`。下一步需捕获更多类型的错误（如自动跳转到 login 页面），并增加自动重试机制。

2. 增加代理池

目前爬取数量较少，并未触发针对 IP 地址的反爬，下一步需要增加 [HTTP Proxy](https://playwright.dev/python/docs/network#http-proxy)，以应对该类型反爬措施。

3. 优化爬取速度

有两点可以优化：

1. 使用 headless=True 参数，能够减少资源占用。但是，仅改这一个参数会触发反爬，可能需要配置下 header。

2. 目前每次爬取一个页面，都需要重启一下 Brower。接下来可以考虑在一个 Brower Context 下爬取多个页面，以增加爬取速度。
