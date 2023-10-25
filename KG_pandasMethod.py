from time import time
from py2neo import Graph, Node, Relationship, NodeMatcher
from tqdm import tqdm
import pandas as pd

# 记录开始时间
start_time = time()

if __name__ == '__main__':

    # 连接neo4j数据库
    g = Graph('http://localhost:7474', name='neo4j', password='zwx980818')
    df = pd.read_csv('dataset/triples.csv')
    print("正在获取数据集样本数......")
    # 获取数据集样本数
    csv_row_count = df.shape[0]
    print("获取成功，样本数为:", csv_row_count, "开始构造知识图谱")

    # tqdm为进度条样式
    with tqdm(total=csv_row_count, desc='Graph构建进度') as pbar:
        for i in range(csv_row_count):
            start_node = Node('Person', name=df['head'][i])
            end_node = Node('Person', name=df['tail'][i])
            relation = Relationship(start_node, df['relation'][i], end_node)
            g.merge(start_node, 'Person', 'name')
            g.merge(end_node, 'Person', 'name')
            g.merge(relation)
            pbar.update(1)
    print("Knowledge graph construction is complete,url:http://localhost:7474")
    print("done in %0.3fs" % (time() - start_time))
