
import py2neo

class GraphIO(object):
  def __init__(self):
    pass

  def relationships(self, word):
    """returns { word_self:count, word_related:count, word_related:count ... }"""

  def appearance(self, word):
    """word appearance. add node if not in db or increment count"""

  def co_appearance(self, word_a, word_b):
    """two words appearing in the same document. create edge if not any, increment one otherwise"""


if __name__=="__main__":
  db=GraphIO()
  
