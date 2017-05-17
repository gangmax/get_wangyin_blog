; 
; Get all Wangyin's blog pages and convert them into markdown format.
;
; Several things need to be done to achieve this:
;
; 1. Parse the index page of "http://www.yinwang.org/", get all the blog pages;
;
; 2. Get the blog pages and covert them into markdown format with "h2m.js".
;
; http://stackoverflow.com/questions/15474994/how-to-parse-html-file-using-clojure
; https://github.com/swannodette/enlive-tutorial/
; http://stackoverflow.com/questions/15875859/opening-file-in-the-same-directory-as-running-code-in-clojure
; http://stackoverflow.com/questions/12469259/how-to-package-shell-script-into-a-leiningen-project
;

(ns get_wangyin_blog.core
  (:require
    [clojure.string :as string]
    [clojure.java.shell :refer [sh]]
    [clojure.repl :refer [doc]]
    [net.cgrand.enlive-html :as html]
    [clojure.java.io :as io] ))

(defn doseq-interval
  "http://stackoverflow.com/questions/25733717/clojure-thread-sleep-between-map-evaluation"
  [f coll interval]
  (doseq [x coll]
    (f x)
    (Thread/sleep interval)))

(defn download
  "Get all Wangyin's blog pages and convert them into markdown format."
  [base-url url-prefix target-directory]
  
  (do
    (def links
      (map #(:href (:attrs %))
        (html/select 
          (html/html-resource
            (java.net.URL. base-url))
          [:li.list-group-item :a])))
    ;(println links)
    (def file-names
      (map
        #(str
          (-> % 
            (.substring
              (.length url-prefix))
            (.replace \/ \-))
          ".markdown")
        links))
    ;(println file-names)
    (defn trim-content
      "Get the meaningful text content from the HTML content."
      [content prefix postfix]
      (let [
        prefix-index (string/index-of content prefix)
        postfix-index (string/index-of content postfix)]
        (do
        ;(println (str "prefix-index=" prefix-index ", postfix-index=" postfix-index))
        ;(println content)
        (if
          (and 
            (not (nil? prefix-index))
            (not (nil? postfix-index))
            (>= prefix-index 0)
            (> postfix-index prefix-index))
          (subs content (+ prefix-index (count prefix)) postfix-index)
          content))))

    (pmap
      #(let
        [
          file-path-name (str target-directory (second %))
          ; Handle the "301 Moved Permanently" error: which is caused by the
          ; "http://yinwang.org/" to "http://www.yinwang.org/" changes.
          ; The solution is to add "www" at the begining of the URL.
          url (let [link (str base-url (first %))] ; base-url: "http://www.yinwang.org/", first(link): "/blog-cn/2017/05/16/chinese"
                (if (= "www." (subs (second (string/split link #"//")) 0 4))
                  link
                  (str (first (string/split link #"//")) "//www." (second (string/split link #"//")))))
          prefix "<div style=\"margin: 2% 5% 2% 5%\">\n\n<table>\n\n<tbody>\n\n<tr>\n\n<td width=\"60%\">\n\n<div style=\"padding: 2% 8% 5% 8%; border: 1px solid LightGrey;\">\n\n"
          postfix "\n</div>\n\n<div style=\"margin-top: 5px\"><script>(adsbygoogle = window.adsbygoogle || []).push({});</script></div>\n\n</td>\n\n<td width=\"16%\" valign=\"top\"><script>(adsbygoogle = window.adsbygoogle || []).push({});</script></td>\n\n</tr>\n\n</tbody>\n\n</table>\n\n</div>\n"
        ]
        (println (str "Downloading '" url "'..."))
        (def output
          (-> (str (System/getProperty "user.dir") "/resources/h2m.js")
              (sh url)))
        (def text (trim-content (:out output) prefix postfix))
        (when-not (empty? text) (spit file-path-name text))
        (if (empty? text)
          (println (str "CANNOT FETCH THE CONTENT BY THE GIVEN URL: " url ": " (:error output)))
          (println (str "Saved to " file-path-name "...")))
        file-path-name)
      (zipmap links file-names))))

(defn -main [& args]
  (do
    (doc download)
    (println (download "http://www.yinwang.org" "/blog-cn/" "./blog/"))))
