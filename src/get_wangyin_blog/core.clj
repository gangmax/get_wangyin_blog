; 
; Get all Wangyin's blog pages and convert them into markdown format.
;
; Several things need to be done to archived it: 
;
; 1. Parse the index page of "http://www.yinwang.org/", get all the blog pages;
;
; 2. Get the blog pages and covert them into markdown format with "html2text.py";
;
; 3. Handle the unexpected "\n" characters made by "html2text".
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
    
    (spit "/tmp/html2text.py" (slurp (io/resource "html2text.py")))
    
    (sh "chmod" "+x" "/tmp/html2text.py")
    
    (map
      #(let [file-path-name (str target-directory (second %))]
        (do
          (println (str "Downloading '" (first %) "'..."))
          (spit file-path-name
            ; Get the raw markdown format by invoking the "html2text.py" program,
            ; then remove the useless '\n' characters in it.
            ; If both of the last character before and the next character after a
            ; "\n" character are not a "\n", it is a useless "\n".
            ; Only the "\n\n" segment is a real "return" and should not be kept.
            (clojure.string/replace
              (:out (sh "/tmp/html2text.py" (first %)))
              #"([^\n])\n([^\n])" "$1$2"))
          (println (str "Saved to " file-path-name "..."))
          file-path-name))
      (zipmap links file-names))))

(defn -main [& args]
  (do
    (doc download)
    (println (download "http://www.yinwang.org/" "http://yinwang.org/blog-cn/" "/tmp/"))))

