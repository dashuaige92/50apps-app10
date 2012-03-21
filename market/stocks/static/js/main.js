(function() {
    $stocks = $('ul.stocks');
    window.setInterval(function() {
        $.ajax({
            url: 'api',
            dataType: 'json',
            type: 'GET',
            success: function(results) {
                $stocks.children().each(function() {
                    $this = $(this);
                    $this.html($this.data('ticker') + ', ' +
                                results[$this.data('ticker')]);
                    //console.log(typeof(stock));
                });
            }
        })
    }, 2000);
})();
