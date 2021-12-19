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