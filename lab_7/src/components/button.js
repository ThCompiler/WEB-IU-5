export class ButtonComponent {
    constructor(parent, text, id, click_event) {
        this.parent = parent;
        this.text = text;
        this.id = id
        this.event = click_event
    }

    getHTML(text) {
        return (
            `
            <button type="button" id="click-card-${this.id}" data-id="${this.id}" class="btn btn-primary">${text}</button>
        `
        )
    }

    render() {
        this.parent.insertAdjacentHTML('beforeend', this.getHTML(this.text))
        document.getElementById(`click-card-${this.id}`).addEventListener("click", this.event)
    }
}