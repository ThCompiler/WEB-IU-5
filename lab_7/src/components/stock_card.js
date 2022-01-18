import {ButtonComponent} from "./button.js";
import {StockPage} from "../pages/stock_page.js";

export class StockCardComponent {
    constructor(parent) {
        this.parent = parent;
    }

    getHTML(data) {
        return (
            `
            <div class="card" style="width: 300px;">
                <div id = "card-${data.pk}" class="card-body">
                    <h5 class="card-title">${data.company_name}</h5>
                    <p class="card-text">${data.price}</p>
                </div>
            </div>
            `
        )
    }

    clickCard(e) {
        const cardId = e.target.dataset.id

        const stockPage = new StockPage(this.parent, cardId)
        stockPage.render()
    }

    render(data) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
        let before_button = document.getElementById(`card-${data.pk}`)
        let button = new ButtonComponent(before_button, "Подробнее", data.pk, this.clickCard.bind(this))
        button.render()
    }
}