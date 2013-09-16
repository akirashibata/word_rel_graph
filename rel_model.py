
import json
import datetime

from shiroyagi_server.DbIo.cursor_retreiver import get_con_cursor
from shiroyagi_server.DbIo.sql_commands import sql_select
from shiroyagi_alg.BOW.bow import BOW 
from shiroyagi_alg.BOW.converter import *

from graph_io import relationships, appearance, co_appearance

class RelModel(object):
  def __init__(self):
    pass

class FeatureDB(object):
  def __init__(self, date_from, date_to, alg_ver='BOW_TF'):
    self.date_from=date_from
    self.date_to=date_to
    self.alg_ver=alg_ver

  def _all_features(self):
    con, cursor=get_con_cursor()
    l= sql_select(cursor, 'FEATURE_RSS', ['contents_id', 'date_published', 'feature', 'body_length'], 
     conditions='WHERE date_published >= %s AND date_published<= %s AND body_length >= %s AND alg_ver=%s',
     cond_data=(self.date_from, self.date_to, 500, self.alg_ver), orderby='date_published', verbose=True)
    cursor.close()
    con.close()
    return l
  
  def one_feature(self):
    for feature in self._all_features():
      yield self._bow_from_feature(feature[2]).feature

  def _bow_from_feature(self, feature):
    b=BOW(feature, converter=TFConverter())
    return b

  def dump_to_file(self, filename):
    with open(filename, 'w') as f:
      for feature in self._all_features():
        data= {'contents_id':feature[0], 'date_published':feature[1].strftime("%Y %m/%d %H:%M"), 'word_count':self._bow_from_feature(feature[2]).feature, 'length':feature[3]}
        print json.dumps(data)
        f.write(json.dumps(data)+'\n')
 
if __name__=='__main__':
  filename='news.json'
  db=FeatureDB(datetime.datetime(2013, 9, 16, 0, 0), datetime.datetime.now(), alg_ver='BOW_TF')
  for i in db.one_feature(): print i
