
import py2neo

class GraphIO(object):
  def __init__(self):
    pass

  def relationships(self, word):
    """returns { word_self:count, word_related:count, word_related:count ... }"""
    print 'returning relationships of word', word
    if word==11489:
      return {11489:4, 1413:3, 23523:2, 929:3}
    if word==11491:
      return {11491:5, 89129:4, 9812912:2}

  def appearance(self, word):
    """word appearance. add node if not in db or increment count"""
    print 'appearance of word', word

  def co_appearance(self, word_a, word_b):
    """two words appearing in the same document. create edge if not any, increment one otherwise"""
    print 'co appearance of word', word_a, word_b

if __name__=="__main__":
  db=GraphIO()
  
