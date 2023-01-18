#Indentation-based syntax considered troublesome

From [here](https://yinwang1.substack.com/p/layout).

<span>Although the idea of</span> [layout syntax](http://en.wikipedia.org/wiki/Off-side_rule)<span>---using whitespace characters to delimit blocks---has been promoted by several languages (notably Python and Haskell), I think this kind of syntax brings more trouble than benefits.</span>

### It takes just one keystroke to produce a serious bug

In most languages a program's format is determined by its meaning, but in a language with layout syntax, its meaning is determined by the format. This makes programs in layout syntax fragile because a tiny change in format could result in a serious error. For example, consider these two Python programs:

> # correct definition
>     def member(x, ls):
>         for y in ls:
>             if x == y:
>                 return True
>         return False         # correct indentation
> 
>     # incorrect definition
>     def member(x, ls):
>         for y in ls:
>             if x == y:
>                 return True
>             return False     # incorrect indentation

The second definition has been "derived" from the first by an inadvertent TAB key, which indented the return statement one more level to the right. While the two definitions differ only in one indentation, they produce totally different results.

Although this is just a minimal example, the bug may take quite some time to show up and be fixed. In order to prevent this kind of bugs from happening, I often find myself moving the cursor up-and-down in a straight line to check the alignment of the statements.

Let's see why this bug cannot happen in a language which does not use layout syntax. We now invent an alternative syntax for Python, so that the pervious program looks like:

> def member(x, ls) {
>         for y in ls {
>             if x == y {
>                 return True
>             }
>         }
>         return False
>     }

Given the correct definition, can you imagine how you could reproduce the bug with just one keystroke? It is almost impossible. To see why:

1.  The return statement can never get into the loop with a change in indentation.

2.  <span>It takes at least</span> _two edits_ <span>and</span> _one movement_ <span>in the editor to move the return statement into the loop. There are two alternatives to choose from:</span>

    *   <span>Cut</span> `return False`<span>. Move the cursor into the closing curly brace of the for-loop. Paste.</span>

    *   <span>Delete the closing curly brace of the for-loop. Move the cursor beyond</span> `return False`<span>. Insert an closing curly brace.</span>

<span>Either way, you must be</span> _deliberate_ <span>and</span> _precise_ <span>in order to reproduce the bug. Otherwise the parser would have complained (for example, if you just delete a closing curly brace).</span>

However, the situation is very different with layout syntax, where one TAB key press produces the same amount of change as the above three operations. The change happens quickly and the program remains grammatically correct, obscuring the presence of a bug.

The situation is a little better for Haskell, because incorrect indentations often cause type errors and the programmer will be alerted, but fundamentally the problem still exists.

### Unconvincing advantages

It is often claimed that layout syntax has the following advantages over curly braces:

*   Your programs become a lot shorter because less curly braces are used.

*   You write less clutter such as curly braces and semicolons, and that beautifies your code.

I found that neither of the two advantages convincing. For the first part, Python and Haskell programs are indeed several times shorter than equivalent Java or C programs, but this cannot really be creditted to layout syntax.

We need to have some blank lines even in a Python or Haskell program, between definitions and sometimes in the middle of a block. The blank lines naturally denote groups of statements. So if we count the number of additional lines introduced by curly braces, we will find that there aren't many. Curly braces also naturally denote statement groups, so not only they don't look bad, they are helpful.

<span>In Python and Haskell, it is the</span> _semantic_ <span>features (pattern matching, first-class functions etc.) that make the programs short, not layout syntax. If we had an alternative syntax of Java which uses layout, then Java programs would still be several times longer than equivalent Scala programs. Java programs are longer not because they use curly braces, but because they don't have things such as first-class functions, so they have to use some tedious design patterns.</span>

Second, layout syntax does not really save "clutter". Even in a language with layout syntax, we may still need to write almost the same amount of (if not more) clutter. The following is a random piece of code taken from the current release of GHC. We can still see lots of curly braces and semicolons in it. I guess layout syntax actually caused trouble, so the authors of GHC decided that they will just write curly braces.

> tcInstanceMethodBody skol_info tyvars dfun_ev_vars
>                          meth_id local_meth_id
>                  meth_sig_fn specs
>                          (L loc bind)
>       = do  {       -- Typecheck the binding, first extending the envt
>             -- so that when tcInstSig looks up the local_meth_id to find
>             -- its signature, we'll find it in the environment
>               let lm_bind = L loc (bind { fun_id = L loc (idName local_meth_id) })
>                                  -- Substitute the local_meth_name for the binder
>                      -- NB: the binding is always a FunBind
>     ; (ev_binds, (tc_bind, _))
>                    <- checkConstraints skol_info tyvars dfun_ev_vars $
>               tcExtendIdEnv [local_meth_id] $
>                   tcPolyBinds TopLevel meth_sig_fn no_prag_fn
>                      NonRecursive NonRecursive
>                      [lm_bind]
>     ; let full_bind = AbsBinds { abs_tvs = tyvars, abs_ev_vars = dfun_ev_vars
>                                        , abs_exports = [(tyvars, meth_id, local_meth_id, specs)]
>                                        , abs_ev_binds = ev_binds
>                                        , abs_binds = tc_bind }
>     ; return (L loc full_bind) }
>       where
>         no_prag_fn  _ = []      -- No pragmas for local_meth_id;
>                             -- they are all for meth_id

### Better ways to save clutter

Even if we do hate curly braces, there are better ways to reduce or even completely eliminate them. For a trivial "solution", we could just use a dim color for curly braces and semicolons in the editor, so that they are less noticeable.

<span>Better still, we could use a</span> _structural editor_ <span>that lets us manipulate the AST (abstract syntax tree) directly. Those editors could provide several options of denoting blocks. You can switch between colored blocks, curly braces, or nothing at all. You can switch the look of your code at any time, instantly. People have implemented such editors, for example</span> [this editor](http://blogs.msdn.com/b/kirillosenkov/archive/2009/09/08/first-videos-of-the-structured-editor-prototype.aspx) <span>designed by Kirill Osenkov.</span>

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1a9082d-52ad-4b1b-abe4-2a0802a500de_794x720.png "Structural Editor by Kirill Osenkov")

### Re-indentation hassle

<span>In a language that doesn't use layout syntax (Java, C, Scheme, ...), no re-indentation is really needed when the code changes. The programmer can move a block of code by a simple copy-and-paste and continue solving the real problem. Re-indentation can always be done later and can be done</span> _automatically_<span>.</span>

<span>But in a language that uses layout syntax, re-indentation is</span> _mandatory_<span>, and worse, it can only be done</span> _manually_<span>. Layout syntax completely disables any editor's auto-indent function. One may think that we might be able to invent a smarter editor that can auto-indent code for those languages. This is simply impossible. This is evident in the analysis of the above example. The two programs differ only in indentation, but they have completely different meanings. Both are grammatically correct programs and the editor has no way to tell which is the one you want unless it can read your mind.</span>

Some people say that because those languages have advanced semantics, programs are so short that we don't need to re-indent code very often. But experiences prove to me that the need for changing and rewriting code can never be eliminated. Writing code is like writing a book, you can always find pieces that need change or even complete rewrite. Usually changes in the following category will cause re-indentation:

*   Scope changes. There are lots of examples in this category: lifting an internal function to top level or push a top-level function into an internal function, surrounding a block with let-bindings, loops, conditional statements, try-except or lifting a block out of them, factoring out duplicated patterns, lifting "invariant code" out of recursion, ... to name a few. These will necessarily change the indentation of a block of code, and each line needs to be re-indented.

*   <span>Align code. For example in Haskell, when we align the arrows (->) of a case expression or the equal signs (=) of a function definition, we will notice that we have to re-indent most of the right-hand-sides, because they often contain multi-line expressions but the editors (for example, Emacs'</span> `align-regexp` <span>function) only move the lines that contains the arrows or equal signs.</span>

*   Renaming. We seldom choose the best names on the first shot, and good names make programs self-explanatory, so renaming is a very important and commonplace action. But in the following simple Haskell program, if we change the name from "helloworld" to "hello" and don't re-indent the rest of the lines, we will get a parse error.

    > helloworld z = let x = 1
    >                        y = 2 in
    >                      x+y+z

    Because the code becomes the following after the renaming, and the second line will no longer be aligned to "x = ...", and that confuses the parser.

    > hello z = let x = 1
    >                        y = 2 in
    >                      x+y+z

    <span>A similar thing happens when we lengthen the name to something like "helloworldcup". Try it yourself. From this example, I hope you see how simple things are made frustratingly complicated by layout syntax. If you haven't been convinced, try adding more lines to the above</span> `let` <span>expression.</span>

The interruption from re-indenting code is usually not just one or two seconds, but often tens of seconds, even minutes. The programmer has to put down real problems at hand and turn to the mind-dead re-indenting job. This disrupts the "flow", which is essential for producing creative and elegant code.

### Layout syntax considered harmful

I believe that syntax, although an important aspect of natural languages, should not play a significant role in programming languages. It has already brought us too much trouble and frustration and wasted too much of our energy.

Syntax has prevented lots of new design possibilities in programming languages. You may have heard language designers say: "Hey this is a nice feature, but the syntax of my language hasn't any room left for it." Layout syntax pushes to this direction even more. It forces us to consciously and constantly think about syntax, drawing our attention away from semantics design. It poses certain constraints on how code must be formatted, and makes a language even less extensible. Thus I think layout syntax is the most troublesome type of syntax.
