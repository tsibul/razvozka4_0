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

