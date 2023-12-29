import { anyElement, buttonElement, aElements, imgElement } from "../components/elements.js"


export async function orderTrack(idx = 1) {

    let dateNow = new Date()
    let testOrder = [
        {
            "title": "курьер направляется к вам",
            "date": `${dateNow.getFullYear()}.${dateNow.getMonth()}.${dateNow.getDate()} ${dateNow.getHours()}:${dateNow.getMinutes()}`,
        },
        {
            "title": "заказ передан на доставку",
            "date": `${dateNow.getFullYear()}.${dateNow.getMonth()}.${dateNow.getDate()} ${dateNow.getHours()}:${dateNow.getMinutes()}`,
        },
        {
            "title": "заказ формируется",
            "date": `${dateNow.getFullYear()}.${dateNow.getMonth()}.${dateNow.getDate()} ${dateNow.getHours()}:${dateNow.getMinutes()}`,
        },
        {
            "title": "заказ принят",
            "date": `${dateNow.getFullYear()}.${dateNow.getMonth()}.${dateNow.getDate()} ${dateNow.getHours()}:${dateNow.getMinutes()}`,
        },
    ]

    const mainDiv = anyElement("div", ["order-body"], "", "tr")
    let ulElem = document.createElement("ul")

    let buttonTr = await buttonElement("заказ получен", ["track-btn"], "tr-btn")
    buttonTr.disabled = true
    buttonTr.classList.add("btn-tr-disabled")
    
    if (idx == 4) {
        buttonTr.removeAttribute("disabled")
        buttonTr.classList.remove("btn-tr-disabled");
    }

    testOrder.slice(0, idx).forEach(async function(elem){
        let li = await ulAelementTrack(elem)
        ulElem.prepend(li)
    })

    let btnDiv = anyElement("div", ["btn-div"])

    btnDiv.append(buttonTr)
    ulElem.append(btnDiv)
    mainDiv.append(ulElem)

    return mainDiv
};


async function ulAelementTrack(element) {
   
    let li = document.createElement("li")
    li.classList.add("order-item-tr")
    let aDiv = anyElement("div")
    aDiv.classList.add("text-tr")
    let spanDiv = anyElement("div")

    let titleS = anyElement("div", ["text-descr-tr"], element["title"])
    
    let qtyS = anyElement("div", ["text-descr-tr"], element["date"])
    let img = await imgElement(element["img"])
    img.setAttribute("data-detail", "detail")
    spanDiv.append(titleS, qtyS)
    spanDiv.classList.add("div-descr-tr")
    aDiv.append(spanDiv)
    li.append(aDiv)
    
    return li
};

// buttonSave.removeAttribute("disabled")
// buttonSave.classList.remove("btn-tr-disabled");