
let basket = []


// Add to basket button
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.addSubmitSingle').forEach(function(button) {
    button.onclick = function() {
        let mainchoice = JSON.parse(button.value.replaceAll("'", "\""));
        createBasketItem(mainchoice);
    }
    });
});

// Clear the basket
function clear_basket () {
    console.log("hello");
    basket = [];
    document.querySelector('#basket').innerHTML = "";
    totaliser();
};

// Launch the start pop up
document.addEventListener('DOMContentLoaded', function() {
    var myModal = bootstrap.Modal.getOrCreateInstance(document.getElementById('launchModal'));
    myModal.show();
});


// Select subchoices
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.addSubmitVariation').forEach(function(button) {
    button.onclick = function() {
        let selectedVars = document.querySelectorAll('.variationRadio')
        let mainchoice = document.querySelector('#mainChoice').value
        let subchoice = {"main_id": mainchoice}
        for (const selectedVar of selectedVars) {
        if (selectedVar.checked) {
            $.extend(subchoice, JSON.parse(selectedVar.value.replaceAll("'", "\"")));
            selectedVar.checked = false;
            createBasketItem(subchoice)
            break;
        }
        }
    }
    });
});


// Create and remove basket items
function createBasketItem(new_item) {

    basket.push(new_item);
        
    var li = document.createElement("li");
    li.classList.add("d-flex");
    li.classList.add("list-group-item");
    let price = new_item["price"] / 100
    li.innerHTML = `
    <div class="flex-fill py-1">${new_item["name"]}</div>
    <div class="py-1">£${price.toFixed(2)}</div>`;

    var rmBtn = document.createElement("Button");
    rmBtn.classList.add("btn");
    rmBtn.classList.add("btn-link");
    rmBtn.classList.add("ps-1");
    rmBtn.value = `${new_item["id"]}`;
    rmBtn.innerHTML = `<h3><i class="bi bi-dash-circle ps-1"></i></h3>`;
    li.appendChild(rmBtn);
    rmBtn.addEventListener('click', function (e) {
        for (let i = 0; i < basket.length ; i++) {
            if (basket[i]["id"] === rmBtn.value) {
                basket.splice(i, 1);
                break;
            };
        };
        this.parentNode.parentNode.removeChild(this.parentNode);
        totaliser();
    });
    
    document.querySelector('#basket').append(li);
    console.log(basket)

    totaliser();
}


// Totaliser
function totaliser() {
    let total_sum = 0
    for (let item of basket) {
    total_sum += item["price"]
    }
    total_sum = total_sum / 100;
    document.querySelector('#total').innerHTML = `Total: £${total_sum.toFixed(2)}`
}

// Checkout and pay
function checkout() {
    $.ajax({
        type: "POST",
        url: "/checkout",
        data: JSON.stringify(basket),
        contentType: "application/json",
        dataType: 'json',
        success: function(result) {
            var myModal = bootstrap.Modal.getOrCreateInstance(document.getElementById('payModal'));
            myModal.hide();
            clear_basket();
            var myModal = bootstrap.Modal.getOrCreateInstance(document.getElementById('launchModal'));
            myModal.show();
          } 
      });
}

// Cancel payment 
function cancelOrder() {
    $.ajax({
        type: "GET",
        url: "/cancelchkout",
      });
    clear_basket();
}