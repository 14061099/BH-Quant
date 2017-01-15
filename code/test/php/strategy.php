<!DOCTYPE html>
<!--[if IE 8]> <html lang="en" class="ie8"> <![endif]-->
<!--[if IE 9]> <html lang="en" class="ie9"> <![endif]-->
<!--[if !IE]><!-->
<html lang="en">
<!--<![endif]-->
<!-- BEGIN HEAD -->

<head>
    <meta charset="utf-8" />
    <title>BUAAQuant</title>
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <meta content="" name="description" />
    <meta content="" name="author" />
    <!-- BEGIN GLOBAL MANDATORY STYLES -->
    <link href="media/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <link href="media/css/bootstrap-responsive.min.css" rel="stylesheet" type="text/css" />
    <link href="media/css/font-awesome.min.css" rel="stylesheet" type="text/css" />
    <link href="media/css/style-metro.css" rel="stylesheet" type="text/css" />
    <link href="media/css/style.css" rel="stylesheet" type="text/css" />
    <link href="media/css/style-responsive.css" rel="stylesheet" type="text/css" />
    <link href="media/css/default.css" rel="stylesheet" type="text/css" id="style_color" />
    <link href="media/css/uniform.default.css" rel="stylesheet" type="text/css" />
    <!-- END GLOBAL MANDATORY STYLES -->
    <link rel="shortcut icon" href="media/image/favicon.ico" />
</head>
<!-- END HEAD -->
<!-- BEGIN BODY -->

