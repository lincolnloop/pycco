# -*- coding: utf-8 -*-
css = u"""\
/*--------------------- Layout and Typography ----------------------------*/
body {
  font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, FreeSerif, serif;
  font-size: 16px;
  line-height: 24px;
  color: #252519;
  margin: 0; padding: 0;
  background: #f5f5ff;
}
body.no-code {
    background: white;
}
a {
  color: #261a3b;
}
  a:visited {
    color: #261a3b;
  }
p {
  margin: 0 0 15px 0;
}
h1, h2, h3, h4, h5, h6 {
  margin: 40px 0 15px 0;
}
h2, h3, h4, h5, h6 {
    margin-top: 0;
  }
#container {
  background: white;
 }
#container, div.section {
  position: relative;
}
.no-code #background {
    display: none;
}
#background {
  position: absolute;
  top: 0; left: 580px; right: 0; bottom: 0;
  background: #f5f5ff;
  border-left: 1px solid #e5e5ee;
  z-index: 0;
}
#jump_to, #jump_page {
  background: white;
  -webkit-box-shadow: 0 0 25px #777; -moz-box-shadow: 0 0 25px #777;
  -webkit-border-bottom-left-radius: 5px; -moz-border-radius-bottomleft: 5px;
  font: 10px Arial;
  text-transform: uppercase;
  cursor: pointer;
  text-align: right;
}
#jump_to, #jump_wrapper {
  position: fixed;
  right: 0; top: 0;
  padding: 5px 10px;
}
  #jump_wrapper {
    padding: 0;
    display: none;
  }
    #jump_to:hover #jump_wrapper {
      display: block;
    }
    #jump_page {
      padding: 5px 0 3px;
      margin: 0 0 25px 25px;
    }
      #jump_page .source {
        display: block;
        padding: 5px 10px;
        text-decoration: none;
        border-top: 1px solid #eee;
      }
        #jump_page .source:hover {
          background: #f5f5ff;
        }
        #jump_page .source:first-child {
        }
.no-code div.docs {
    max-width: 600px;
    min-width: 600px;
}
div.docs {
  float: left;
  max-width: 500px;
  min-width: 500px;
  min-height: 5px;
  padding: 10px 25px 1px 50px;
  vertical-align: top;
  text-align: left;
}
  .docs pre {
    margin: 15px 0 15px;
    padding-left: 15px;
  }
  .docs p tt, .docs p code {
    background: #f8f8ff;
    border: 1px solid #dedede;
    font-size: 12px;
    padding: 0 0.2em;
  }
  .octowrap {
    position: relative;
  }
    .octothorpe {
      font: 12px Arial;
      text-decoration: none;
      color: #454545;
      position: absolute;
      top: 3px; left: -20px;
      padding: 1px 2px;
      opacity: 0;
      -webkit-transition: opacity 0.2s linear;
    }
      div.docs:hover .octothorpe {
        opacity: 1;
      }
div.code {
  margin-left: 580px;
  padding: 14px 15px 16px 50px;
  vertical-align: top;
}
  .code pre, .docs p code {
    font-size: 12px;
  }
    pre, tt, code {
      line-height: 18px;
      font-family: Monaco, Consolas, "Lucida Console", monospace;
      margin: 0; padding: 0;
    }
div.clearall {
    clear: both;
}


/*---------------------- Syntax Highlighting -----------------------------*/
td.linenos { background-color: #f0f0f0; padding-right: 10px; }
span.lineno { background-color: #f0f0f0; padding: 0 5px 0 5px; }
body .hll { background-color: #ffffcc }
body .c { color: #408080; font-style: italic }  /* Comment */
body .err { border: 1px solid #FF0000 }         /* Error */
body .k { color: #954121 }                      /* Keyword */
body .o { color: #666666 }                      /* Operator */
body .cm { color: #408080; font-style: italic } /* Comment.Multiline */
body .cp { color: #BC7A00 }                     /* Comment.Preproc */
body .c1 { color: #408080; font-style: italic } /* Comment.Single */
body .cs { color: #408080; font-style: italic } /* Comment.Special */
body .gd { color: #A00000 }                     /* Generic.Deleted */
body .ge { font-style: italic }                 /* Generic.Emph */
body .gr { color: #FF0000 }                     /* Generic.Error */
body .gh { color: #000080; font-weight: bold }  /* Generic.Heading */
body .gi { color: #00A000 }                     /* Generic.Inserted */
body .go { color: #808080 }                     /* Generic.Output */
body .gp { color: #000080; font-weight: bold }  /* Generic.Prompt */
body .gs { font-weight: bold }                  /* Generic.Strong */
body .gu { color: #800080; font-weight: bold }  /* Generic.Subheading */
body .gt { color: #0040D0 }                     /* Generic.Traceback */
body .kc { color: #954121 }                     /* Keyword.Constant */
body .kd { color: #954121; font-weight: bold }  /* Keyword.Declaration */
body .kn { color: #954121; font-weight: bold }  /* Keyword.Namespace */
body .kp { color: #954121 }                     /* Keyword.Pseudo */
body .kr { color: #954121; font-weight: bold }  /* Keyword.Reserved */
body .kt { color: #B00040 }                     /* Keyword.Type */
body .m { color: #666666 }                      /* Literal.Number */
body .s { color: #219161 }                      /* Literal.String */
body .na { color: #7D9029 }                     /* Name.Attribute */
body .nb { color: #954121 }                     /* Name.Builtin */
body .nc { color: #0000FF; font-weight: bold }  /* Name.Class */
body .no { color: #880000 }                     /* Name.Constant */
body .nd { color: #AA22FF }                     /* Name.Decorator */
body .ni { color: #999999; font-weight: bold }  /* Name.Entity */
body .ne { color: #D2413A; font-weight: bold }  /* Name.Exception */
body .nf { color: #0000FF }                     /* Name.Function */
body .nl { color: #A0A000 }                     /* Name.Label */
body .nn { color: #0000FF; font-weight: bold }  /* Name.Namespace */
body .nt { color: #954121; font-weight: bold }  /* Name.Tag */
body .nv { color: #19469D }                     /* Name.Variable */
body .ow { color: #AA22FF; font-weight: bold }  /* Operator.Word */
body .w { color: #bbbbbb }                      /* Text.Whitespace */
body .mf { color: #666666 }                     /* Literal.Number.Float */
body .mh { color: #666666 }                     /* Literal.Number.Hex */
body .mi { color: #666666 }                     /* Literal.Number.Integer */
body .mo { color: #666666 }                     /* Literal.Number.Oct */
body .sb { color: #219161 }                     /* Literal.String.Backtick */
body .sc { color: #219161 }                     /* Literal.String.Char */
body .sd { color: #219161; font-style: italic } /* Literal.String.Doc */
body .s2 { color: #219161 }                     /* Literal.String.Double */
body .se { color: #BB6622; font-weight: bold }  /* Literal.String.Escape */
body .sh { color: #219161 }                     /* Literal.String.Heredoc */
body .si { color: #BB6688; font-weight: bold }  /* Literal.String.Interpol */
body .sx { color: #954121 }                     /* Literal.String.Other */
body .sr { color: #BB6688 }                     /* Literal.String.Regex */
body .s1 { color: #219161 }                     /* Literal.String.Single */
body .ss { color: #19469D }                     /* Literal.String.Symbol */
body .bp { color: #954121 }                     /* Name.Builtin.Pseudo */
body .vc { color: #19469D }                     /* Name.Variable.Class */
body .vg { color: #19469D }                     /* Name.Variable.Global */
body .vi { color: #19469D }                     /* Name.Variable.Instance */
body .il { color: #666666 }                     /* Literal.Number.Integer.Long */


* {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

html,
body,
#Page {
  height: 100vh;
}

#Page {
  transform: translateX(-400px);
  transition: transform .3s;
}

#Page[data-state=open] {
  overflow-x: hidden;
  transform: translateX(0);
}

/* Resets and unborking */
#container > .section .docs:first-of-type {
  margin-bottom: 40px;
}

.clearall div.docs:first-of-type h1 {
  margin-top: 0;
}

/* Navigation */
#container {
  box-sizing: content-box;
  width: 500px;
  padding-left: calc(400px + 2.6em);
}

#background {
  left: calc(500px + 400px + 2.6em);
}

div.code {
  margin-left: 500px;
}

.docsnav {
  position: absolute;
  z-index: 1;
  width: 400px;
  height: 100%;
  font-size: 120%;
}

.docsnav,
.docsnav-tree {
  background: #292929;
}

.docsnav-header {
  padding-top: 1em;
}

.docsnav-tree {
  padding-left: 0;
}

.docsnav-branch {
  list-style: none;
}

.docsnav-branch .docsnav-tree {
  display: none;
}

.docsnav-branch[data-state=open] > .docsnav-tree {
  display: block;
}

/* Handle folders */
.docsnav-folder {
  font-weight: bold;
}

.docsnav-folder + .docsnav-tree {
  margin-bottom: 1em;
}

.docsnav-folder + .docsnav-tree a {
  font-size: 92.5%;
  padding: .4em 1em;
}

/* Poor man indentation */
.docsnav-tree .docsnav-tree a {
  padding-left: 2em;
}

.docsnav-tree .docsnav-tree .docsnav-tree a {
  padding-left: 3em;
}

.docsnav-tree .docsnav-tree .docsnav-tree .docsnav-tree a {
  padding-left: 4em;
}

/* All links */
.docsnav a,
.docsnav-toggler {
  display: flex;
  align-items: center;
  justify-content: space-between;

  padding: .65em 1em;
  border-bottom: 1px solid #393939;
  font-family: 'Open Sans',sans-serif;
  color: ghostwhite;
  text-decoration: none;
  line-height: 1.2;
}

.docsnav-file:hover {
  background: #373737;
}

.docsnav-icon {
  display: inline-block;
}

.docsnav-icon,
.docsnav-file:after {
  font-size: 150%;
  font-weight: normal;
  color: #669966;
  content: "→";
}

.docsnav-file:after {
  visibility: hidden;
}

.docsnav-file:hover:after {
  visibility: visible;
}

.docsnav a:visited,
.docsnav-toggler:visited {
  color: white;
}

/* Exception to the all links rule */
.docsnav-header .docsnav-upbtn {
  align-items: baseline;
  justify-content: initial;
}

.docsnav .docsnav-toggler {
  border-bottom: none;
}

.docsnav-toggler {
  z-index: 2;
  position: absolute;
  top: 80px;
  left: 353px;

  justify-content: center;

  height: 2.6em;
  width: 15vh;
  min-width: 8em;

  transform: rotate(90deg);

  border: none;
  background: #222;

  font-size: 90%;
  font-weight: bold;
  text-transform: uppercase;
  line-height: 1;
  color: white;
  cursor: pointer;
}
"""

