# 埃及括號

From [here](https://yinwang1.substack.com/p/egypt-brackets).

自從出現 Java 語言，所謂 Egyptian brackets（埃及括號）的寫法就開始流行。為什麼叫「埃及括號」呢？因為他們把左邊的花括號放在一行的末尾，看起來就很像埃及壁畫裡的人物圖案（如圖）。

function fact(n) {

if (n == 0) {

return 1;

} else {

return n * fact(n - 1);

}

}

我自己也使用埃及括號多年，但在教學中，我決定拋棄它。我覺得埃及括號不符合藝術對稱的美感，而且使下一行距離太近，違反了排版美學。使用埃及括號的時候，我經常故意留一個空行，免得兩行粘的太近，這樣還不如乾脆把花括號放在下行開頭，自然空出一行來。

埃及括號的產生，可能是由於有人想把更多代碼行顯示在屏幕上。然而我發現，好程序員的函數都不會很長，所以沒必要費心思壓縮代碼的高度。

去掉埃及括號的桎梏之後，代碼更加美觀，容易理解。我推薦大家都這樣寫 Java 和 JavaScript 代碼。

function fact(n)

{

if (n == 0)

{

return 1;

}

else

{

return n * fact(n - 1);

}

}
