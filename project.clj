(defproject get_wangyin_blog "0.1.0-SNAPSHOT"
  :description "Get all Wangyin's blog pages and convert them into markdown format."
  :url "http://github.com/gangmax/get_wangyin_blog"
  :license {:name "GPLv3"
            :url "https://www.gnu.org/licenses/gpl-3.0.txt"}
  :dependencies [[org.clojure/clojure "1.8.0"]
                 [enlive "1.1.6"]
                ]
  :jvm-opts ^:replace [] ;Fix the "TieredCompilation is disabled in this release" error, from "https://github.com/technomancy/leiningen/wiki/Faster"
  :main get_wangyin_blog.core)
