$(function () {
    var checkbox = document.getElementById('residental_like_pernament');
    var f = $('#child_residential_address').detach()
    checkbox.addEventListener('click', function () {
        if ($('#child_residential_address').length == 0) {
            f.insertAfter(checkbox)
        } else {
            $('#child_residential_address').detach()
        }
    });

    var checkbox2 = document.getElementById('mother_address_like_child');
    var f2 = $('#mother_residental_address').detach()
    checkbox2.addEventListener('click', function () {
        if ($('#mother_residental_address').length == 0) {
            f2.insertAfter(checkbox2)
        } else {
            $('#mother_residental_address').detach()
        }
    });

    var checkbox3 = document.getElementById('father_address_like_child');
    var f2 = $('#father_residental_address').detach()
    checkbox3.addEventListener('click', function () {
        if ($('#father_residental_address').length == 0) {
            f2.insertAfter(checkbox3)
        } else {
            $('#father_residental_address').detach()
        }
    });

    var checkbox4 = document.getElementById('id_recruiment-catchment_area');
    console.log(checkbox4)
    // var f4 = $('#no_catchment_area_information_form').detach()
    checkbox4.addEventListener('click', function () {
        if ($('#no_catchment_area_information_form').length == 0) {
            console.log('if')
            f4.insertAfter(checkbox4.nextElementSibling)
        } else {
            console.log('else')
            f4 = $('#no_catchment_area_information_form').detach()
        }
    });
});

//----------------------------------------------
//Usuwanie bez wstawiania wszystkich na raz
    // $('.address').on('click', function (event) {
    //     if ($(event.target).next().hasClass('residental_address')){
    //         var f = $(event.target).next().detach();
    //     }
    // });
// });