<body class="page-header-fixed">
    <!-- BEGIN HEADER -->
    <div class="header navbar navbar-inverse navbar-fixed-top">
        <!-- BEGIN TOP NAVIGATION BAR -->
        <div class="navbar-inner">
            <div class="container-fluid">
                <!-- BEGIN LOGO -->
                <a class="brand" href="index.php">
                    <!-- <img src="media/image/logo.png" alt="logo" /> -->
                    <img src="media/image/BUAAQuant.png" alt="logo" />
                </a>
                <!-- END LOGO -->
                <!-- BEGIN RESPONSIVE MENU TOGGLER -->
                <a href="javascript:;" class="btn-navbar collapsed" data-toggle="collapse" data-target=".nav-collapse">
                    <img src="media/image/menu-toggler.png" alt="" />
                </a>
                <!-- END RESPONSIVE MENU TOGGLER -->
                <!-- BEGIN TOP NAVIGATION MENU -->
                <ul class="nav pull-right">
                    <li class="active"><a href="index.html"><i class="icon-cogs"></i><span>我的策略</span> </a> </li>
                    <li><a href="reports.html"><i class="icon-list-alt"></i><span>帮助</span> </a> </li>
                    <li><a href="guidely.html"><i class="icon-coffee"></i><span>智能投顾</span> </a></li>
                    <li><a href="charts.html"><i class="icon-comments"></i><span>社区</span> </a> </li>
                    <li><a href="shortcodes.html"><i class="icon-code"></i><span>Shortcodes</span> </a> </li>
                    <li class="dropdown">
                        <a href="javascript:;" class="dropdown-toggle" data-toggle="dropdown"> <i class="icon-long-arrow-down"></i><span>Drops</span> <b class="caret"></b></a>
                        <ul class="dropdown-menu">
                            <li><a href="icons.html">Icons</a></li>
                            <li><a href="faq.html">FAQ</a></li>
                            <li><a href="pricing.html">Pricing Plans</a></li>
                            <li><a href="login.html">Login</a></li>
                            <li><a href="signup.html">Signup</a></li>
                            <li><a href="error.html">404</a></li>
                        </ul>
                    </li>
                    <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown"><i
                            class="icon-cog"></i> 账户 <b class="caret"></b></a>
                        <ul class="dropdown-menu">
                            <li><a href="javascript:;">设置</a></li>
                            <li><a href="javascript:;">帮助</a></li>
                        </ul>
                    </li>
                    <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown"><i
                            class="icon-user"></i> 某某某 <b class="caret"></b></a>
                        <ul class="dropdown-menu">
                            <li><a href="javascript:;">个人信息</a></li>
                            <li><a href="javascript:;">登出</a></li>
                        </ul>
                    </li>
                </ul>
                <!-- END TOP NAVIGATION MENU -->
            </div>
        </div>
        <!-- END TOP NAVIGATION BAR -->
    </div>
    <!-- END HEADER -->
    <!-- BEGIN CONTAINER -->
    <div class="page-container row-fluid">
        <!-- BEGIN SIDEBAR -->
        <!-- END SIDEBAR -->
        <!-- BEGIN PAGE -->
        <div class="" style="background: #ffffff">
            <!-- BEGIN SAMPLE PORTLET CONFIGURATION MODAL FORM-->
            <!-- <div id="portlet-config" class="modal hide">
                <div class="modal-header">
                    <button data-dismiss="modal" class="close" type="button"></button>
                    <h3>portlet Settings</h3>
                </div>
                <div class="modal-body">
                    <p>Here will be a configuration form</p>
                </div>
            </div> -->
            <!-- END SAMPLE PORTLET CONFIGURATION MODAL FORM-->
            <!-- BEGIN PAGE CONTAINER-->
            <div class="container-fluid">
                <!-- BEGIN PAGE HEADER-->
                <div class="row-fluid">
                    <div class="span12">
                        <ul class="breadcrumb">
                            <li>
                                <i class="icon-home"></i>
                                <a href="index.html">首页</a>
                                <i class="icon-angle-right"></i>
                            </li>
                            <li><a href="#">策略</a></li>
                        </ul>
                        <!-- END PAGE TITLE & BREADCRUMB-->
                    </div>
                </div>
                <div class="span6 pull-left" style="width: 44.5%;">
                        <!-- BEGIN TAB PORTLET-->
                        <div class="portlet box blue tabbable">
                            <div class="portlet-title">
                                <div class="caption"><i class="icon-reorder"></i>帮助</div>
                            </div>
                            <div class="portlet-body">
                                <div class="tabbable portlet-tabs">
                                    <ul class="nav nav-tabs">
                                        <li><a href="#portlet_tab2_3" data-toggle="tab">智能策略实例</a></li>
                                        <li><a href="#portlet_tab2_2" data-toggle="tab">我的收藏</a></li>
                                        <li class="active"><a href="#portlet_tab2_1" data-toggle="tab">API文档</a></li>
                                    </ul>
                                    <div class="tab-content">
                                        <!-- <div class="tab-pane active" id="portlet_tab2_1">
                                            <div class="alert">
                                                Check out the below dropdown menu. It will be opened as usual since there is enough space at the bottom.
                                            </div>
                                            <div class="btn-group">
                                                <a class="btn red" href="#" data-toggle="dropdown">
                                                    <i class="icon-user"></i> Settings
                                                    <i class="icon-angle-down"></i>
                                                </a>
                                                <ul class="dropdown-menu">
                                                    <li><a href="#"><i class="icon-plus"></i> Add</a></li>
                                                    <li><a href="#"><i class="icon-trash"></i> Edit</a></li>
                                                    <li><a href="#"><i class="icon-remove"></i> Delete</a></li>
                                                    <li class="divider"></li>
                                                    <li><a href="#"><i class="i"></i> Full Settings</a></li>
                                                </ul>
                                            </div>
                                            <p>
                                                Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait.
                                            </p>
                                            <p>
                                                Deros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna.
                                            </p>
                                        </div> -->
                                       <!--  <div class="tab-pane" id="portlet_tab2_2">
                                            <p>
                                                Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo.
                                            </p>
                                            <p>
                                                <a class="btn red" href="ui_tabs_accordions.html#portlet_tab2_2" target="_blank">Activate this tab via URL</a>
                                            </p>
                                        </div> -->
                                       <!--  <div class="tab-pane" id="portlet_tab2_3">
                                            <p>
                                                Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.
                                            </p>
                                            <p>
                                                <a class="btn purple" href="ui_tabs_accordions.html#portlet_tab2_3" target="_blank">Activate this tab via URL</a>
                                            </p>
                                        </div> -->
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- END TAB PORTLET-->
                    </div>
               <div class="span6 pull-right" style="width: 50%;">
                <!-- BEGIN PROGRESS BARS PORTLET-->
                <div class="portlet box grey">
                    <div class="portlet-title">
                        <div class="caption"><i class="icon-cogs"></i>策略</div>
                        <div class="tools">
                            <a href="javascript:;" class="collapse"></a>
                            <a href="#portlet-config" data-toggle="modal" class="config"></a>
                            <a href="javascript:;" class="reload"></a>
                            <!-- <a href="javascript:;" class="remove"></a> -->
                        </div>
                    </div>
                    <div class="portlet-body">

                            <!-- /widget-header -->
                            <div class="widget-content">
                                <div id="code" style="height: 511px; width: auto;">from hmmlearn.hmm import GaussianHMM
