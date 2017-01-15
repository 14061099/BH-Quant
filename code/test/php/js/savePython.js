var dates = [];
var fees = [];

function showChart() {
    // alert("zzz");
    getusers();


    // 将配置项赋给chart对象，来显示相关的数据
    mychart.setOption(option);
    // alert("aaa");
}

function savePython() {
    var x = editor.getValue();
    console.log(x);
    $.ajax({
        type: "post",
        async: false,
        url: "./php/savePy.php",
        data: { text: x },
        dataType: "json",
        success: function(result) {
            if (result) {
                // for (var i = 0; i < result.length; i++) {
                //     dates.push(result[i].name);
                //     fees.push(result[i].age);
                // }
                for (var key in result) {
                    console.log(key);
                    dates.push(key);
                    fees.push(result[key]);
                }
            }
        },
        error: function(errmsg) {}
    });
    return dates, fees;
}
