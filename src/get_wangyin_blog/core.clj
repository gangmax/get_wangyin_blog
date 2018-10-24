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
    [clojure.repl :refer [doc]]
    [get_wangyin_blog.lib :as lib] ))

(defn -main [& args]
  (do
    (doc lib/download)
    (println (lib/download "http://www.yinwang.org" "/blog-cn/" "./blog/", false))))
