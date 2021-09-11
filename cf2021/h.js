let items = [
    {
       "id" : 0,
       "quantity" : 10**-2
    },
]

$.ajax({
    type: "POST",
    url: "/donate",
    data: JSON.stringify({"items": items}),
    contentType: "application/json",
    success: (data) => {
        $("#form-donation").hide()
        $("#receipt").fadeIn(500)
        $("input").val(0)

        parseData(data)
    },
    dataType: "json"
});