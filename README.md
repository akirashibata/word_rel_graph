(English follows)

日本語の単語の関係性をグラフDBでモデル化します (日本語でなくても動くはず）

文章の構造を理解する上で、単語同士の関係性を理解することは非常に重要です。具体的には
 - 関連語：同じドキュメントに出現する事が多い単語　（例：「オリンピック」と「滝川クリステル」）
 - 派生語：同じ単語を含む派生的な単語　（例：「グラフ」と「グラフデータベース」）
 - 類語：似たことを意味するが別の単語　（例：「シンプル」と「簡単」）

などが考えられます。単語同士の関係がわかると、サーチやレコメンデーションに非常に有効です。例えば、パイソンのことを気にしている人はDropBoxについても気になるだろう、とか、台風のことを気にしていたら竜巻のことも気になるだろう、とか。

今回は私がニュース記事から収集した書く記事の単語リストを入力データとし、そこから単語同士の関連性を抽出し、グラフデータベースに入力することで、日本語を可視化してみたいと思います。

具体的にはNeo4Jというグラフデータベースが結構充実しているようなので、これのパイソンAPIを使いたいと思います。
 - 使い方のチュートリアルはここ：http://www.coolgarif.com/brain-food/getting-started-with-neo4j-part2
 - 若しくはPy2NeoというAPIもよさそうです：http://blog.safaribooksonline.com/2013/07/23/using-neo4j-from-python/

また、Neo4jの関連プロジェクトで、可視化をツールがあるようなので、それを使ってモデルを見ながら探索してみたいと思います
 - 例えばここにあるツールとか；http://www.neo4j.org/develop/visualize

作業分担
 - 入力データの読み込み
 - 分析による関連性の抽出
 - データベースへの入力
 - 可視化

皆さんの参加お待ちしています！

====
A graph DB modeling engine for Japanese words (or in fact should work with any language)

It is rather important to understand relationships between words in a language. In particular
 - Related words: words that are likely to appear in the same document as the given word (e.g. "Olympic" and "Takigawa Crystel"
 - Derived words: words that are derived from a given word (e.g. "graph" and "graph-database")
 - Synonym: words that have the same meaning as a given words (e.g. "simple" and "easy")

are some of the examples. Once we know these relationships, it is highly practical against search and recommendation applications. For example, if someone likes to know about Python, then the person may also be interested in DropBox. If a person likes to know about typhoon, then he/she may also like to know about tornados.

At this time I would like to propose to use the word list data that I extracted from Japanese news articles. By putting in the relationships into Graph DB, we will be able to visualize Japanese language to some extent.

From my initial research, Neo4j appears to be a prominent graph DB and has a few options as to python API
 - "Embedded" python api as described here: http://www.coolgarif.com/brain-food/getting-started-with-neo4j-part2
 - Py2Neo as also seems attractive: http://blog.safaribooksonline.com/2013/07/23/using-neo4j-from-python/

Also, there are projects related to Neo4j that readily enables the visualization of graph DBs, which would be fun to try out:
 - such as those in  http://www.neo4j.org/develop/visualize

Proposed work breakdown:
 - reading in input data
 - extraction of relationships
 - input into graph DB
 - visualization

Looking forward to working with you!
