const fulfilledIcon = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" ' +
    'class="bi bi-check-lg" viewBox="0 0 16 16"><path d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 ' +
    '1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 ' +
    '5.4-6.425a.247.247 0 0 1 .02-.022Z"/></svg>';
const waitingIcon = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" ' +
    'class="bi bi-hourglass" viewBox="0 0 16 16"><path d="M2 1.5a.5.5 0 0 1 .5-.5h11a.5.5 0 0 1 0 1h-1v1a4.5 4.5 0 0 ' +
    '1-2.557 4.06c-.29.139-.443.377-.443.59v.7c0 .213.154.451.443.59A4.5 4.5 0 0 1 12.5 13v1h1a.5.5 0 0 1 0 1h-11a.5.5 ' +
    '0 1 1 0-1h1v-1a4.5 4.5 0 0 1 2.557-4.06c.29-.139.443-.377.443-.59v-.7c0-.213-.154-.451-.443-.59A4.5 4.5 0 0 1 3.5 ' +
    '3V2h-1a.5.5 0 0 1-.5-.5zm2.5.5v1a3.5 3.5 0 0 0 1.989 3.158c.533.256 1.011.791 1.011 1.491v.702c0 .7-.478 1.235-1.011 ' +
    '1.491A3.5 3.5 0 0 0 4.5 13v1h7v-1a3.5 3.5 0 0 0-1.989-3.158C8.978 9.586 8.5 9.052 8.5 8.351v-.702c0-.7.478-1.235 ' +
    '1.011-1.491A3.5 3.5 0 0 0 11.5 3V2h-7z"/></svg>';
const handshakeIcon = '<svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 640 512">' +
    '<path d="M272.2 64.6l-51.1 51.1c-15.3 4.2-29.5 11.9-41.5 22.5L153 161.9C142.8 171 129.5 176 115.8 176H96V304c20.4 ' +
    '.6 39.8 8.9 54.3 23.4l35.6 35.6 7 7 0 0L219.9 397c6.2 6.2 16.4 6.2 22.6 0c1.7-1.7 3-3.7 3.7-5.8c2.8-7.7 9.3-13.5 ' +
    '17.3-15.3s16.4 .6 22.2 6.5L296.5 393c11.6 11.6 30.4 11.6 41.9 0c5.4-5.4 8.3-12.3 8.6-19.4c.4-8.8 5.6-16.6 ' +
    '13.6-20.4s17.3-3 24.4 2.1c9.4 6.7 22.5 5.8 30.9-2.6c9.4-9.4 9.4-24.6 0-33.9L340.1 243l-35.8 33c-27.3 25.2-69.2 ' +
    '25.6-97 .9c-31.7-28.2-32.4-77.4-1.6-106.5l70.1-66.2C303.2 78.4 339.4 64 377.1 64c36.1 0 71 13.3 97.9 37.2L505.1 ' +
    '128H544h40 40c8.8 0 16 7.2 16 16V352c0 17.7-14.3 32-32 32H576c-11.8 0-22.2-6.4-27.7-16H463.4c-3.4 6.7-7.9 13.1-13.5 ' +
    '18.7c-17.1 17.1-40.8 23.8-63 20.1c-3.6 7.3-8.5 14.1-14.6 20.2c-27.3 27.3-70 30-100.4 8.1c-25.1 20.8-62.5 ' +
    '19.5-86-4.1L159 404l-7-7-35.6-35.6c-5.5-5.5-12.7-8.7-20.4-9.3C96 369.7 81.6 384 64 384H32c-17.7 ' +
    '0-32-14.3-32-32V144c0-8.8 7.2-16 16-16H56 96h19.8c2 0 3.9-.7 5.3-2l26.5-23.6C175.5 77.7 211.4 64 248.7 64H259c4.4 ' +
    '0 8.9 .2 13.2 .6zM544 320V176H496c-5.9 0-11.6-2.2-15.9-6.1l-36.9-32.8c-18.2-16.2-41.7-25.1-66.1-25.1c-25.4 0-49.8 ' +
    '9.7-68.3 27.1l-70.1 66.2c-10.3 9.8-10.1 26.3 .5 35.7c9.3 8.3 23.4 8.1 32.5-.3l71.9-66.4c9.7-9 24.9-8.4 33.9 1.4s8.4' +
    ' 24.9-1.4 33.9l-.8 .8 74.4 74.4c10 10 16.5 22.3 19.4 35.1H544zM64 336a16 16 0 1 0 -32 0 16 16 0 1 0 32 0zm528 16a16' +
    ' 16 0 1 0 0-32 16 16 0 1 0 0 32z"/></svg>';
