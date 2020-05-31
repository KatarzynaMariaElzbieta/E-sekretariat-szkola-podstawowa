
var child_residential_address = document.getElementById('child_residential_address');
console.log(child_residential_address)

document.addEventListener("DOMContentLoaded", function () {

    var child_residential_address = document.getElementById('child_residential_address');
    var checkbox = document.getElementByTagName("residential_like_permanent");
    checkbox.addEventListener('click', function(){
        child_residential_address.parentElement.removeChild(child_residential_address);
    });
});