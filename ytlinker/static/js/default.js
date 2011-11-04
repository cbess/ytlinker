$(function() {
    // handle clear clicks
    $('a.clear').click(function() {
        // clear fields specified in the clicked tag's `field` attribute
        $($(this).attr('field')).val('');
    });
});