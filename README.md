# KG

这是一个生成知识图谱的小程序，并且有两种方法进行实现，具体来说是使用两种不同的包,
目前只支持csv数据集(三列,startNode,relation,endNode)的简单生成，后续会不断更新改进以适应更多数据集

## Environments,Default installation of the latest version
* py2neo
* csv
* pandas
* tqdm
* time

## About KG_csvMethod.py
需要统一csv文件内的列顺序，无需统一列头名称

### dataset(.csv)
* column 1:start node
* column 2:end node
* column 3:relation

  请将csv文件内的数据改为上述格式（无需修改列头名称）
  Then you can run:
  `python KG_csvMethod.py`

## About KG_pandasMethod.py
需要统一csv文件内的列头名称，无需统一列顺序

### dataset(.csv)
* column 1.name = head
* column 2.name = tail
* column 3.name = relation

  请将csv文件内的列头名称改为上述格式（无需修改列顺序）
  Then you can run:
  `python KG_pandasMethod.py`