const diggingIcon = '<svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 576 512"><path d="M208 ' +
    '64a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zM9.8 214.8c5.1-12.2 19.1-18 31.4-12.9L60.7 210l22.9-38.1C99.9 144.6 129.3 ' +
    '128 161 128c51.4 0 97 32.9 113.3 81.7l34.6 103.7 79.3 33.1 34.2-45.6c6.4-8.5 16.6-13.3 27.2-12.8s20.3 6.4 25.8 ' +
    '15.5l96 160c5.9 9.9 6.1 22.2 .4 32.2s-16.3 16.2-27.8 16.2H288c-11.1 ' +
    '0-21.4-5.7-27.2-15.2s-6.4-21.2-1.4-31.1l16-32c5.4-10.8 16.5-17.7 28.6-17.7h32l22.5-30L22.8 ' +
    '246.2c-12.2-5.1-18-19.1-12.9-31.4zm82.8 91.8l112 48c11.8 5 19.4 16.6 19.4 29.4v96c0 17.7-14.3 32-32 ' +
    '32s-32-14.3-32-32V405.1l-60.6-26-37 111c-5.6 16.8-23.7 25.8-40.5 20.2S-3.9 486.6 1.6 469.9l48-144 11-33 32 1' +
    '3.7z"/></svg>';
const deliverToIcon = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" ' +
    'class="bi bi-arrow-clockwise" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 3a5 5 0 1 0 4.546 2.914.5.5 0 0 ' +
    '1 .908-.417A6 6 0 1 1 8 2v1z"/><path d="M8 4.466V.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384L8.41 ' +
    '4.658A.25.25 0 0 1 8 4.466z"/></svg>';
const deleteIcon = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="16" fill="currentColor" ' +
    'viewBox="0 0 16 16"><path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 ' +
    '8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z"/></svg>';
const tableRender = document.querySelector("#render");

let cachedRazvozkiLast = null;
let cachedRazvozkiList = null;

async function razvLast(lastElement) {
    let data = await fetchJsonData('/rzv/json_razvozki_last/' + lastElement);
    cachedRazvozkiLast = JSON.parse(data);
    return cachedRazvozkiLast;
}

async function razvList(lastElement) {
    let data = await fetchJsonData('/rzv/json_razvozki_list/' + lastElement);
    cachedRazvozkiList = JSON.parse(data);
    return cachedRazvozkiList;
}

tableRender.addEventListener("mouseover", async (event) => {
        const target = event.target;
        const element = target.closest(".end-element");
        if (element && tableRender.contains(element)) {
            await addRows(element);
        }
    }
);

// tableRender.addEventListener("focus", async (event) => {
//         const target = event.target;
//         const element = target.closest(".end-element");
//         if (element && tableRender.contains(element)) {
//             await addRows(element);
//         }
//     }
// );


async function addRows(row) {
    row.classList.remove('end-element');
    let lastElement = row.id;

    try {
        const razvozkiList = await razvList(lastElement);
        for (const element of razvozkiList) {
            const newRow = await buildRow(element)
            row.parentElement.appendChild(newRow);
        }
        const razvozkiLast = await razvLast(lastElement);
        await row.parentElement.appendChild(await buildLastRow(razvozkiLast[0], lastElement));
    } catch (error) {
        console.error('Ошибка при добавлении строк:', error);
    }
}