html = """\
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html;charset=utf-8">
  <title>{{ title }}</title>
  <link rel="stylesheet" href="{{ stylesheet }}">
</head>
<body class="{{ page_class }}">

<div id="Page">
<nav id="docsnav" class="docsnav">
  <a href="#" class="docsnav-toggler" id="MenuToggler">Menu</a>

  <header class="docsnav-header">
    <!-- You may not need this -->
    <a href="/" class="docsnav-folder docsnav-upbtn">
      <span class="docsnav-icon">&#8593;</span>
      TOP
    </a>
    <!--
    <a href="#" class="docsnav-folder docsnav-upbtn">
      <span class="docsnav-icon">&#11025;</span>
      Projects
    </a>
    -->
  </header>
<ul class="docsnav-tree">
    {{& tree}}
</ul>
</nav>
<div id='container'>
  <div id="background"></div>
  {{#sources?}}
  <div id="jump_to">
    Jump To &hellip;
    <div id="jump_wrapper">
      <div id="jump_page">
        {{#sources}}
          <a class="source" href="{{ url }}">{{ basename }}</a>
        {{/sources}}
      </div>
    </div>
  </div>
  {{/sources?}}
  <div class='section'>
    <div class='docs'><h1>{{ title }}</h1></div>
  </div>
  <div class='clearall'>
  {{#sections}}
  <div class='section' id='section-{{ num }}'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-{{ num }}'>#</a>
      </div>
      {{{ docs_html }}}
    </div>
    <div class='code'>
      {{{ code_html }}}
    </div>
  </div>
  <div class='clearall'></div>
  {{/sections}}
</div>
</div>
<script>
(function() {
  var toggler = document.getElementById('MenuToggler'),
      page = document.getElementById('Page'),
      content = document.getElementById('container'),
      folders = document.querySelectorAll('.docsnav-tree .docsnav-folder');
  if (document.getElementsByTagName('BODY')[0].classList.contains('no-code')) {
    page.setAttribute('data-state', 'open');
  }
  toggler.addEventListener('click', function(evt) {
    evt.preventDefault();

    page.setAttribute('data-state', page.getAttribute('data-state') === 'open' ? 'closed' : 'open');
  });

  for (var i = 0; i < folders.length; i++) {
    folder = folders[i];

    folder.addEventListener('click', function(evt) {
      evt.preventDefault();

      branch = this.parentNode;

      branch.setAttribute('data-state', branch.getAttribute('data-state') === 'open' ? 'closed' : 'open');
    });
  }
})();
</script>
</body>
"""
