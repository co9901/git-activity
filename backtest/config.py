#!/usr/bin/env python

username = 'elnni'
password = '2lnnify'
database = 'backtest/data.pkl'

urls = [
    'https://github.com/fogleman/Craft.git',
    'https://github.com/mit-probabilistic-computing-project/BayesDB.git',
    'https://github.com/NeilFraser/JS-Interpreter.git',
    'https://github.com/statsmodels/statsmodels.git',
    'https://github.com/co9901/git-activity.git',
    'https://github.com/renzodenardi/jpgml.git',
    'https://github.com/yeomii/bacchusDB.git',
    'https://github.com/jugglinmike/chrome-user-agent.git',
    'https://github.com/noqqe/devnull-as-a-service.git',
    'https://github.com/lihaoyi/macropy.git',
    'https://github.com/feross/webtorrent.git',
    'https://github.com/shurain/bbb.git',
    'https://github.com/sublee/xyrn.git',
    'https://github.com/PredictionIO/PredictionIO.git',
    'https://github.com/dcramer/mangodb.git',
    'https://github.com/UCB-ICSI-Vision-Group/decaf-release.git',
    'https://github.com/nico/collectiveintelligence-book.git',
    'https://github.com/vhf/free-programming-books.git',
    'https://github.com/yhat/ggplot.git',
    'https://github.com/tylerwilliams/pymemc.git',
    'https://github.com/nnnick/Chart.js.git',
    'https://github.com/cudamat/cudamat.git',
    'https://github.com/centic9/jgit-cookbook.git',
    'https://github.com/quantopian/zipline.git',
    'https://github.com/mldss/pci-summary.git',
    'https://github.com/nitishsrivastava/deepnet.git',
    'https://github.com/luispedro/BuildingMachineLearningSystemsWithPython.git',
    'https://github.com/jakevdp/2013_fall_ASTR599.git',
    'https://github.com/networkx/networkx.git',
    'https://github.com/imos/Puzzle.git',
    'https://github.com/zavg/Asis.git',
    'https://github.com/piskvorky/gensim.git',
    'https://github.com/davidmoreno/onion.git',
    'https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition.git',
    'https://github.com/bower/bower.git',
    'https://github.com/JohnLangford/vowpal_wabbit.git',
    'https://github.com/PixarAnimationStudios/OpenSubdiv.git',
    'https://github.com/shurain/codesprint2013.git',
    'https://github.com/pymc-devs/pymc.git',
    'https://github.com/operatz/sustainable-assistance.git',
    'https://github.com/rstacruz/nprogress.git',
    'https://github.com/chrisclark/PythonForDataScience.git',
    'https://github.com/lisa-lab/pylearn2.git',
    'https://github.com/facebook/tornado.git',
    'https://github.com/mgedmin/findimports.git',
    'https://github.com/Hybrid0/clj-hannanum.git',
    'https://github.com/github/github-services.git',
    'https://github.com/rhiokim/haroopad.git',
    'https://github.com/rofl0r/proxychains-ng.git',
    'https://github.com/mozilla/rust.git',
    'https://github.com/e-/MulticoreComputing.git',
    'https://github.com/hmason/tc.git',
    'https://github.com/fogleman/Minecraft.git',
    'https://github.com/NancyFx/Nancy.git',
    'https://github.com/toopay/bootstrap-markdown.git',
    'https://github.com/karan/Projects.git',
    'https://github.com/scikit-learn/scikit-learn.git',
    'https://github.com/saitoha/tanasinn.git',
    'https://github.com/github/choosealicense.com.git',
    'https://github.com/pgriess/node-webworker.git',
    'https://github.com/samsquire/ideas.git',
    'https://github.com/nforge/yobi.git',
    'https://github.com/orangeduck/libCello.git',
    'https://github.com/blueimp/jQuery-File-Upload.git',
    'https://github.com/mame/quine-relay.git',
    'https://github.com/tjpalmer/blockly-mario.git',
    'https://github.com/tomyun/xeit.git',
    'https://github.com/SamyPesse/tv.js.git',
    'https://github.com/gangwon/3046.git',
    'https://github.com/facebook/fbconsole.git',
    'https://github.com/pubnub/genetic-car-2.git',
    'https://github.com/hakimel/reveal.js.git',
    'https://github.com/sim0629/sirc.git',
    'https://github.com/hakimel/Ladda.git',
    'https://github.com/jakearchibald/request-quest.git',
    'https://github.com/pa7/nude.js.git',
    'https://github.com/JuliaLang/julia.git',
    'https://github.com/designmodo/Flat-UI.git',
    'https://github.com/superjoe30/jamulator.git',
    'https://github.com/Valloric/YouCompleteMe.git',
    'https://github.com/twbs/bootstrap.git',
    'https://github.com/jongman/algospot.git',
    'https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers.git',
    'https://github.com/harthur/brain.git',
    'https://github.com/shutterstock/rickshaw.git',
    'https://github.com/tric/trick2013.git',
    'https://github.com/kripken/lua.vm.js.git',
    'https://github.com/shaih/HElib.git',
    'https://github.com/kripken/speak.js.git',
    'https://github.com/nigma/pywt.git',
    'https://github.com/commonsense/conceptnet.git',
    'https://github.com/msanders/autopy.git',
    'https://github.com/sympy/sympy.git',
    'https://github.com/deeplearningais/CUV.git',
    'https://github.com/joyent/node.git',
    'https://github.com/nforge/yobi.git',
    'https://github.com/twbs/bootstrap.git',
    'https://github.com/jquery/jquery.git',
    'https://github.com/rails/rails.git',
    'https://github.com/mbostock/d3.git',
    'https://github.com/angular/angular.js.git',
    'https://github.com/mrdoob/three.js.git',
    'https://github.com/hakimel/reveal.js.git',
    'https://github.com/django/django.git',
    'https://github.com/mitsuhiko/flask.git',
    'https://github.com/facebook/tornado.git',
    'https://github.com/reddit/reddit.git',
    'https://github.com/ipython/ipython.git',
    'https://github.com/webpy/webpy.git',
    'https://github.com/pydata/pandas.git',
    'https://github.com/b4winckler/macvim.git',
    'https://github.com/scikit-learn/scikit-learn.git',
    'https://github.com/numpy/numpy.git',
    'https://github.com/elasticsearch/elasticsearch.git',
    'https://github.com/nathanmarz/storm.git',
    'https://github.com/clojure/clojure.git',
    'https://github.com/facebook/facebook-android-sdk.git',
    'https://github.com/spring-projects/spring-framework.git',
    'https://github.com/netty/netty.git',
    'https://github.com/mongodb/mongo.git',
    'https://github.com/rethinkdb/rethinkdb.git',
]

def parse(url):
    owner, repo = url.split('/')[-2:]
    return (owner, repo[:-4], url)

targets = [parse(u) for u in list(set(urls))]