import datetime
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import cm
from matplotlib import pyplot
startdate = '2012-06-01'
enddate = '2016-04-07'
df = get_price(['000300.XSHG'], start_date=startdate, end_date=enddate, frequency='daily', fields=['close','volume','high','low'])
close = df['close']['000300.XSHG']
high = df['high']['000300.XSHG'][5:]
low = df['low']['000300.XSHG'][5:]
volume = df['volume']['000300.XSHG'][5:]
money = df['volume']['000300.XSHG'][5:]
datelist = pd.to_datetime(close.index[5:])
logreturn = (np.log(np.array(close[1:]))-np.log(np.array(close[:-1])))[4:]
logreturn5 = np.log(np.array(close[5:]))-np.log(np.array(close[:-5]))
diffreturn = (np.log(np.array(high))-np.log(np.array(low)))
closeidx = close[5:]
X = np.column_stack([logreturn,diffreturn,logreturn5])
len(X)</div>
                                <script src="./js/src/ace.js" type="text/javascript" charset="utf-8"></script>
                                <script>
                                var editor = ace.edit("code");
                                editor.setTheme("ace/theme/monokai");
                                editor.getSession().setMode("ace/mode/python");
                                editor.getSession().setUseWrapMode(true);
                                var x = editor.getValue();
                                document.getElementById('code').style.fontSize = '16px';
                                console.log(x);
                                </script>
                                <!-- /shortcuts -->
                            </div>
                            <br>
                            <div style="right: 0"><a href="#" class="btn blue">运行回测 <i class="m-icon-swapright m-icon-white"></i></a></div>

                    </div>
                </div>
            </div>
                <!-- END PAGE CONTENT-->
            </div>
            <!-- END PAGE CONTAINER-->

        </div>
        <!-- END PAGE -->
    </div>
    <!-- END CONTAINER -->
    <!-- BEGIN FOOTER -->
    <div class="footer">
        <div class="footer-inner">
            2013 &copy; Metronic by keenthemes.
        </div>
        <div class="footer-tools">
            <span class="go-top">

            <i class="icon-angle-up"></i>

            </span>
        </div>
    </div>
    <!-- END FOOTER -->
    <!-- BEGIN JAVASCRIPTS(Load javascripts at bottom, this will reduce page load time) -->
    <!-- BEGIN CORE PLUGINS -->
    <script src="media/js/jquery-1.10.1.min.js" type="text/javascript"></script>
    <script src="media/js/jquery-migrate-1.2.1.min.js" type="text/javascript"></script>
    <!-- IMPORTANT! Load jquery-ui-1.10.1.custom.min.js before bootstrap.min.js to fix bootstrap tooltip conflict with jquery ui tooltip -->
    <script src="media/js/jquery-ui-1.10.1.custom.min.js" type="text/javascript"></script>
    <script src="media/js/bootstrap.min.js" type="text/javascript"></script>
    <!--[if lt IE 9]>

    <script src="media/js/excanvas.min.js"></script>

    <script src="media/js/respond.min.js"></script>

    <![endif]-->
    <script src="media/js/jquery.slimscroll.min.js" type="text/javascript"></script>
    <script src="media/js/jquery.blockui.min.js" type="text/javascript"></script>
    <script src="media/js/jquery.cookie.min.js" type="text/javascript"></script>
    <script src="media/js/jquery.uniform.min.js" type="text/javascript"></script>
    <!-- END CORE PLUGINS -->
    <script src="media/js/app.js"></script>
    <script>
    jQuery(document).ready(function() {

        App.init();

    });
    </script>
    <!-- END JAVASCRIPTS -->
    <script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-37564768-1']);
    _gaq.push(['_setDomainName', 'keenthemes.com']);
    _gaq.push(['_setAllowLinker', true]);
    _gaq.push(['_trackPageview']);
    (function() {
        var ga = document.createElement('script');
        ga.type = 'text/javascript';
        ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(ga, s);
    })();
    </script>
</body>
<!-- END BODY -->

</html>
