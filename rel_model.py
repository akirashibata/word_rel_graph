#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#----------------------------------------------------------------------------
#
#                ,,~~--___---,         Written by
#               /             .~,
#           /  _,~             )         Akira Shibata
#          (_-(~)   ~, ),,,(  /'           for Shiroyagi Corp.
#          Z6  .~`' ||     \ |　　　　
#          /_,/     ||      ||               akira.shibata@shiroyagi.co.jp
#    ~~~~~~~~~~~~~~~W`~~~~~~W`~~~~~~~~~
#                                               @all rights reserverd
#----------------------------------------------------------------------------


import json
import datetime

from shiroyagi_server.DbIo.cursor_retreiver import get_con_cursor
from shiroyagi_server.DbIo.sql_commands import sql_select
from shiroyagi_alg.BOW.bow import BOW 
from shiroyagi_alg.BOW.converter import *

from graph_io import GraphIO

class RelModel(object):
  def __init__(self, feature_db, words_db, graph_db):
    self.feature_db=feature_db
    self.words_db=words_db
    self.graph_db=graph_db
    
  def build(self, n=-1, con_db=True):
    count=0
    for feature in self.feature_db.one_feature(): 
      if n>0 and count>n: break
      count +=1
      keys_processed=[]
      print feature
      for key, val in feature.items():
        if self.words_db.is_noun(key):
          #print 'calling appearance'
          if con_db: self.graph_db.appearance(key)
          #print 'done calling appearance'
          keys_processed.append(key)
          for key2 in keys_processed:
            if not key2==key:
              pass
              #print 'calling co appearance'
              if con_db: self.graph_db.co_appearance(key, key2)       
              #print 'done calling co appearance'

  def get(self, word_id=None, word=None):
    if not word_id and not word: return None
    elif not word_id and word: 
      word_ids=self.words_db.one_id(word)
    else:
      word_ids=list(word_id)
    rels_norm={}
    for word_id in word_ids:
      print 'checking', word_id
      if self.words_db.is_noun(word_id):
        rels=self.graph_db.relationships(word_id)
        try: norm=rels.pop(word_id)
        except: 
          print 'word not found in rels', word_id, rels
          raise
        for wid, val in rels.items():
          rels_norm[self.words_db.one_word(wid)]=float(val)/norm
      else:
        print 'only nouns'
        return None
    return rels_norm

class WordsDB(object):
  def __init__(self, down_to):
    self.n=down_to
    self.con, self.cursor=get_con_cursor()
    self.noun=[]
    self.nonoun=[]

  def _all_words(self):
    l= sql_select(self.cursor, 'DICT_IDF', ['word_id', 'word'],
     conditions='word_id < %s',
     cond_data=(self.n), orderby='word_id', reverse=False, verbose=True)
    self.cursor.close()
    self.con.close()
    return l

  def is_noun(self, word_id):
    return True
    if word_id in self.nonoun: return False
    if word_id in self.noun: return True
    l=sql_select(self.cursor, 'DICT_IDF', ['pos_1'],
     conditions='word_id = %s',
     cond_data=((word_id,)), verbose=True)
    if l[0][0]=='名詞'.decode('utf-8'):
      self.noun.append(word_id)
      return True
    else: 
      self.nonoun.append(word_id)
      return False

  def one_word(self, word_id):
    l= sql_select(self.cursor, 'DICT_IDF', [ 'word'],
     conditions='word_id = %s',
     cond_data=((word_id,)), verbose=True)
    if len(l)>0: return l[0]
    return None

  def one_id(self, word):
    l= sql_select(self.cursor, 'DICT_IDF', [ 'word_id'],
     conditions='word = %s',
     cond_data=((word,)), verbose=True)
    if len(l)>0: return map(lambda x: x[0], l)
    return None

  def dump_to_file(self, filename):
    with open (filename, 'w') as f:
      for word_id, word in self._all_words():
        print word_id, word.encode('utf-8')
        f.write(json.dumps({word_id:word})+'\n')

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
  def main():
    start=datetime.datetime.now()
    interval=datetime.timedelta(days=1)
    start=start-interval
    for i in range(1):
      time_from=start-interval
      print 'building model using data from', time_from, 'to', start
      fdb=FeatureDB(time_from, start, alg_ver='BOW_TF')
      start=time_from

      wdb=WordsDB(10)
      print wdb.one_word(10)
      word='ペン'
      print wdb.one_id(word)

      gdb=GraphIO()

      model=RelModel(fdb, wdb, gdb)
      model.build(2, con_db=False)
      #print model.get(word='ペン')

  import cProfile as profile
  import pstats
  filename = 'profile_stats.stats'
  profile.run('main()', filename)

  stats = pstats.Stats('profile_stats.stats')
  stats.strip_dirs()
  stats.sort_stats('cumulative')
  stats.print_stats()
