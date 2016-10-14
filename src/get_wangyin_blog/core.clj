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
    
    (def file-names
      (map
        #(str
          (-> % 
            (.substring
              (.length url-prefix))
            (.replace \/ \-))
          ".markdown")
        links))
    
    (defn trim-content
      "Get the meaningful text content from the HTML content."
      [content prefix postfix]
      (let [
        cannot-trim-tag "CANNOT find trim prefix/postfix!!!!!!\n\n\n"
        prefix-index (string/index-of content prefix)
        postfix-index (string/index-of content postfix)]
        (if (and 
              (not (nil? prefix-index))
              (not (nil? postfix-index))
              (>= prefix-index 0)
              (> postfix-index prefix-index))
          (subs content (+ prefix-index (count prefix)) postfix-index)
          content)))

    (pmap
      #(let [
          file-path-name (str target-directory (second %))
          ; Handle the "301 Moved Permanently" error: which is caused by the
          ; "http://yinwang.org/" to "http://www.yinwang.org/" changes.
          ; The solution is to add "www" at the begining of the URL.
          url (let [link (first %)]
                (if (= "www." (subs (second (string/split link #"//")) 0 4))
                  link
                  (str (first (string/split link #"//")) "//www." (second (string/split link #"//")))))
          prefix "<div style=\"margin: 2% 5% 2% 5%\">\n\n<table>\n\n<tbody>\n\n<tr>\n\n<td width=\"60%\">\n\n<div style=\"padding: 2% 8% 5% 8%; border: 1px solid LightGrey;\">\n\n"
          postfix "\n</div>\n\n<div style=\"margin-top: 5px\"><script>(adsbygoogle = window.adsbygoogle || []).push({});</script></div>\n\n</td>\n\n<td width=\"16%\" valign=\"top\"><script>(adsbygoogle = window.adsbygoogle || []).push({});</script></td>\n\n</tr>\n\n</tbody>\n\n</table>\n\n</div>\n"]
        (do
          (println (str "Downloading '" url "'..."))
          (spit file-path-name 
            (trim-content 
              (:out (sh (str (System/getProperty "user.dir") "/resources/h2m.js") url))
              prefix postfix))
          (println (str "Saved to " file-path-name "..."))
          file-path-name))
      (zipmap links file-names))))

(defn -main [& args]
  (do
    (doc download)
    (println (download "http://www.yinwang.org/" "http://yinwang.org/blog-cn/" "./blog/"))))
