$(document).ready( function () {

    // Sums a column
    jQuery.fn.dataTable.Api.register( 'sum()', function ( ) {
        return this.flatten().reduce( function ( a, b ) {
            if ( typeof a === 'string' ) {
                a = a.replace(/[^\d.-]/g, '') * 1;
            }
            if ( typeof b === 'string' ) {
                b = b.replace(/[^\d.-]/g, '') * 1;
            }
            return a + b;
        }, 0 );
    } );
    
    var table = $('#spirit_table').DataTable({
        paging:   false,
        order: [[ 0, "asc" ]],
        scrollX: true, 
        dom: '<lf<i<"#total_whiskies">><t>>',
        language: {
            searchPlaceholder: "Search whiskies (and rums!)",
            search: "",
            zeroRecords: "I don't own this...yet!",
            infoEmpty: "Showing 0 whiskies?!? How can this be??",
            info: "Showing _TOTAL_ of _MAX_ unique whiskies",
            infoFiltered:   "",
        },
        columnDefs: [ {
            targets: [ 0 ],
            orderData: [ 0, 1, 2 ]
        }, {
            targets: [ 1 ],
            orderData: [ 1, 2, 0]
        },{
            targets: [ 2 ],
            orderData: [ 2, 1, 0]
        }]
    });

});