# How to reduce the contagious power of 'const' in C++

From [here](https://yinwang0.substack.com/p/const).

For the purpose of optimization and (possibly?) safety, the C++ programming language decided that the users should manually specify 'const' annotations for variables that they know will/should never be modified. While I admit the possible usefulness of this annotation, I often see it misused, and this often results in a contagious effect where unnecessarily many variables and parameters are annotated as 'const'.

In this post, I reason philosophically about the true meaning of the 'const' annotation, and propose some tentative principles regarding the use of it. By following them, I hope to reduce the contagious power of 'const' to the minimum.

First, the rule for 'const' annotations for variables:

> Rule 1\. Declare a variable as 'const' if you want it to be inlined, or you don't want it to be modified.

By this principle, these examples are legitimate:

    const int max = 1000;
    const char* name = "permanent name";

These declarations can be global variables as well as local variables. Declaring them as 'const' can facilitate the inlining opportunities of them, as well as prevent unwanted modifications.

Now we just have one other rule. This one concerns the 'const' annotations on functions:

> <span>Rule 2\. As a function, be self-disciplined about what you</span> _take_<span>, but be relaxed on what you</span> _give_<span>.</span>

This means, put 'const' on the parameters whenever you are sure that you will by no chance modify the input argument, but never put 'const' on the return type unless the compiler asks you to.

<span>The reason behind this may take a little bit of thinking. By putting 'const' on the input parameter, the function is basically declaring: "Whoever passes me this argument, I promise not to modify it." "I'm side-effect free on this parameter." "I'm</span> _pure_ <span>on this parameter."</span>

This is a good thing, because you give the callers of the function more freedom of what they can give you. If you don't declare your "pureness" (on the parameter), some callers may not be able to pass you certain data because they don't want their data to be accidentally modified by you. They need their original values intact, because they are going to use them after you return.

So in general, this is a good thing to do in C++:

      void foo(const char* in);

<span>But there is a catch here: whether you can put 'const' here depends on the function body and all the function calls inside. Whenever you put 'const' on the parameter type, you have to make sure that any functions you call don't modify this parameter either. That is to say this is a</span> _transitive_ <span>property. For example, something like this will not work:</span>

      void foo(const char* in) {
        bar(in);
      }
    void bar(char* in) { ... }

That is because bar may modify its parameter, which is also foo's parameter.

<span>Is this to say that you should declare bar as void bar(</span>_const_ <span>char* in)? It all depends on whether bar actually modifies its argument or not. If it does, then there is no way you can use 'const', consequently you cannot declare foo as taking a</span> _const char either. Then the type of foo should be "void foo(char_ <span>in)", not having the 'const'.</span>

There is no way you should use 'const' in foo then, because the helper bar modifies the data. You have to say this honestly: "I may modify the contents of in, because one of the functions I call modifies it."

This is where it can get painful in C++, because the other functions you call may be written by other people and they may not follow the same principles here. They may not have 'const' on their parameter types even though they haven't modified the parameter in their function body. This is not their fault, because adding those 'const' annotations is so boring. Some automatic inference can certainly be helpful in these cases, but unfortunately inference for 'const' is not provided by C++.

On the other hand, why should you NOT put 'const' on the return type? This is because if you do, then you are basically announcing: "Whoever calls me cannot modify the value that I return."

This like saying this in your will: "I will give my house to my son, but he is not allowed to modify it." Well, the law may give you the right to specify this, but what good can this do to your son? You are limiting the happiness you can provide. More over, can this kind of restriction really be enforced? Who has the time or right to keep an eye on your son and restrict his action on the house? This is just impossible to work.

<span>Coming back to the context of programming, what's the point of not allowing the callers to modify what you GIVE them? By returning, you are giving up control of the return value to the caller. It should be up to the caller, and not you, to decide whether to modify the return value or not. Even if you put 'const' annotations in the return type, they are usually ignored by the callers. They just use a </span>_const_cast_<span> whenever the 'const' gets in their way. This makes the 'const' annotation on return types virtually useless.</span>

If you put 'const' on the return type and the callers respect it, then it will contaminate the whole data path wherever the return value goes. This is nasty and unnecessary.

So in general, this is not a good thing to do:

      const char* bar();

Because your caller would have to be like this:

    void baz() {
      const char* ret = bar();
      bizaar(ret);
    }

And the receiver of the return value (bizaar) must be defined as something like:

      void bizaar(const char* in) {
        bizaar2(in);
      }

And now bizaar2 needs to be declared as:

      void bizaar2(const char* in);

And so on... You see how the contagion started? Because bar() returned a const value, which is unnecessarily restrictive. So in general, it is not a good idea to return 'const'.

I'll leave this as an thought exercise: When can we reasonably use 'const' on the return value?
