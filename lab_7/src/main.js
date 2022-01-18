import {MainPage} from "./pages/main_page.js";

document.addEventListener('DOMContentLoaded', () => {
    const root = document.getElementById('root');
    const mainPage = new MainPage(root)
    mainPage.render()
});
