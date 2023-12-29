import { anyElement, buttonElement, aElements, imgElement } from "../components/elements.js"


export async function orderConfirm() {

    let testOrder = [
        {
            "title": "заказ принят",
            "confId": "conf-1",
        },
        {
            "title": "заказ формируется",
            "confId": "conf-2",
        },
        {
            "title": "заказ передан на доставку",
            "confId": "conf-3",
        },
        {
            "title": "курьер направляется к вам",
            "confId": "conf-4",
        },

    ]

    const mainDiv = anyElement("div", ["order-body"], "", "tr")
   
    let ulElem = await ulAelementConfirm(testOrder)
    mainDiv.append(ulElem)

    return mainDiv
};

function ulAelementConfirm(collection=[]) {
    let ul = document.createElement("ul")

    collection.forEach(async function (element, index) {
        let li = document.createElement("li")
        li.classList.add("order-item")
        let aDiv = anyElement("div")
        let spanDiv = anyElement("div")
        let buttonTr = await buttonElement("выполнить", ["confirm-btn"], element["confId"])
        

        let titleS = anyElement("span", ["text-descr-cnf"], element["title"])


        titleS.setAttribute("data-detail", "detail")
        spanDiv.setAttribute("data-detail", "detail")

        let img = await imgElement(element["img"])
        img.setAttribute("data-detail", "detail")
        spanDiv.classList.add("div-descr-cnf")
        spanDiv.append(titleS, buttonTr)

        aDiv.append(spanDiv)
        
        li.append(aDiv)
        ul.append(li)
    });
    return ul
};

