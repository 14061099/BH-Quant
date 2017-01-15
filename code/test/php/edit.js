$(".algo-title").click(function(b) {
    console.log("xxxxx");
    b.stopPropagation();
    $(this).addClass("hidden");
    $(".algo-title-box").removeClass("hidden").focus().val($(".algo-title").html());
    var a = getByteLen($("#title-box").val());
    $("#title-box").width(a * 8 + "px").css({ padding: 10, "min-width": 390, "max-width": 1280 })
});
$("#title-box").keydown(function() {
    var a = getByteLen($("#title-box").val());
    $("#title-box").width(a * 8 + "px").css({ padding: 10, "min-width": 390, "max-width": 1280 })
});
$("#title-box").blur(function() {
    $(".algo-title-box").addClass("hidden");
    var a = this;
    if ($(this).val() != "") { $(".algo-title").html($(a).val()) }
    $(".algo-title").removeClass("hidden");
    $(document).attr("title", $(this).val());
    unsave()
});
