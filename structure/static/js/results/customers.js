let resultsTable = $("#results-table-dt").DataTable({
    dom: '<"row mb-2"<"col-12"l>>rBftip',
    
    ajax: {
        // url: function (data) {
        //     // Get the ID from the URL
        //     let id = window.location.pathname.split('/').pop();

        //     // Construct the API URL with the ID
        //     return `/studentapi/${id}`;
        // },
        url: "/customersapi"
    },
    processing: true,
    language: {
        processing: 'Loading results...',
    },
    columnDefs: [{
        orderable: false,
        className: 'select-checkbox',
        targets: 0
    }],
    select: {
        style: 'multi+shift',
        selector: 'td:first-child',
        info: true,
    },
    columns: [
        {
            data: null,
            render: function render(data, type, row, meta) {
                return '';
            }
        },
        {
            data: 'name',
        },
        {
            data: 'credit',
        },
        {
            data: 'ip',
        },
        {
            data: 'debit_limit',
        }
       
    ],
    buttons: [
        {
            extend: 'print',
            exportOptions: {
                columns: [1, 2, 3, 4, 5, 6, 7, 8],
            }
        },
        {
            extend: 'csv',
            exportOptions: {
                columns: [1, 2, 3, 4, 5, 6, 7, 8],
            }
        },
        {
            extend: 'pdf',
            exportOptions: {
                columns: [1, 2, 3, 4, 5, 6, 7, 8],
            }
        },
        {
            extend: 'selectNone',
            name: 'selectNone',
        },
        {
            extend: '',
            text: 'Refresh Table',
            action: function (e, table, button, config) {
                table.ajax.reload(null, false);
            }
        },
        {
            extend: 'selected',
            text: 'Edit Customer',
            action: function (e, table, button, config) {
                let selectedRows = table.rows({selected: true});
                if (selectedRows.count() !== 1) {
                    alert("Sorry, you can only edit one result. Kindly select only one result");
                    return;
                }
                let data = table.row(selectedRows.indexes()[0]).data();
                $("#edit-result-form").attr("action", `/editsiprequest/${data.id}`);
                $("#edit-result-id").val(data.id);
                $("#edit-result-channels").val(data.channels);
                $("#edit-result-provider").val(data.provider);
                $("#edit-result-codecs").val(data.codecs);
                $("#edit-result-certificate").val(data.certificate);
                $("#edit-result-status").val(data.status);
                $("#edit-result-ip").val(data.ip);
                $('#editResultModal').modal('show');
            }
        },
     
        {
            extend: 'selected',
            text: 'Delete',
            attr: {
                class: 'ml-2 btn btn-sm btn-danger',
            },
            action: function (e, table, button, config) {
                let selectedRows = table.rows({selected: true}).indexes();
                let resultIds = [];
                Array.from(selectedRows).forEach((rowIndex) => {
                    let data = table.row(rowIndex).data();
                    resultIds.push(data.id);
                });

                if (confirm("Are you sure you want to delete?")) {
                    fetch(`/api/delete_siprequests?siprequests=${resultIds.join(',')}`)
                        .then(res => res.json())
                        .then(payload => {
                            Array.from(selectedRows).forEach((row) => {
                                table.row(row).remove().draw();
                                table.ajax.reload(null, false);
                            });
                        });
                }
            }
        },
    ],
});




