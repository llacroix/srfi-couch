<!DOCTYPE html>
<html>
<head>
  <title>The Pyramid Web Framework</title>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <meta name="keywords" content="python web application" />
  <meta name="description" content="pyramid web application" />

  <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/prettify/r224/prettify.css" type="text/css">

  <link rel="stylesheet" href="${request.static_url('pysrfi:static/styles/bootstrap.css')}" type="text/css" media="screen" charset="utf-8" />
  <link rel="stylesheet" href="${request.static_url('pysrfi:static/styles/jquery.terminal.css')}" type="text/css" media="screen" charset="utf-8" />

  <!-- <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=AM_HTMLorMML-full"></script> -->
  <!-- <script src="http://cdnjs.cloudflare.com/ajax/libs/prettify/r224/prettify.js" type="text/javascript"></script> -->

  <script src="${request.static_url('pysrfi:static/scripts/lib/jquery.js')}" type="text/javascript"></script>
  <script src="${request.static_url('pysrfi:static/scripts/lib/jquery.terminal.js')}" type="text/javascript"></script>
  <script src="${request.static_url('pysrfi:static/scripts/lib/bootstrap.js')}" type="text/javascript"></script>
  <script src="${request.static_url('pysrfi:static/scripts/lib/biwascheme-0.6.1.js')}" type="text/javascript"></script>

  <script src="${request.static_url('pysrfi:static/scripts/site.js')}" type="text/javascript"></script>

  <style>
    body {
        padding-top: 70px;
        padding-bottom: 20px;
    }

    dd {
        padding: 10px 20px;
    }

    /* By default it's not affixed in mobile views, so undo that */
    .bs-sidebar.affix {
      position: static;
    }

    /* First level of nav */
    .bs-sidebar .bs-sidenav {
      margin-bottom: 30px;
      padding-top:    10px;
      padding-bottom: 10px;
      text-shadow: 0 1px 0 #fff;
      background-color: #f7f5fa;
      border-radius: 5px;
    }

    /* All levels of nav */
    .bs-sidebar .nav > li > a {
      display: block;
      color: #716b7a;
      padding: 5px 20px;
    }

    .bs-sidebar .nav > li > a:hover,
    .bs-sidebar .nav > li > a:focus {
      text-decoration: none;
      background-color: #e5e3e9;
      border-right: 1px solid #dbd8e0;
    }

    .bs-sidebar .nav > .active > a,
    .bs-sidebar .nav > .active:hover > a,
    .bs-sidebar .nav > .active:focus > a {
      font-weight: bold;
      color: #563d7c;
      background-color: transparent;
      border-right: 1px solid #563d7c;
    }

    /* Nav: second level (shown on .active) */
    .bs-sidebar .nav .nav {
      display: none; /* Hide by default, but at >768px, show it */
      margin-bottom: 8px;
    }
    .bs-sidebar .nav .nav > li > a {
      padding-top:    3px;
      padding-bottom: 3px;
      padding-left: 30px;
      font-size: 90%;
    }

    /* Show and affix the side nav when space allows it */
    @media (min-width: 992px) {
      .bs-sidebar .nav > .active > .nav {
        display: block;
      }
      /* Widen the fixed sidebar */
      .bs-sidebar.affix,
      .bs-sidebar.affix-bottom {
        width: 213px;
      }
      .bs-sidebar.affix {
        position: fixed; /* Undo the static from mobile first approach */
        top: 80px;
      }
      .bs-sidebar.affix-bottom {
        position: absolute; /* Undo the static from mobile first approach */
      }
      .bs-sidebar.affix-bottom > .bs-sidenav,
      .bs-sidebar.affix > .bs-sidenav,
      .bs-sidebar.affix-bottom > .toc > .nav,
      .bs-sidebar.affix > .toc > .nav {
        margin-top: 0;
        margin-bottom: 0;
      }
    }

    @media (min-width: 1200px) {
      /* Widen the fixed sidebar again */
      .bs-sidebar.affix-bottom,
      .bs-sidebar.affix {
        width: auto;
      }
    }
  </style>

</head>
<body>
    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">SRFIs</a>
        </div>
        <div class="navbar-collapse collapse">
        </div><!--/.navbar-collapse -->
      </div>
    </div>

    <div class="container">
        <div class="term"></div>
    </div>

    ${next.body()}

    <hr />
</body>
</html>
