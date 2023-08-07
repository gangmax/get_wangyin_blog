# Back to the future of databases

From [here](https://yinwang1.substack.com/p/database).

Why do we need databases? What a stupid question. I already heard some people say. But it is a legitimate question, and here is an answer that not many people know.

<span>First of all, why can't we just write programs that operate on objects? The answer is, obviously, we don't have enough memory to hold all the data. But why can't we just swap out the objects to disk and load them back when needed? The answer is yes we can, but not in Unix, because Unix manages memory as</span> _pages_<span>, not as</span> _objects_<span>. There are systems who lived before Unix that manage memory as objects, and perform </span>_object-granularity persistence_<span>. That is a feature ahead of its time, and is until today far more advanced than the current state-of-the-art. Here are some pictures of such systems:</span>

[IBM System/38](http://en.wikipedia.org/wiki/IBM_System/38)

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd886afed-1775-4b45-a742-b789d9cb0766_200x150.jpeg "system-38")

[Lisp Machine](http://en.wikipedia.org/wiki/Lisp_machine)

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F30c9d034-2e54-4fbd-a893-fa9600888ced_160x211.jpeg "lisp-machine")

[Oberon](http://www.ics.uci.edu/~franz/Site/pubs-pdf/BC03.pdf)

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F081fb49f-76c4-4aef-84db-fc01b8c9c01b_200x151.png "Oberon")

Those systems don't really need databases (in its usual sense). Data integration was seamless and transparent to the programmer. You don't need to know the existence of a "disk", a "file system", or a "database". You can just pretend that you can allocate infinite number of objects and work on them in the most natural way. Unfortunately most of those systems were either terribly expensive or had problems in other aspects of their design. Finally, they seemed to have died out.

Good ideas never die. Nobody uses those systems today, but this is not to say that there is nothing we can learn from their design. On the contrary, some of their ways are far superior than the current state-of-the-art of Unix-based systems. Unix will never reach that level of elegance and power.

But any how, Unix rules the world. We can live with it, but it is just mediocre. Please don't believe everything that the modern Operating Systems books tell you. Sometimes you have to look further into the past for the future. As Einstein said, "Nothing is more needed to overcome the modernist's snobbishness."

Unix used to be free, but you get what you pay for. Although there is a thing called "virtual memory", your programs can't just allocate objects and then operate on them without any knowledge about the "file system". Nothing works out-of-the-box in Unix. In fact it is far from that. Unix and its "philosophy" is a constant source of trouble. It is more like a "non-operating system" than an "operating system". It leaves too much work for you to do, and leaves more than enough rope to hang yourself.

Unix builds its reputation and authority by blaming the users. If you don't know how to use me, you are an idiot! This is the same trick that the weavers played on the emperor: If you can't see the clothes, you are either stupid or incompetent. What a powerful way to cover the ass of any crap!

Unix's incapability is why people "invented" databases. The combination "Unix + databases" is supposed to be a cheap replacement for those advanced systems where programs don't need to know the existence of such a second-level data storage layer. But because of some irreparable design issues, Unix still can't achieve that even with the help of databases. The databases, until today, still relies on Unix's low-tech mechanisms such as memory mapped files to store data, which causes complications and performance issues.

<span>However, databases were somehow considered a big thing, and people who made it became the richest men in the world. Consequently, you have to take database classes if you want a computer science degree. So here is an</span> _ultimate cheat sheet_ <span>for those who really want to know what a database is. You will not need to sit through a semester's course if you remember the few things that I put below. Trust me, many students got A+'s because I told them this ;-)</span>

<span>Every "</span>_row_<span>" in a database "</span>_table_<span>" is a data structure, much like a "struct" in C, or a "class" in Java. A table is then an array (or list) of such data structures. The "</span>_keys_<span>" of a database table are in essence "</span>_persistent memory addresses"_<span>. When serializing an object, we can't just put the memory address of an object onto disk, because the address may not be the same when the object is reloaded into memory. This is why we need "keys". In a sense, "keys" are a more general notion than "addresses" -- addresses are just keys that are integers.</span>

