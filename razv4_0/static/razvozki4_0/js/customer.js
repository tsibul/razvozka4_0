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

const urlList = '/rzv/json_customers_list/';
const urlLast = '/rzv/json_customers_last/';

async function customersList(lastElement, url) {
    const data = await fetchJsonData(url + lastElement);
    return JSON.parse(data);
}

table.addEventListener("mouseover", async (event) => {
        const target = event.target;
        const element = target.closest(".end-element");
        if (element && table.contains(element)) {
            await addRows(element);
        }
    }
);

async function addRows(row) {
    row.classList.remove('end-element');
    const lastElement = row.id;
    try {
        const customerList = await customersList(lastElement, urlList);
        for (const element of customerList) {
            const newRow = await buildCustomerRow(element)
            row.parentElement.appendChild(newRow);
        }
        const customerLast = await customersList(lastElement, urlLast);
        const lastRow = await buildCustomerRow(customerLast[0]);
        lastRow.classList.add('end-element');
        lastRow.id = Number(lastElement) + 50;
        await row.parentElement.appendChild(lastRow);
    } catch (error) {
        console.error('Ошибка при добавлении строк:', error);
    }
}

async function buildCustomerRow(element){
    const newRow = document.createElement('tr');
    newRow.classList.add('cst-modal');
    newRow.dataset.id = element['pk'];
    // name
    let newCell = document.createElement('td');
    let cellContent = document.createTextNode(element.fields['name']);
    newCell.appendChild(cellContent);
    newCell.style.fontWeight = 'bold';
    newRow.appendChild(newCell);
    // address
    newCell = document.createElement('td');
    cellContent = document.createTextNode(element.fields['address']);
    newCell.appendChild(cellContent);
    newRow.appendChild(newCell);
    // contact
    newCell = document.createElement('td');
    cellContent = document.createTextNode(element.fields['contact']);
    newCell.appendChild(cellContent);
    newRow.appendChild(newCell);
    // subcontractor
    newCell = document.createElement('td');
    const cellText = element.fields['subcontractor'] ? 'Да' :'Нет';
    cellContent = document.createTextNode(cellText);
    newCell.appendChild(cellContent);
    newRow.appendChild(newCell);
    // button
    newCell = document.createElement('td');
    newCell.setAttribute('onclick', 'event.stopPropagation()');
    const button = document.createElement('button');
    button.type = 'button';
    button.classList.add('btn-delete', 'btn-bg');
    button.setAttribute('onclick', 'customerDelete(this, ' + element['pk'] + ');');
    newCell.appendChild(button);
    newRow.appendChild(newCell);
    return newRow;
}