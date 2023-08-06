const tableRender = document.querySelector("#render");
const urlList = tableRender.dataset.url;
const urlLast = tableRender.dataset.url_last;

async function razvLast(lastElement) {
    const data = await fetchJsonData(urlLast + lastElement);
    return JSON.parse(data);
}

async function razvList(lastElement) {
    const data = await fetchJsonData(urlList + lastElement);
    return JSON.parse(data);
}

tableRender.addEventListener("mouseover", async (event) => {
        const target = event.target;
        const element = target.closest(".end-element");
        if (element && tableRender.contains(element)) {
            await addRows(element);
        }
    }
);

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

