/**
* Created by wangxingyao on 2017/7/13.
*/

/* 标签式单文件引入方式 */
var myChart = echarts.init(document.getElementById('main'));
var idcList = ['北京', '南京', '青岛','无锡','武汉'];
var index = 0;  // 使得 idcList 中的多个 idc 可以循环切换


function fresh(datas, datasmax) {
    option = {
        backgroundColor: '#1b1b1b',
        color: ['lime'],
        title : {
            text: '网络观测-丢包',
            x:'center',
            textStyle : {
                color: '#fff'
            }
        },
        tooltip : {
            trigger: 'item',
            formatter: '{b}'
        },
        legend: {
            orient: 'vertical',
            x:'left',
            data: idcList,
            selectedMode: 'single',
            selected:{
                '北京':  false,
                '南京' : false,
                '青岛' : false,
                '无锡' : false,
                '武汉' : false
            },
            textStyle : {
                color: '#fff'
            }
        },
        toolbox: {
            show : true,
            orient : 'vertical',
            x: 'right',
            y: 'center',
            feature : {
                mark : {show: true},
                dataView : {show: true, readOnly: false},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        dataRange: {
            x: 'left',
            y: 'bottom',
            calculable : false,
            splitList: [
                {start: 0, end: 3, color: '#00EE00'},
                {start: 3, end: 10, color:'orange'},
                {start: 10, color:'red'},
            ],
            textStyle:{
                color:'#fff'
            }
        },
        series : [
            {
                name: '全国',
                type: 'map',
                roam: true,
                hoverable: false,
                mapType: 'china',
                itemStyle:{
                    normal:{
                        borderColor:'rgba(100,149,237,1)',
                        borderWidth:0.5,
                        areaStyle:{
                            color: '#1b1b1b'
                        }
                    }
                },
                data:[],
                markLine : {
                    smooth:true,
                    symbol: ['none', 'circle'],
                    symbolSize : 1,
                    itemStyle : {
                        normal: {
                            color:'#fff',
                            borderWidth:1,
                            borderColor:'rgba(30,144,255,0.5)'
                        }
                    },
                    data : [
                        [{name:'北京'},{name:'南京'}],
                        [{name:'北京'},{name:'青岛'}],
                        [{name:'北京'},{name:'无锡'}],
                        [{name:'北京'},{name:'武汉'}],
                        [{name:'北京'},{name:'廊坊'}],
                        [{name:'北京'},{name:'西安'}],

                        [{name:'南京'},{name:'北京'}],
                        [{name:'南京'},{name:'青岛'}],
                        [{name:'南京'},{name:'无锡'}],
                        [{name:'南京'},{name:'武汉'}],
                        [{name:'南京'},{name:'廊坊'}],
                        [{name:'南京'},{name:'西安'}],

                        [{name:'青岛'},{name:'北京'}],
                        [{name:'青岛'},{name:'南京'}],
                        [{name:'青岛'},{name:'无锡'}],
                        [{name:'青岛'},{name:'武汉'}],
                        [{name:'青岛'},{name:'廊坊'}],
                        [{name:'青岛'},{name:'西安'}]
                    ],
                },
                geoCoord: {
                    '上海': [121.4648,31.2891],
                    '东莞': [113.8953,22.901],
                    '东营': [118.7073,37.5513],
                    '中山': [113.4229,22.478],
                    '临汾': [111.4783,36.1615],
                    '临沂': [118.3118,35.2936],
                    '丹东': [124.541,40.4242],
                    '丽水': [119.5642,28.1854],
                    '乌鲁木齐': [87.9236,43.5883],
                    '佛山': [112.8955,23.1097],
                    '保定': [115.0488,39.0948],
                    '兰州': [103.5901,36.3043],
                    '包头': [110.3467,41.4899],
                    '北京': [116.4551,40.2539],
                    '北海': [109.314,21.6211],
                    '南京': [118.8062,31.9208],
                    '南宁': [108.479,23.1152],
                    '南昌': [116.0046,28.6633],
                    '南通': [121.1023,32.1625],
                    '厦门': [118.1689,24.6478],
                    '台州': [121.1353,28.6688],
                    '合肥': [117.29,32.0581],
                    '呼和浩特': [111.4124,40.4901],
                    '咸阳': [108.4131,34.8706],
                    '哈尔滨': [127.9688,45.368],
                    '唐山': [118.4766,39.6826],
                    '嘉兴': [120.9155,30.6354],
                    '大同': [113.7854,39.8035],
                    '大连': [122.2229,39.4409],
                    '天津': [117.4219,39.4189],
                    '太原': [112.3352,37.9413],
                    '威海': [121.9482,37.1393],
                    '宁波': [121.5967,29.6466],
                    '宝鸡': [107.1826,34.3433],
                    '宿迁': [118.5535,33.7775],
                    '常州': [119.4543,31.5582],
                    '广州': [113.5107,23.2196],
                    '廊坊': [116.521,39.0509],
                    '延安': [109.1052,36.4252],
                    '张家口': [115.1477,40.8527],
                    '徐州': [117.5208,34.3268],
                    '德州': [116.6858,37.2107],
                    '惠州': [114.6204,23.1647],
                    '成都': [103.9526,30.7617],
                    '扬州': [119.4653,32.8162],
                    '承德': [117.5757,41.4075],
                    '拉萨': [91.1865,30.1465],
                    '无锡': [120.3442,31.5527],
                    '日照': [119.2786,35.5023],
                    '昆明': [102.9199,25.4663],
                    '杭州': [119.5313,29.8773],
                    '枣庄': [117.323,34.8926],
                    '柳州': [109.3799,24.9774],
                    '株洲': [113.5327,27.0319],
                    '武汉': [114.3896,30.6628],
                    '汕头': [117.1692,23.3405],
                    '江门': [112.6318,22.1484],
                    '沈阳': [123.1238,42.1216],
                    '沧州': [116.8286,38.2104],
                    '河源': [114.917,23.9722],
                    '泉州': [118.3228,25.1147],
                    '泰安': [117.0264,36.0516],
                    '泰州': [120.0586,32.5525],
                    '济南': [117.1582,36.8701],
                    '济宁': [116.8286,35.3375],
                    '海口': [110.3893,19.8516],
                    '淄博': [118.0371,36.6064],
                    '淮安': [118.927,33.4039],
                    '深圳': [114.5435,22.5439],
                    '清远': [112.9175,24.3292],
                    '温州': [120.498,27.8119],
                    '渭南': [109.7864,35.0299],
                    '湖州': [119.8608,30.7782],
                    '湘潭': [112.5439,27.7075],
                    '滨州': [117.8174,37.4963],
                    '潍坊': [119.0918,36.524],
                    '烟台': [120.7397,37.5128],
                    '玉溪': [101.9312,23.8898],
                    '珠海': [113.7305,22.1155],
                    '盐城': [120.2234,33.5577],
                    '盘锦': [121.9482,41.0449],
                    '石家庄': [114.4995,38.1006],
                    '福州': [119.4543,25.9222],
                    '秦皇岛': [119.2126,40.0232],
                    '绍兴': [120.564,29.7565],
                    '聊城': [115.9167,36.4032],
                    '肇庆': [112.1265,23.5822],
                    '舟山': [122.2559,30.2234],
                    '苏州': [120.6519,31.3989],
                    '莱芜': [117.6526,36.2714],
                    '菏泽': [115.6201,35.2057],
                    '营口': [122.4316,40.4297],
                    '葫芦岛': [120.1575,40.578],
                    '衡水': [115.8838,37.7161],
                    '衢州': [118.6853,28.8666],
                    '西宁': [101.4038,36.8207],
                    '西安': [109.1162,34.2004],
                    '贵阳': [106.6992,26.7682],
                    '连云港': [119.1248,34.552],
                    '邢台': [114.8071,37.2821],
                    '邯郸': [114.4775,36.535],
                    '郑州': [113.4668,34.6234],
                    '鄂尔多斯': [108.9734,39.2487],
                    '重庆': [107.7539,30.1904],
                    '金华': [120.0037,29.1028],
                    '铜川': [109.0393,35.1947],
                    '银川': [106.3586,38.1775],
                    '镇江': [119.4763,31.9702],
                    '长春': [125.8154,44.2584],
                    '长沙': [113.0823,28.2568],
                    '长治': [112.8625,36.4746],
                    '阳泉': [113.4778,38.0951],
                    '青岛': [120.4651,36.3373],
                    '韶关': [113.7964,24.7028]
                }
            },
            {
                name: '北京',
                type: 'map',
                mapType: 'china',
                data:[],
                markLine : {
                    smooth:true,
                    effect : {
                        show: true,
                        scaleSize: 1,
                        period: 30,
                        color: '#fff',
                        shadowBlur: 10
                    },
                    itemStyle : {
                        normal: {
                            borderWidth:1,
                            lineStyle: {
                                type: 'solid',
                                shadowBlur: 10
                            }
                        }
                    },
                    data : [
                        [{name:'北京'}, {name:'南京',value:datas['bjnj']}],
                        [{name:'北京'}, {name:'青岛',value:datas['bjqd']}],
                        [{name:'北京'}, {name:'无锡',value:datas['bjwx']}],
                        [{name:'北京'}, {name:'武汉',value:datas['bjwh']}],
                        [{name:'北京'}, {name:'廊坊',value:datas['bjlf']}],
                        [{name:'北京'}, {name:'西安',value:datas['bjxa']}]
                    ]
                },
                markPoint : {
                    symbol:'emptyCircle',
                    symbolSize : function (v){
                        return 10 + v/10
                    },
                    effect : {
                        show: true,
                        shadowBlur : 0
                    },
                    itemStyle:{
                        normal:{
                            label:{show:false}
                        },
                        emphasis: {
                            label:{position:'top'}
                        }
                    },
                    data : [
                            {name:'南京',value:datasmax['bjnj']},
                            {name:'青岛',value:datasmax['bjqd']},
                            {name:'无锡',value:datasmax['bjwx']},
                            {name:'武汉',value:datasmax['bjwh']},
                            {name:'廊坊',value:datasmax['bjlf']},
                            {name:'西安',value:datasmax['bjxa']}
                    ]
                }
            },
            {
                name: '南京',
                type: 'map',
                mapType: 'china',
                data:[],
                markLine : {
                    smooth:true,
                    effect : {
                        show: true,
                        scaleSize: 1,
                        period: 30,
                        color: '#fff',
                        shadowBlur: 10
                    },
                    itemStyle : {
                        normal: {
                            borderWidth:1,
                            lineStyle: {
                                type: 'solid',
                                shadowBlur: 10
                            }
                        }
                    },
                    data : [
                        [{name:'南京'},{name:'北京',value:datas['njbj']}],
                        [{name:'南京'},{name:'无锡',value:datas['njwx']}],
                        [{name:'南京'},{name:'武汉',value:datas['njwh']}],
                        [{name:'南京'},{name:'廊坊',value:datas['njlf']}],
                        [{name:'南京'},{name:'西安',value:datas['njxa']}]
                    ]
                },
                markPoint : {
                    symbol:'emptyCircle',
                    symbolSize : function (v){
                        return 10 + v/10
                    },
                    effect : {
                        show: true,
                        shadowBlur : 0
                    },
                    itemStyle:{
                        normal:{
                            label:{show:false}
                        },
                        emphasis: {
                            label:{position:'top'}
                        }
                    },
                    data : [
                            {name:'北京',value:datasmax['njbj']},
                            {name:'无锡',value:datasmax['njwx']},
                            {name:'武汉',value:datasmax['njwh']},
                            {name:'廊坊',value:datasmax['njlf']},
                            {name:'西安',value:datasmax['njxa']}
                    ]
                }
            },
            {
                name: '无锡',
                type: 'map',
                mapType: 'china',
                data:[],
                markLine : {
                    smooth:true,
                    effect : {
                        show: true,
                        scaleSize: 1,
                        period: 30,
                        color: '#fff',
                        shadowBlur: 10
                    },
                    itemStyle : {
                        normal: {
                            borderWidth:1,
                            lineStyle: {
                                type: 'solid',
                                shadowBlur: 10
                            }
                        }
                    },
                    data : [
                        [{name:'无锡'}, {name:'南京',value:datas['wxnj']}],
                        [{name:'无锡'}, {name:'青岛',value:datas['wxqd']}],
                        [{name:'无锡'}, {name:'北京',value:datas['wxbj']}],
                        [{name:'无锡'}, {name:'武汉',value:datas['wxwh']}],
                        [{name:'无锡'}, {name:'廊坊',value:datas['wxlf']}],
                        [{name:'无锡'}, {name:'西安',value:datas['wxxa']}]
                    ]
                },
                markPoint : {
                    symbol:'emptyCircle',
                    symbolSize : function (v){
                        return 10 + v/10
                    },
                    effect : {
                        show: true,
                        shadowBlur : 0
                    },
                    itemStyle:{
                        normal:{
                            label:{show:false}
                        },
                        emphasis: {
                            label:{position:'top'}
                        }
                    },
                    data : [
                            {name:'南京',value:datasmax['wxnj']},
                            {name:'青岛',value:datasmax['wxqd']},
                            {name:'北京',value:datasmax['wxbj']},
                            {name:'武汉',value:datasmax['wxwh']},
                            {name:'廊坊',value:datasmax['wxlf']},
                            {name:'西安',value:datasmax['wxxa']}
                    ]
                }
            },
            {
                name: '武汉',
                type: 'map',
                mapType: 'china',
                data:[],
                markLine : {
                    smooth:true,
                    effect : {
                        show: true,
                        scaleSize: 1,
                        period: 30,
                        color: '#fff',
                        shadowBlur: 10
                    },
                    itemStyle : {
                        normal: {
                            borderWidth:1,
                            lineStyle: {
                                type: 'solid',
                                shadowBlur: 10
                            }
                        }
                    },
                    data : [
                        [{name:'武汉'}, {name:'南京',value:datas['whnj']}],
                        [{name:'武汉'}, {name:'青岛',value:datas['whqd']}],
                        [{name:'武汉'}, {name:'无锡',value:datas['whwx']}],
                        [{name:'武汉'}, {name:'北京',value:datas['whbj']}],
                        [{name:'武汉'}, {name:'廊坊',value:datas['whlf']}],
                        [{name:'武汉'}, {name:'西安',value:datas['whxa']}]
                    ]
                },
                markPoint : {
                    symbol:'emptyCircle',
                    symbolSize : function (v){
                        return 10 + v/10
                    },
                    effect : {
                        show: true,
                        shadowBlur : 0
                    },
                    itemStyle:{
                        normal:{
                            label:{show:false}
                        },
                        emphasis: {
                            label:{position:'top'}
                        }
                    },
                    data : [
                            {name:'南京',value:datasmax['whnj']},
                            {name:'青岛',value:datasmax['whqd']},
                            {name:'无锡',value:datasmax['whwx']},
                            {name:'北京',value:datasmax['whbj']},
                            {name:'廊坊',value:datasmax['whlf']},
                            {name:'西安',value:datasmax['whxa']}
                    ]
                }
            },
            {
                name: '青岛',
                type: 'map',
                mapType: 'china',
                data:[],
                markLine : {
                    smooth:true,
                    effect : {
                        show: true,
                        scaleSize: 1,
                        period: 30,
                        color: '#fff',
                        shadowBlur: 10
                    },
                    itemStyle : {
                        normal: {
                            borderWidth:1,
                            lineStyle: {
                                type: 'solid',
                                shadowBlur: 10
                            }
                        }
                    },
                    data : [
                            [{name:'青岛'},{name:'北京',value:datas['qdbj']}],
                            [{name:'青岛'},{name:'无锡',value:datas['qdwx']}],
                            [{name:'青岛'},{name:'武汉',value:datas['qdwh']}],
                            [{name:'青岛'},{name:'廊坊',value:datas['qdlf']}]
                    ]
                },
                markPoint : {
                    symbol:'emptyCircle',
                    symbolSize : function (v){
                        return 10 + v/10
                    },
                    effect : {
                        show: true,
                        shadowBlur : 0
                    },
                    itemStyle:{
                        normal:{
                            label:{show:false}
                        },
                        emphasis: {
                            label:{position:'top'}
                        }
                    },
                    data : [
                            {name:'北京',value:datasmax['qdbj']},
                            {name:'无锡',value:datasmax['qdwx']},
                            {name:'武汉',value:datasmax['qdwh']},
                            {name:'廊坊',value:datasmax['qdlf']}
                    ]
                }
            }
        ]
    };

    var idc = idcList[index];
    option.legend.selected[idc.toString()] = 'true';
    index++;
    index %= idcList.length;

    myChart.clear();
    myChart.setOption(option);
}

function refresh() {
    $.ajax({
        type: 'get',
        url: '/netmanage/get_net_loss',
        data: {'arg': 'test'},
        async: false,
        dataType: 'json',
        success: function(result) {
            console.log('refresh() ajax() success');
            var datas = result['loss'];
            var datasmax = result['max'];
            var warnlog = result['warnlog']
            fresh(datas, datasmax);
            if (warnlog.length>0){
                //alert(warnlog);
                htmlstart="<table border=1><thead><tr><th>源IDC</th><th>源IP</th><th>目的IDC</th><th>目的IP</th><th>丢包率</th></tr></thead>";
                htmlcontent="";
                html="";
                for (i = 0; i < warnlog.length; i++){
                    r=warnlog[i];
                    //alert(warnlog.length);
                    htmlcontent = htmlcontent+"<tr><td>"+r[0]+"</td><td>"+r[1]+"</td><td>"+r[2]+"</td><td>"+r[3]+"</td><td>"+r[4]+"</td></tr>"
                    if (r[4] >=10 ){
                        sound=1;
                        //sound=sound+1;
                        //counttime=counttime+1;
                    }
                }
                //丢包率大于10%会声音报警
                if (sound == 1&&counttime == 0){
                    document.getElementById("sound").src="/static/sound.wav";
                    //sound=sound+1;
                    counttime=counttime+1;
                }
                html = htmlstart+htmlcontent+"</table>" ;

                $("#warn").html(html)
            }
            else{
                $("#warn").empty();
                sound=0;
                counttime=0;
            }
        },
        error: function() {
            alert('refresh() ajax() error');
        }
    });
}

setInterval(refresh, 10000);

refresh()
