const modal = document.querySelector('#driverModal');
const table = document.querySelector('#render');

function inputs(modal) {
    return {
        id: modal.querySelector('#drv_id'),
        code: modal.querySelector("#code"),
        description: modal.querySelector("#description"),
        phone1: modal.querySelector("#phone1"),
        phone2: modal.querySelector('#phone2'),
        car_no: modal.querySelector('#car_no'),
        icon_code: modal.querySelector('#icon_code')
    }
}

async function openDriverModal(titleText, modalData) {
    const modalTitle = modal.querySelector("#modal-title");
    modalTitle.textContent = titleText;
    for (const key in inputs(modal)) {
        inputs(modal)[key].value = modalData[key];
    }

    modal.style.display = "block";
}

async function prepareToEditDriver(element) {
    const drvId = element.dataset.id;
    const jsonUrl = '/rzv/json_driver_select/' + drvId;
    let driver = {name: null};
    if (drvId != null) {
        driver = JSON.parse(await fetchJsonData(jsonUrl));
        document.getElementsByClassName(driver['icon_code'])[0].checked = true;
    } else document.getElementById('chk-1').checked = true;
    const titleText = drvId == null ? 'Новый водитель' : 'Редактировать водителя';
    await openDriverModal(titleText, driver);
}

table.addEventListener("click", async (event) => {
    const target = event.target;
    const element = target.closest(".drv-modal");
    if (element && table.contains(element)) {
        await prepareToEditDriver(element);
    }
});
