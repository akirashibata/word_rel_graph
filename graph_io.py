
from py2neo import neo4j
from py2neo import node, rel

class GraphIO(object):
  def __init__(self):
    self.graph_db = neo4j.GraphDatabaseService(neo4j.DEFAULT_URI)
    self.word = self.graph_db.get_or_create_index(neo4j.Node, "Word")
    self.nodes = {};
    pass

  def node_for_word(self, wid):
    node = self.nodes.get(wid)
    if not node:
      n = self.word.get("wid", str(wid))
      if len(n) > 0:
        node = n[0]
        self.nodes[wid] = node
    return node
  
  def relationships(self, wid):
    """returns { word_self:count, word_related:count, word_related:count ... }"""
    node = self.node_for_word(wid)
    print node.get_properties(), node

  def appearance(self, wid):
    """word appearance. add node if not in db or increment count"""
    node = self.node_for_word(wid)
    if not node:
      node = self.word.get_or_create("wid", str(wid), {"wid":wid, "count":1})
      self.nodes[wid] = node
    node["count"] += 1

  def co_appearance(self, wid_a, wid_b):
    """two words appearing in the same document. create edge if not any, increment one otherwise"""
    n_a = self.node_for_word(wid_a)
    n_b = self.node_for_word(wid_b)
    r = self.graph_db.match(start_node=n_a, end_node=n_b, bidirectional=True)
    if len(r) == 0:
      r0, r1 = self.graph_db.create(
                rel(n_a, "COAPPEARS", n_b, count=0),
                rel(n_b, "COAPPEARS", n_a, count=0))
      r = [r0, r1]
      
    r[0]["count"] += 1
    r[1]["count"] += 1

if __name__=="__main__":
  db=GraphIO()
  
  db.appearance(123)
  db.appearance(456)
  db.appearance(789)
  
  db.co_appearance(123, 456)
  db.co_appearance(456, 789)
  
  db.co_appearance(123, 456)
  db.co_appearance(123, 789)
  
  db.relationships(123)
  db.relationships(456)
  db.relationships(789)
  
