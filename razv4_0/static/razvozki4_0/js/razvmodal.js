const modal = document.querySelector("#razvModal");
const clickElements = document.querySelectorAll(".edit-modal");

function inputs(modal) {
    return {
        id: modal.querySelector('#razv_id'),
        address: modal.querySelector("#address"),
        contact: modal.querySelector('#contact'),
        customer_id: modal.querySelector("#customer_id"),
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
        inputs(modal)[key].textContent = modalData[key] || "";
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
            let razvozka = { date_id: 1};
            if (razvId != null) {
                razvozka = JSON.parse(await fetchJsonData(jsonUrl));
            } else if (razvDate != null) {
                razvozka = {
                    date: razvDate,
                    date_id: await fetchJsonData('/rzv/json_date_id/' + razvDate )
                };
            }

            const titleText = razvId == null ? 'Новая развозка' : 'Редактировать развозку';

            openEditModal(titleText, razvozka);
        }
    )
    ;
});