async function buildRow(element) {
    const newRow = document.createElement('tr');
    newRow.classList.add('edit-modal');
    newRow.dataset.id = element['pk'];
    //date
    let newCell = document.createElement('td');
    let cellContent = document.createTextNode(dateRusLong(element.fields['date']));
    newCell.appendChild(cellContent);
    newRow.appendChild(newCell);
    // driver icon
    newCell = document.createElement('td');
    if (element.fields['driver'] != null) {
        const driverIcon = await fetchJsonData('/rzv/json_driver_url/' + element.fields['driver']);
        newCell.dataset.title = await fetchJsonData('/rzv/json_driver_description/' + element.fields['driver']);
        newCell.classList.add('title-icon');
        const newImage = document.createElement('img');
        newImage.src = driverIcon;
        newImage.alt = 'driver icon';
        newCell.appendChild(newImage);
    }
    newRow.appendChild(newCell);
    // fulfilled icon
    newCell = document.createElement('td');
    newCell.setAttribute('onclick', 'event.stopPropagation()');
    newCell.dataset.title = 'Поменять статус';
    newCell.classList.add('title-icon');
    let button = document.createElement('button');
    button.classList.add('btn-bg');
    button.setAttribute('onclick', 'razvozkaFulfilled(this, ' + element['pk'] + ')');
    if (element.fields['fulfilled']) {
        button.classList.add('btn-submit');
        button.innerHTML =  fulfilledIcon;
        button.insertBefore(document.createTextNode(''), button.firstChild);
    } else {
        button.classList.add('btn-delete');
        button.innerHTML = waitingIcon;
        button.insertBefore(document.createTextNode(''), button.firstChild);
    }
    newCell.appendChild(button);
    newRow.appendChild(newCell)
    // return_All icon
    newCell = document.createElement('td');
    newCell.setAttribute('onclick','event.stopPropagation()');
    if (element.fields['return_from']) {
        button = document.createElement('button');
        button.type = 'button';
        button.id = 'but-' + element['pk'];
        button.setAttribute('onclick','razvozkaReturnAll(this, ' + element['pk'] + ');');
        button.classList.add('btn-bg');
        button.innerHTML = handshakeIcon;
        if (element.fields['returned_all']) {
            button.classList.add('btn-submit');
        } else {
            button.classList.add('delete');
        }
    }
    newRow.appendChild(newCell);
    // customer_name
    newCell = document.createElement('td');
    newCell.innerHTML = '<strong>' + element.fields['customer_name'] + '</strong>';
    newRow.appendChild(newCell);
    // address
    newCell = document.createElement('td');
    newCell.innerHTML = element.fields['address'];
    newRow.appendChild(newCell);
    //contact
    newCell = document.createElement('td');
    newCell.innerHTML = element.fields['contact'];
    newRow.appendChild(newCell);
    // to_do
    newCell = document.createElement('td');
    let toDoString = '';
    if (element.fields['to_do_take']) {
        toDoString += '<div><strong>ЗАБРАТЬ: </strong>' + element.fields['to_do_take'] + '</div>';
    }
    if (element.fields['to_do_deliver']) {
        toDoString += '<div><strong>ЗАБРАТЬ: </strong>' + element.fields['to_do_deliver'] + '</div>';
    }
    newCell.innerHTML = toDoString;
    newRow.appendChild(newCell);
    // return from icon
    newCell = document.createElement('td');
    if (element.fields['return_from']) {
        newCell.classList.add('title-icon-big');
        newCell.setAttribute('onmouseenter', 'plannedReturnsList(' + element['pk'] + ', this);');
        button = document.createElement('button');
        button.type = 'button';
        button.classList.add('btn-submit', 'btn-bg');
        button.innerHTML = diggingIcon;
        newCell.appendChild(button);
    }
    newRow.appendChild(newCell);
    // deliver_to icon
    newCell = document.createElement('td');
    if (element.fields['customer'] != null) {
        const customer = fetchJsonData('/rzv/json_customer_select/' + element.fields['customer']);
        if (customer['subcontractor'] && element.fields['to_do_deliver'] != null) {
            newCell.setAttribute('obclick', 'event.stopPropagation()');
            newCell.classList.add('title-icon');
            newCell.dataset.title = 'Отправить на переработку';
            button = document.createElement('button');
            button.type = 'button';
            button.classList.add('btn-delete', 'btn-bg');
            button.setAttribute('onclick', 'razvozkaDeliverTo(this, ' + element['pk'] + ');');
            button.innerHTML = deliverToIcon;
            if (element.fields['deliver_to']) {
                button.classList.add('delete-neg');
            }
            newCell.appendChild(button);
        }
    }
    newRow.appendChild(newCell);
    // delete icon
    newCell = document.createElement('td');
    newCell.setAttribute('onclick', 'event.stopPropagation()');
    newCell.classList.add('title-icon');
    newCell.dataset.title = 'Удалить';
    button = document.createElement('button');
    button.type = 'button';
    button.classList.add('btn-delete', 'btn-bg');
    button.setAttribute('onclick', 'razvozkaDelete(this, ' + element['pk'] + ');');
    button.innerHTML = deleteIcon;
    newCell.appendChild(button);
    newRow.appendChild(newCell);
    return newRow;
}

async function buildLastRow(element, number) {
    const newRow = buildRow(element);
    (await newRow).classList.add('end-element');
    (await newRow).id = Number(number) + 20;
    return newRow;
}

