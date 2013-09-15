(English follows)

$BF|K\8l$NC18l$N4X78@-$r%0%i%U(BDB$B$G%b%G%k2=$7$^$9(B ($BF|K\8l$G$J$/$F$bF0$/$O$:!K(B

$BJ8>O$N9=B$$rM}2r$9$k>e$G!"C18lF1;N$N4X78@-$rM}2r$9$k$3$H$OHs>o$K=EMW$G$9!#6qBNE*$K$O(B
 - $B4XO"8l!'F1$8%I%-%e%a%s%H$K=P8=$9$k;v$,B?$$C18l!!!JNc!'!V%*%j%s%T%C%/!W$H!VBl@n%/%j%9%F%k!W!K(B
 - $BGI@88l!'F1$8C18l$r4^$`GI@8E*$JC18l!!!JNc!'!V%0%i%U!W$H!V%0%i%U%G!<%?%Y!<%9!W!K(B
 - $BN`8l!';w$?$3$H$r0UL#$9$k$,JL$NC18l!!!JNc!'!V%7%s%W%k!W$H!V4JC1!W!K(B

$B$J$I$,9M$($i$l$^$9!#C18lF1;N$N4X78$,$o$+$k$H!"%5!<%A$d%l%3%a%s%G!<%7%g%s$KHs>o$KM-8z$G$9!#Nc$($P!"%Q%$%=%s$N$3$H$r5$$K$7$F$$$k?M$O(BDropBox$B$K$D$$$F$b5$$K$J$k$@$m$&!"$H$+!"BfIw$N$3$H$r5$$K$7$F$$$?$iN54,$N$3$H$b5$$K$J$k$@$m$&!"$H$+!#(B

$B:#2s$O;d$,%K%e!<%95-;v$+$i<}=8$7$?=q$/5-;v$NC18l%j%9%H$rF~NO%G!<%?$H$7!"$=$3$+$iC18lF1;N$N4XO"@-$rCj=P$7!"%0%i%U%G!<%?%Y!<%9$KF~NO$9$k$3$H$G!"F|K\8l$r2D;k2=$7$F$_$?$$$H;W$$$^$9!#(B

$B6qBNE*$K$O(BNeo4J$B$H$$$&%0%i%U%G!<%?%Y!<%9$,7k9==<<B$7$F$$$k$h$&$J$N$G!"$3$l$N%Q%$%=%s(BAPI$B$r;H$$$?$$$H;W$$$^$9!#(B
 - $B;H$$J}$N%A%e!<%H%j%"%k$O$3$3!'(Bhttp://www.coolgarif.com/brain-food/getting-started-with-neo4j-part2
 - $B<c$7$/$O(BPy2Neo$B$H$$$&(BAPI$B$b$h$5$=$&$G$9!'(Bhttp://blog.safaribooksonline.com/2013/07/23/using-neo4j-from-python/

$B$^$?!"(BNeo4j$B$N4XO"%W%m%8%'%/%H$G!"2D;k2=$r%D!<%k$,$"$k$h$&$J$N$G!"$=$l$r;H$C$F%b%G%k$r8+$J$,$iC5:w$7$F$_$?$$$H;W$$$^$9(B
 - $BNc$($P$3$3$K$"$k%D!<%k$H$+!((Bhttp://www.neo4j.org/develop/visualize

$B:n6HJ,C4(B
 - $BF~NO%G!<%?$NFI$_9~$_(B
 - $BJ,@O$K$h$k4XO"@-$NCj=P(B
 - $B%G!<%?%Y!<%9$X$NF~NO(B
 - $B2D;k2=(B

$B3'$5$s$N;22C$*BT$A$7$F$$$^$9!*(B

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
