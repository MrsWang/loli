# encoding: utf-8
class Tree():
  def __init__(self, data):
    self.data = data
    self.root_node = []
    self.common_node = {}
    self.node_name = {}
    self.other = {}
    self.tree= []
    self.node_name = {}
    # print self.data

  def find_root_node(self, father_id):
    # 查找根节点
    # 返回 根节点列表
    for node in self.data:
      # print father_id
      if node[father_id] is None:
        self.root_node.append(node)

  def find_common_node(self, father_id):
    # """
    # 寻找同级的对象
    # :return: 共同的父节点字典
    # """
    for node in self.data:
      father = node.get(father_id)
      # print father
      # 排除根节点情况
      if father is not None:
        # 如果父节点ID不在字典中则添加到字典中
        if father not in self.common_node:
          self.common_node[father] = []
        self.common_node[father].append(node)

    # print self.common_node
    return self.common_node

  def find_child(self, primary_id, father_id, child_node, node, args):
    # 获取共同父节点字典的子节点数据

    # print "primary_id:"
    # print primary_id
    # print "father_id:"
    print father_id

    child_list = self.common_node.get(father_id, [])

    # print child_list
    for item in child_list:
      # 生成其他字段
      for i in args:
        self.other[i] = item[i]

      self.other[primary_id] = item[primary_id]
      self.other['children'] = []
      # print "other-------"
      # print self.other
      # 生成字典
      base = dict(self.other)
      self.other.clear()
      # print base

      # print primary_id
      # print item[primary_id]

      # 遍历查询子节点
      self.find_child(primary_id, item[primary_id], base[node], node, args)
      # print "-----"
      # print child_node
      # print "====="
      # print base
      # 添加到列表
      child_node.append(base)


  def build_tree(self, primary_id, father_id, node, *args):
    self.find_root_node(father_id)
    self.find_common_node(father_id)
    self.node_name[node] = []
    # print self.node_name

    for root in self.root_node:
      # 生成其他字段
      for i in args:
        self.other[i] = root[i]

      self.other[primary_id] = root[primary_id]
      self.other[node] = []

      # print self.other

      base = dict(self.other)
      self.other.clear()

      # print base[primary_id]

      print "=-=-=-="
      print node
      print base[node]

      # 遍历查询子节点
      self.find_child(primary_id, base[primary_id], base[node], node, args)

      self.tree.append(base)


    print "tree:"
    print self.tree

    return self.tree


data = [
  {"a_id": 1, "parent_id": None, "name": "01"},
  {"a_id": 2, "parent_id": 1, "name": "0101"},
  {"a_id": 3, "parent_id": 1, "name": "0102"},
  {"a_id": 4, "parent_id": 1, "name": "0103"},
  {"a_id": 5, "parent_id": 2, "name": "010101"},
  {"a_id": 6, "parent_id": 2, "name": "010102"},
  {"a_id": 7, "parent_id": 2, "name": "010103"},
  {"a_id": 8, "parent_id": 3, "name": "010201"},
  {"a_id": 9, "parent_id": 4, "name": "010301"},
  {"a_id": 10, "parent_id": 9, "name": "01030101"},
  {"a_id": 11, "parent_id": 9, "name": "01030102"},
]

new_tree = Tree(data=data)

result = new_tree.build_tree('a_id', 'parent_id', 'children', 'name')