$(document).ready(function(){		
    $('#addTeacher').click(function(){
        $('#teacherModal').modal({
            backdrop: 'static',
            keyboard: false
        });		
        $("#teacherModal").on("shown.bs.modal", function () {
            $('#teacherForm')[0].reset();
            $('.modal-title').html("<i class='fa fa-plus'></i> Add Teacher");
            $('#action').val('addTeacher');
            $('#save').val('Save');
        });
    });

    // Initialize select2 for specialization dropdown
    $('#specialization').select2({
        placeholder: "Select specialization",
        allowClear: true
    });
});