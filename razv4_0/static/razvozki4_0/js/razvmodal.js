const modal = document.querySelector("#razvModal");
const clickElements = document.querySelectorAll(".edit-modal");

function inputs(modal) {
    return {
        id: modal.querySelector('#razv_id'),
        address: modal.querySelector("#address"),
        contact: modal.querySelector('#contact'),
        customer_id: modal.querySelector("#customer_id"),
        customer_customer_name: modal.querySelector("#customer_customer_name"),
        customer_name: modal.querySelector("#customer_name"),
        date: modal.querySelector("#date"),
        date_id: modal.querySelector("#date_id"),
        date_until: modal.querySelector("#date_until"),
        map_point: modal.querySelector("#map_point"),
        to_do_deliver: modal.querySelector("#to_do_deliver"),
        to_do_take: modal.querySelector("#to_do_take"),
    };
}

function openEditModal(titleText, modalData) {
    // Populate the modal fields with the data
    const modalTitle = modal.querySelector("#modal-title");
    modalTitle.textContent = titleText;
    for (const key in inputs(modal)) {
        inputs(modal)[key].value = modalData[key] || "";
    }
    modal.style.display = "block";
    if(modalData['customer_id'] != null) {
        returnList(modalData['customer_id']);
    }
}

function fetchJsonData(jsonUrl) {
    return fetch(jsonUrl)
        .then(response => response.json());
}

clickElements.forEach(function (element) {
    element.addEventListener("click", async () => {
        const razvId = element.dataset.id;
        const razvDate = element.dataset.date;
        const jsonUrl = '/rzv/json_razvozka/' + razvId;
        let razvozka = {date_id: 1};
        if (razvId != null) {
            razvozka = JSON.parse(await fetchJsonData(jsonUrl));
            if (razvozka['customer_id'] != null) {
                const cstUrl = '/rzv/json_customer_name/' + razvozka['customer_id'];
                razvozka['customer_customer_name'] = await fetchJsonData(cstUrl);
            }
        } else if (razvDate != null) {
            razvozka = {
                date: razvDate,
                date_until: razvDate,
                date_id: await fetchJsonData('/rzv/json_date_id/' + razvDate)
            };
        }
        const titleText = razvId == null ? 'Новая развозка' : 'Редактировать развозку';
        if (!razvozka['fulfilled']) openEditModal(titleText, razvozka);
    });
});

function dropDown() {
    document.querySelector("#cstDropdown").classList.toggle("show")
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function (event) {
    if (!event.target.matches('.btn-dropdown') && !event.target.matches('#customer_customer_name')) {
        const dropdowns = document.getElementsByClassName("dropdown-content");
        let i;
        for (i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

function filterCust() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("customer_customer_name");
    filter = input.value.toUpperCase();
    const div = document.getElementById("cstDropdown");
    a = div.getElementsByTagName("li");
    for (i = 0; i < a.length; i++) {
        let txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}

async function selectCustomer(obj) {
    const custId = obj.value;
    const customerId = document.querySelector('#customer_id')
    const customerName = document.querySelector('#customer_name');
    const address = document.querySelector('#address');
    const contact = document.querySelector('#contact');
    const customer = await customerById(custId);
    customerId.value = customer['id'];
    customerName.value = customer['name'];
    address.value = customer['address'];
    contact.value = customer['contact'];
    await returnList(custId);
}

async function selectDriver(obj) {
    const driverId = obj.value;
    document.querySelector('#driver-icon').src = await fetchJsonData('/rzv/json_driver_url/' + driverId);
}

async function returnList(custId){
    const urlRazvozki = '/rzv/json_deliveries/' + custId;
    const razvozkiList = JSON.parse(await fetchJsonData(urlRazvozki));
    let optionString = '';
    if (razvozkiList.length > 0) {
        const customer = await customerById(custId);
        optionString += '<p><strong>возврат поставленого ' + customer['name'] + '</strong></p>'
    }
    let i = 0;
    razvozkiList.forEach(function (razvozka) {
        let dateRus = razvozka.fields['date'].slice(8) + '.' + razvozka.fields['date'].slice(5, 7) + '.' + razvozka.fields['date'].slice(2, 4);
        optionString += '<span><input type="checkbox" class="checkbox" name="rzv_check_' + i + '" id="rzv_check_' + i + '">' +
            '<input type="text" value="' + razvozka['pk'] + '" + name="rzv_no_' + i + '" hidden>&nbsp;' +
            '<label for="rzv_check_' + i + '">от&nbsp;<strong>' + dateRus + '</strong> ' + razvozka.fields['to_do_deliver'] + '</label></span>'
        i++;
    });
    document.querySelector('#rzv-quantity').value = razvozkiList.length;
    document.querySelector('#delivered_to_customer').innerHTML = optionString;
}

async function customerById(custId){
    const urlCustomer = '/rzv/json_customer_select/' + custId;
    return JSON.parse(await fetchJsonData(urlCustomer));
}