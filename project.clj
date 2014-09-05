(defproject get_wangyin_blog "0.1.0-SNAPSHOT"
  :description "Get all Wangyin's blog pages and convert them into markdown format."
  :url "http://github.com/gangmax"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.5.1"]
                 [enlive "1.1.5"]
                ]
  :jvm-opts ^:replace [] ;Fix the "TieredCompilation is disabled in this release" error, from "https://github.com/technomancy/leiningen/wiki/Faster"
  :main get_wangyin_blog.core)
