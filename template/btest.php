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
    <!-- BEGIN PAGE LEVEL STYLES -->
    <link rel="stylesheet" type="text/css" href="media/css/jquery-ui-1.10.1.custom.min.css">
    <link href=" media/css/bootstrap-modal.css " rel="stylesheet " type="text/css " />
    <!-- END PAGE LEVEL STYLES -->
    <link rel="shortcut icon " href="media/image/favicon.ico " />
    <script src="media/js/jquery-1.10.1.min.js " type="text/javascript "></script>
    <script src="media/js/jquery-migrate-1.2.1.min.js " type="text/javascript "></script>
    <!-- IMPORTANT! Load jquery-ui-1.10.1.custom.min.js before bootstrap.min.js to fix bootstrap tooltip conflict with jquery ui tooltip -->
    <script src="media/js/jquery-ui-1.10.1.custom.min.js " type="text/javascript "></script>
    <script src="media/js/bootstrap.min.js " type="text/javascript "></script>
    <!--[if lt IE 9]>

    <script src="media/js/excanvas.min.js "></script>

    <script src="media/js/respond.min.js "></script>

    <![endif]-->
    <script src="media/js/jquery.slimscroll.min.js " type="text/javascript "></script>
    <script src="media/js/jquery.blockui.min.js " type="text/javascript "></script>
    <script src="media/js/jquery.cookie.min.js " type="text/javascript "></script>
    <script src="media/js/jquery.uniform.min.js " type="text/javascript "></script>
    <!-- END CORE PLUGINS -->
    <!-- BEGIN PAGE LEVEL PLUGINS -->
    <script src="media/js/bootstrap-modal.js " type="text/javascript "></script>
    <script src="media/js/bootstrap-modalmanager.js " type="text/javascript "></script>
    <!-- END PAGE LEVEL PLUGINS -->
    <!-- BEGIN PAGE LEVEL SCRIPTS -->
    <script src="media/js/app.js "></script>
    <script src="media/js/echarts.js "></script>
    <script src="media/js/ui-modals.js "></script>
    <!-- END PAGE LEVEL SCRIPTS -->
    <script>
    jQuery(document).ready(function() {

        // initiate layout and plugins

        App.init();

        UIModals.init();

    });
    </script>
    <style type="text/css">
    div.hidden {
        display: none;
    }
    </style>
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
                <a class="brand" href="index.html">
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
                                        class="icon-user"></i> 某某�?<b class="caret"></b></a>
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
        <div class="page-sidebar nav-collapse collapse">
            <!-- BEGIN SIDEBAR MENU -->
            <ul class="page-sidebar-menu">
                <li>
                    <!-- BEGIN SIDEBAR TOGGLER BUTTON -->
                    <div class="sidebar-toggler hidden-phone"></div>
                    <!-- BEGIN SIDEBAR TOGGLER BUTTON -->
                </li>
                <li class=" ">
                    <a href="temp.html">
                        <i class="icon-arrow-left"></i>
                        <span class="title">返回</span>
                    </a>
                </li>
                <li class="start active">
                    <a href="#" onclick="showChart()">
                        <span class="title">收益概况</span>
                    </a>
                </li>
                <li class=" ">
                    <a href="deal_detail.html">
                        <span class="title">交易详情</span>
                    </a>
                </li>
                <li class=" ">
                    <a href="day_return.html">
                        <span class="title">每日概况</span>
                    </a>
                </li>
                <li class=" ">
                    <a href="log.html">
                        <span class="title">日志输出</span>
                    </a>
                </li>
                <li class="">
                    <a href="javascript:;">
                        <i class="icon-bookmark-empty"></i>
                        <span class="title">数据分析</span>
                        <span class="selected"></span>
                        <span class="arrow open"></span>
                    </a>
                    <ul class="sub-menu">
                        <li>
                            <a href="strategy_profit.html">

                            策略收益</a>
                        </li>
                        <li>
                            <a href="benchmark_profit.html">

                            基准收益</a>
                        </li>
                        <li class="">
                            <a href="Alpha.html">

                            Alpha</a>
                        </li>
                        <li>
                            <a href="Beta.html">

                            Beta</a>
                        </li>
                        <li>
                            <a href="Sharpe.html">

                            Sharpe</a>
                        </li>
                        <li>
                            <a href="Sortino.html">

                            Sortino</a>
                        </li>
                        <li>
                            <a href="information_ratio.html">

                            Information Ratio</a>
                        </li>
                        <li>
                            <a href="volatility.html">

                            Volatility</a>
                        </li>
                        <li>
                            <a href="benchmark_volatility.html">

                            Benchmark Volatility</a>
                        </li>
                        <li>
                            <a href="max_drawdown.html">

                            Max Drawdown</a>
                        </li>
                    </ul>
                </li>
            </ul>
            <!-- END SIDEBAR MENU -->
        </div>
        <!-- END SIDEBAR -->
        <!-- BEGIN PAGE -->
        <div class="page-content">
            <!-- BEGIN PAGE CONTAINER-->
            <div class="container-fluid">
                <!-- BEGIN PAGE HEADER-->
                <div class="row-fluid">
                    <div class="span12">
                        <ul class="breadcrumb">
                            <li>
                                <i class="icon-home"></i>
                                <a href="index.html">Home</a>
                                <span class="icon-angle-right"></span>
                            </li>
                            <li><a href="#">详细回测</a></li>
                        </ul>
                    </div>
                </div>
                <!-- END PAGE HEADER-->
                <!-- BEGIN PAGE CONTENT-->
                <div id="splitter-pane" class="splitter-pane">
                <div id="showChart" style="width: 1100px; height: 600px; ">
<?php
$xx = exec("python ../code/main.py 2>&1", $array, $ans);
var_dump($array);
// foreach ($array as $key => $value) {
//  echo $value;
// }

$chartJson = json_decode(end($array), true);
// echo "1";
?>
                    <script type="text/javascript">
                    var myChart = echarts.init(document.getElementById("showChart"));
                    var option = {
                        title: {
                            text: '投资金额视图'
                        },
                        tooltip: {},
                        legend: {
                            data: ["金额"]
                        },
                        xAxis: {
                            data: <?php echo "['" . implode("','", $chartJson["date"]) . "']"; ?>
                        },
                        yAxis: {
                            precision: 1,
                            power: 1,
                            scale: true,
                            type: 'value'
                        },
                        series: [{
                            name: '金额',
                            type: 'line',
                            data: <?php echo "[" . implode(",", $chartJson["val"]) . "]"; ?>
                        }]
                    };
                    myChart.setOption(option);
                    </script>
                </div>

</div>

                <!-- END PORTLET-->
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
    <!-- END FOOTER -->
    <!-- BEGIN JAVASCRIPTS(Load javascripts at bottom, this will reduce page load time) -->
    <!-- BEGIN CORE PLUGINS -->

    <!-- END JAVASCRIPTS -->
    <!-- END BODY -->

</html>
