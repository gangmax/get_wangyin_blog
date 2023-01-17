 [<div class="image2-inset"><picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F073c3daa-a238-4dd0-8500-219696b02626_300x225.png 424w, https://substackcdn.com/image/fetch/w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F073c3daa-a238-4dd0-8500-219696b02626_300x225.png 848w, https://substackcdn.com/image/fetch/w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F073c3daa-a238-4dd0-8500-219696b02626_300x225.png 1272w, https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F073c3daa-a238-4dd0-8500-219696b02626_300x225.png 1456w" sizes="100vw">![null](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F073c3daa-a238-4dd0-8500-219696b02626_300x225.png "null")</picture></div>](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F073c3daa-a238-4dd0-8500-219696b02626_300x225.png) 

<span>The null pointer is considered to be a "</span>[billion-dollar mistake](http://www.infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare)<span>". I have been wondering why there is such a notion until I saw the </span>[video](http://www.infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare) <span>where Tony Hoare claims it to be his mistake. In fact, he didn't really say that null pointer should not be used.</span>

<span>From this video, you can see that </span>_introducing_ <span>null reference is not really a mistake. On the contrary, null references are helpful and sometimes indispensable. The mistake is not in the</span> _existence_<span> of the null pointers, but in how the type system treats them. Unfortunately, most languages (C++, Java, C#, ...) don't treat them correctly.</span>

<span>Every class type</span> `A` <span>of Java is in fact a</span> _union type_ <span></span> `{A, null}`<span>, because you can use null where an A object is expected. {A, null} is almost equivalent to the Maybe type of Haskell, where null corresponds to</span> `Nothing` <span>of Haskell. So the trouble really is that an annotation like</span> `{String, null}` <span>should be distinguished from</span>`String`<span>, so that it will be clear whether null can possibly be its value.</span>

<span>Unfortunately most languages don't provide a convenient union type that you can put</span> `String` <span>and</span> `null` <span>together (</span>[Typed Racket](http://docs.racket-lang.org/ts-guide/) <span>is an exception). If Java is to have union types, we can say something like:</span>

    {String, null} find1() {
      if (...) {
        return "okay";
      } else {
        return null;
      }
    }

<span>This is saying:</span> `find1`<span>may return a name which is a</span> `String`<span>, or it may return</span> _nothing_<span>. Because of the union type </span>`{String, null}`<span>, the type system knows that you should check for null when you have called</span> `find(),`<span> so it will force you to write a null check:</span>

    String s = find();  
    if (s != null) {
      x = s.length();
    }

In comparison, if we define a slightly different function find2, with a different return type:

    String find2() {
        ...
        return "okay";
    }

From the return type we know that find2 will never return null, so the type checker can let you you use the String without checking:

    String s = find();
    x = s.length();
