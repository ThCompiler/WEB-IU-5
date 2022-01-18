import {StockComponent} from "../components/stock.js";
import {ButtonComponent} from "../components/button.js";
import {MainPage} from "./main_page.js";
import {ajax} from "../modules/ajax.js";
import {urls} from "../modules/urls.js";

export class StockPage {
    constructor(parent, id) {
        this.parent = parent
        this.id = id
    }

    async getData() {
        return ajax.get(urls.stock(this.id))
    }

    get page() {
        return document.getElementById('stock-page')
    }

    getHTML() {
        return (
            `
                <div id="stock-page">
                </div>
            `
        )
    }

    clickBack() {
        const mainPage = new MainPage(this.parent)
        mainPage.render()
    }

    async render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)
        let before_button = document.getElementById(`stock-page`)
        let button = new ButtonComponent(before_button, "Назад", '', this.clickBack.bind(this))
        button.render()

        const data = (await this.getData()).data
        const stock = new StockComponent(this.page)
        stock.render(data)
    }
}