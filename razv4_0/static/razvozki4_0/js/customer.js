const modal = document.querySelector('#customerModal');
const table = document.querySelector('#render');

function inputs(modal) {
    return {
        id: modal.querySelector('#cst_id'),
        name: modal.querySelector("#name"),
        address: modal.querySelector("#address"),
        contact: modal.querySelector('#contact'),
        subcontractor: modal.querySelector('#subcontractor'),
    }
}

async function openCustomerModal(titleText, modalData) {
    const modalTitle = modal.querySelector("#modal-title");
    modalTitle.textContent = titleText;
    for (const key in inputs(modal)) {
        inputs(modal)[key].value = modalData[key];
    }
    modal.style.display = "block";
}

async function prepareToEditCustomer(element){
        const cstId = element.dataset.id;
        const jsonUrl = '/rzv/json_customer_select/' + cstId;
        let customer = {name: null, address:null, contact:null, subcontractor: false};
        if (cstId != null) {
            customer = JSON.parse(await fetchJsonData(jsonUrl));
        }
        const titleText = cstId == null ? 'Новый клиент' : 'Редактировать клиента';
        openCustomerModal(titleText, customer);
}

table.addEventListener("click", async (event) => {
    const target = event.target;
    const element = target.closest(".cst-modal");
    if (element && table.contains(element)) {
        await prepareToEditCustomer(element);
    }
});


