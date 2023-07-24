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
//        inputs(modal)[key].textContent = modalData[key] || "";
    }
    modal.style.display = "block";
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
    const urlCustomer = '/rzv/json_customer_select/' + custId;
    const customer = JSON.parse(await fetchJsonData(urlCustomer));
    customerId.value = customer['id'];
    customerName.value = customer['name'];
    address.value = customer['address'];
    contact.value = customer['contact'];
}