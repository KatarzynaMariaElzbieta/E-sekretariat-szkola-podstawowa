$(function () {
    //Pola dodatkowe
    function extra_field() {
        var checkbox = document.getElementById('residental_like_pernament');
        var f = $('#child_residential_address').detach()
        checkbox.addEventListener('click', function () {
            if ($('#child_residential_address').length == 0) {
                f.insertAfter(checkbox)
                validate_postcodes()
                console.log('tu')

            } else {
                $('#child_residential_address').detach()
            }
        });

        var checkbox2 = document.getElementById('mother_address_like_child');
        var f2 = $('#mother_residental_address').detach()
        checkbox2.addEventListener('click', function () {
            if ($('#mother_residental_address').length == 0) {
                f2.insertAfter(checkbox2)
                validate_postcodes()
            } else {
                $('#mother_residental_address').detach()
            }
        });

        var checkbox3 = document.getElementById('father_address_like_child');
        var f3 = $('#father_residental_address').detach()
        checkbox3.addEventListener('click', function () {
            if ($('#father_residental_address').length == 0) {
                f3.insertAfter(checkbox3)
                validate_postcodes()

            } else {
                $('#father_residental_address').detach()
            }
        });

        var checkbox4 = document.getElementById('id_recruiment-no_catchment_area');
        var f4 = $('#no_catchment_area_information_form').detach()
        checkbox4.addEventListener('click', function () {
            if ($('#no_catchment_area_information_form').length == 0) {
                f4.insertAfter(checkbox4.nextElementSibling)
            } else {
                f4 = $('#no_catchment_area_information_form').detach()
            }
        });
    }

    var button = document.querySelector('#submit');

    function validate_pesel() {
        //Walidacja peselu
        var pesel = document.querySelector('#id_recruiment-PESEL');
        var regPesel = /^\d+$/
        pesel.addEventListener('blur', function (e) {
            pesel.nextSibling.remove()
            if (pesel.value.length == 11 && regPesel.test(pesel.value)) {
                if (pesel.nextSibling) {

                }
            } else {
                console.log(regPesel.test(pesel.value))
                pesel.after("Pesel nieprawidłowy")
                button.addEventListener('click', function (s) {
                    return false
                })
            }
        })
    }

    //Walidacja daty urodzenia
    function validate_birthdate() {
        var birthdate = document.querySelector('#id_recruiment-birthdate');
        console.log(birthdate)

        var regbirthdate = /^(0[1-9]|[1-2][0-9]|3[0-1])[-](0[1-9]|1[0-2])[-](20)\d\d$/i
        birthdate.addEventListener('blur', function (e) {
            if (birthdate.nextSibling) birthdate.nextSibling.remove()
            if (regbirthdate.test(birthdate.value)) {
                if (birthdate.nextSibling) {
                }
            } else {
                console.log(regbirthdate.test(birthdate.value))
                birthdate.after("Data nieprawidłowa")
                button.addEventListener('click', function (s) {
                    return false

                })
            }
        })
    }

    //Walidacja numeru telefonu
    function phone_number() {
        var phone = document.querySelectorAll('.phone');
        console.log(phone)
        var regphone = /[\d]{9}/;
        $('.phone').on('blur', function (event) {
            if (event.target.nextSibling) {
                event.target.nextSibling.remove()
            }

            if (regphone.test(event.target.value)) {
                if (event.target.nextSibling) {
                    console.log('phone')
                }
            } else {
                console.log(regphone.test(event.target.value))
                console.log('ko')


                event.target.after("Numer nieprawidłowy")
                button.addEventListener('click', function (s) {
                    // s.preventDefault()
                    return false

                })
            }
        })
    }

    function validate_postcodes() {
        var post_codes = document.querySelectorAll('.postcode');
        console.log(post_codes)
        console.log('tu2')
        var regpost_code = /[\d]{2}-[\d]{3}/g;
        $('.postcode').on('blur', function (event) {
            if (event.target.nextSibling) event.target.nextSibling.remove()
            if (regpost_code.test(event.target.value)) {
                if (event.target.nextSibling) {
                    console.log('postcode')
                }
            } else {
                console.log(regpost_code.test(event.target.value))
                console.log('ko')


                event.target.after("Kod nieprawidłowy")
                button.addEventListener('click', function (s) {
                    // s.preventDefault()
                    return false

                })
            }
        })
    }


    extra_field()
    validate_pesel()
    phone_number()
// validate_birthdate()
    validate_postcodes()
});

