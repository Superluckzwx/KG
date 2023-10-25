from time import time
import csv
from py2neo import Graph, Node, Relationship, NodeMatcher
from tqdm import tqdm

start_time = time()


def get_csv_rowCount(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        temp_file = csv.reader(f)
        # 相当于1执行了reader次，然后将reader次数的1相加，就是csv文件的行数
        row_count = sum(1 for row in temp_file)
        return row_count - 1


if __name__ == '__main__':
    g = Graph('http://localhost:7474', name='neo4j', password='zwx980818')
    print("正在获取数据集样本数......")
    csv_row_count = get_csv_rowCount('dataset/triples.csv')
    print("获取成功，样本数为:", csv_row_count, "开始构造知识图谱")
    with open('dataset/triples.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        with tqdm(total=csv_row_count, desc='MAP构造进度') as pbar:
            for item in reader:
                # 跳过第一行
                if reader.line_num == 1:
                    continue
                start_node = Node('Person', name=item[0])
                end_node = Node('Person', name=item[1])
                relation = Relationship(start_node, item[3], end_node)
                g.merge(start_node, 'Person', 'name')
                g.merge(end_node, 'Person', 'name')
                g.merge(relation)
                pbar.update(1)
    print("Knowledge graph construction is complete,url:http://localhost:7474")
    print("done in %0.3fs" % (time() - start_time))
