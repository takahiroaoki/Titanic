# titanic

## Overview
In this project, [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview), the famous dataset for machine-learning was analyzed.

## Requirement
- Windows 10
- [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop) 4.2.0
- VSCode with the extention of Remote Development 0.21.0

## How to use
1. Open the "titanic" directory (i.e. this project itself) in a container through Remote Development extention of VSCode.
2. Open ./main.ipynb and run it from top to bottom.

## Frequent Error
### Could not find renderer
Sometimes we are encountered by the following error.
```
Error loading preloads: Could not find renderer
```
This error would be from Jupyter extention of VSCode.
So, uninstall the Jupyter extention and install another version of it.
In my case, it goes well by 'v2021.11.1001480274'

## Reference
- [東京大学のデータサイエンティスト育成講座](https://www.amazon.co.jp/%E6%9D%B1%E4%BA%AC%E5%A4%A7%E5%AD%A6%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E3%82%B5%E3%82%A4%E3%82%A8%E3%83%B3%E3%83%86%E3%82%A3%E3%82%B9%E3%83%88%E8%82%B2%E6%88%90%E8%AC%9B%E5%BA%A7-Python%E3%81%A7%E6%89%8B%E3%82%92%E5%8B%95%E3%81%8B%E3%81%97%E3%81%A6%E5%AD%A6%E3%81%B6%E3%83%87%E2%80%95%E3%82%BF%E5%88%86%E6%9E%90-%E5%A1%9A%E6%9C%AC%E9%82%A6%E5%B0%8A/dp/4839965250/ref=sr_1_1?keywords=%E3%83%87%E3%83%BC%E3%82%BF%E3%82%B5%E3%82%A4%E3%82%A8%E3%83%B3%E3%83%86%E3%82%A3%E3%82%B9%E3%83%88%E8%82%B2%E6%88%90%E8%AC%9B%E5%BA%A7&qid=1639975123&sprefix=%E3%83%87%E3%83%BC%E3%82%BF%E3%82%B5%E3%82%A4%E3%82%A8%E3%83%B3%E3%83%86%E3%82%A3%E3%82%B9%E3%83%88%2Caps%2C217&sr=8-1)
