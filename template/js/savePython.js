function savePython() {
    var x = editor.getValue();
    var pyname = $(".algo-title").html();
    // console.log(x);
    console.log(pyname);
    $.ajax({
        type: "post",
        async: false,
        url: "./savePy.php",
        data: { "text": x, "pyname": pyname },
        dataType: "",
        success: function(result) {
            if (result) {
                // for (var i = 0; i < result.length; i++) {
                //     dates.push(result[i].name);
                //     fees.push(result[i].age);
                // }
                // for (var key in result) {
                //     console.log(result[key]);
                // }
                console.log(result);
            }
        },
        error: function(errmsg) {}
    });
    console.log("xxx");
}
