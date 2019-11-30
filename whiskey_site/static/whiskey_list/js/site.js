$(document).ready( function () {

    $('#spirit_table').DataTable({
        paging:   false,
        order: [[ 0, "asc" ]],
        scrollX: true, 
        dom: '<lfi<t>>',
        language: {
            searchPlaceholder: "Search whiskies (and rums!)",
            search: "",
            zeroRecords: "I don't own this...yet!",
            infoEmpty: "Showing 0 whiskies?!? How can this be??",
            info: "Showing _TOTAL_ of _MAX_ whiskies",
            infoFiltered:   "",
        },
        columnDefs: [ {
            targets: [ 0 ],
            orderData: [ 0, 1, 2 ]
        }, {
            targets: [ 1 ],
            orderData: [ 0, 1 , 2]
        } ]
    })
});