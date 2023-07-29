function fetchJsonData(jsonUrl) {
    return fetch(jsonUrl)
        .then(response => response.json());
}

function dateRus(dateString) {
    return dateString.slice(8) + '.' + dateString.slice(5, 7) + '.' + dateString.slice(2, 4);
}

function dateRusLong(dateString) {
    return dateString.slice(8) + '.' + dateString.slice(5, 7) + '.' + dateString.slice(0, 4);
}


function planShow() {
    const planBody = document.querySelector(".plan-body");
    planBody.classList.toggle('un-show');
}

function razvozkaFulfilled(obj, razvId) {
    obj.classList.toggle('btn-submit');
    obj.classList.toggle('btn-delete');

    const checkLg = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="16" fill="currentColor" viewBox="0 0 16 16">' +
        '<path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 ' +
        '0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"/></svg>';
    const hourGlass = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="16"\n' +
        ' fill="currentColor"  viewBox="0 0 16 16">\n' +
        ' <path d="M2 1.5a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-1v1a4.5 4.5 0 0 1-2.557 4.06c-.29.139-.443.377-.443.59v.7c0 ' +
        '.213.154.451.443.59A4.5 4.5 0 0 1 12.5 13v1h1a.5.5 0 0 1 0 1h-11a.5.5 0 1 1 0-1h1v-1a4.5 4.5 0 0 1 ' +
        '2.557-4.06c.29-.139.443-.377.443-.59v-.7c0-.213-.154-.451-.443-.59A4.5 4.5 0 0 1 3.5 3V2h-1a.5.5 0 0 ' +
        '1-.5-.5zm2.5.5v1a3.5 3.5 0 0 0 1.989 3.158c.533.256 1.011.791 1.011 1.491v.702c0 .7-.478 1.235-1.011 1.491A3.5 ' +
        '3.5 0 0 0 4.5 13v1h7v-1a3.5 3.5 0 0 0-1.989-3.158C8.978 9.586 8.5 9.052 8.5 8.351v-.702c0-.7.478-1.235 ' +
        '1.011-1.491A3.5 3.5 0 0 0 11.5 3V2h-7z"/>\n' +
        ' </svg>\n';
    if (obj.classList.contains('btn-submit')) {
        obj.childNodes[1].innerHTML = checkLg;
    } else {
        obj.childNodes[1].innerHTML = hourGlass;
    }
    const url = '/rzv/razvozka_fulfilled/' + razvId;
    fetch(url)
}

async function razvozkaReturnAll(obj, razvId) {
    const modal = document.querySelector('#deliverModal')
    modal.style.display = 'block';
    let returnList = '';
    let returnAll = '';
    let i = 0;
    const toReturn = await razvozkaReturnsInfoById(razvId);
    toReturn.forEach(function (delivery) {
        if (delivery['deliver__return_all']) {
            returnAll = ' checked ';
        } else {
            returnAll = '';
        }
        returnList += '<div class="input-line input-line-left"><input type="checkbox" class="check-input" id="delivery-chk-' +
            i + '"' + 'name="delivery-chk-' + i + '"' + returnAll + '>&nbsp;&nbsp;&nbsp;' +
            '<label for="delivery-' + delivery['deliver__id'] + '"><strong>' + dateRus(delivery['deliver__date']) +
            '</strong>' + delivery['deliver__to_do_deliver'] + '</label>' +
            '<input hidden name="delivery-' + i + '" value="' + delivery['deliver__id'] + '"></div>';
        i += 1;
    });
    modal.querySelector('#razv-id').value = razvId;
    modal.querySelector('#rzv-return-quantity').value = toReturn.length;
    modal.querySelector('#to_return_from_customer').innerHTML = returnList;
}

async function razvozkaDelete(obj, razvId) {
    const rzvUrl = '/rzv/json_razvozka/' + razvId;
    const razvozka = JSON.parse(await fetchJsonData(rzvUrl));
    if (!razvozka['fulfilled']) {
        obj.parentElement.parentElement.style.display = 'none';
        const url = '/rzv/razvozka_delete/' + razvId;
        fetch(url);
    }
}

function razvozkaDeliverTo(obj, razvId) {
    obj.classList.toggle('delete-neg');
    const url = '/rzv/razvozka_deliver_to/' + razvId;
    fetch(url)
}

async function plannedReturnsList(razvId, obj) {
    const plannedReturns = await razvozkaReturnsInfoById(razvId);
    let titleText = ''
    plannedReturns.forEach(function (element) {
        titleText += dateRus(element['deliver__date']) + ' ' + element['deliver__to_do_deliver'] + ' || ';
    });
    obj.dataset.title = titleText;
}

async function razvozkaReturnsInfoById(razvId) {
    const returnUrl = '/rzv/json_returns_full_info/' + razvId;
    return await fetchJsonData(returnUrl);
}


const returnAllForm = document.getElementById('deliverModalForm');

returnAllForm.addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(returnAllForm);

    fetch('/rzv/razvozka_returned_all/', {
        method: 'POST',
        body: formData,
    })
        .then((response) => {
            closeModal()
        })
        .catch((error) => {
            console.error(error);
        });
    const returnClause = returnAllForm.querySelector('#to_return_from_customer')
    const returnObjects = returnClause.querySelectorAll('.check-input')
    let checked = true;
    returnObjects.forEach(function (checkbox){
        if(checkbox.checked == false){
            checked = false
        }
    });
       const butId = 'but-' + returnAllForm.querySelector('#razv-id').value;
       if(checked){
           document.getElementById(butId).classList.remove('btn-delete')
           document.getElementById(butId).classList.add('btn-submit')
       }else{
           document.getElementById(butId).classList.add('btn-delete')
           document.getElementById(butId).classList.remove('btn-submit')
       }


});