<span>There is a white lie in the above paragraph - I didn't mention that there is some redundancy in a database table in comparison to a serialized data structure. Some data is duplicated across multiple rows because a RDBMS table row has fixed width, so it can't store variable length data such as arrays. What can you do then? By recognizing that the table is the only thing that can "grow" in a relational database, an obvious solution is to turn the array 90 degrees clockwise, and make each element a row in</span> _another table_<span>! But how do you connect from where the array is originated from? You add the key of the object to</span> _each_ <span>row of this new "array table". See how the key is duplicated? This is why people "invented" column-based databases (such as Vertica, HBase etc) for "compressing" these keys. But what they achieved was essentially making the tables slightly closer to the format of serialized data structures.</span>

You create the problem, and then you solve it. And you call this two inventions.

<span>Keys are </span>_persistent pointers_<span>. Whenever you need to</span> _dereference_ <span>a pointer, you do a "</span>_join_<span>" in the database, so "join" is equivalent to "following pointers".</span>

<span>A database "</span>_schema_<span>" is in essence a "structure type", like the struct definition in C. For example, the schema created by the following SQL statement</span>

    CREATE TABLE Students ( sid CHAR(20),
                            name CHAR(20),
                            login CHAR(20),
                            age INTEGER,
                            gpa REAL )

is equivalent to the C struct

    struct student {
      char* sid;
      char* name;
      char* login;
      int age;
      double gpa;
    }

(Note that I use a SQL declaration here just because I don't want to draw a picture of the schema. This equivalence of a relational schema with a structure type has nothing to do with SQL.)

That's almost the whole story. You have addresses, pointers, dereference operation, structure types, arrays/lists of structures, so now you can implement things like linked lists, graphs etc. With them, you can implement some complicated algorithms such as A* search in a database. You just need to take a data structure class, and then translate what you learned there into a database language like SQL.

But SQL is a crappy language. It wasn't designed for programmers. It was designed for manual input by human operators (usually non-technical people like accountants). You type in a "query", and the computer prints out a "response". That is why it is called a "query language". This language does its job for human operators, but it was then abused beyond its capabilities. It was interfaced with computer programs to write serious programs. I doubt if those people knew what they were doing, but it just happened, like many other silly things. There are just so many things you can't express in that language. The result is a dumb and fragile system held together by band-aids. You have to be very careful otherwise you lose blood.

If you really want to learn SQL, here is the cheat sheet for it:

The query

    SELECT Book.title
     FROM Book
     WHERE price > 100

is equivalent to the Lisp expression

    (map (lambda (b) b.title)
         (filter (lambda (p) (> p 100)) Book)

This program is then sent to the "database engine" for execution. That is, we move the program to the data, instead of loading the data to the program. And that's also the principle behind MapReduce. Have you noticed how easy this can be done with Lisp? You just send the code to the interpreters running on remote machines!

The problem with SQL is that you need yet another layer of language before programs can operate the database. SQL is a weak and quirky language. It is not Turing-complete and at some places it doesn't even "compose". You need to combine it with a decent language before you can write serious programs. Your programs send SQL commands to the database to store and load data, just like a human operator would do. This is a very low-tech way of data integration. It is error-prone, inefficient and subject to security risks such as "SQL injection".

Indeed, there is a "good component" in SQL, because it has some "relational programming" features. However, the other word for "relational programming" is "logic programming", where languages like Prolog and Datalog excel. They are both more expressive and more elegant than SQL. Considering that Prolog and Datalog appeared much earlier than SQL (1972, 1977 v.s. 1986), I would say that SQL is a step backwards.

Maybe you have seen, for some weird reasons we are still in the Dark Ages of computer programming. We are not supposed to be here since better designed systems already existed. It would be foolish to dismiss them as failures. They are just ahead of their times. By looking to the past, we see a way back to the future.
