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
    const url = 'razvozka_fulfilled/' + razvId;
    fetch(url)
    /*const xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.send();

     */
}

function razvozkaReturnAll(obj, razvId) {
    obj.classList.toggle('btn-submit');
    obj.classList.toggle('btn-delete');
    const url = 'razvozka_returned_all/' + razvId;
    fetch(url);
}

async function razvozkaDelete(obj, razvId) {
    const rzvUrl = '/rzv/json_razvozka/' + razvId;
    const razvozka = JSON.parse(await fetchJsonData(rzvUrl));
    if (!razvozka['fulfilled']) {
        obj.parentElement.parentElement.style.display = 'none';
        const url = 'razvozka_delete/' + razvId;
        fetch(url);
    }
}

function razvozkaDeliverTo(obj, razvId) {
    obj.classList.toggle('delete-neg');
    const url = 'razvozka_deliver_to/' + razvId;
    fetch(url)
}