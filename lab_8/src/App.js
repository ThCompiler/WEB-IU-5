import './App.css';
import {Route, Routes, Navigate} from "react-router-dom";
import MainPage from "./pages/main_pages.js";
import StockPage from "./pages/stock_page.js";

function App() {

    return (
        <div className="App">
            <Routes>
                <Route path="/" element={<Navigate to={"/stocks"}/>}/>
                <Route exact path="/stocks" element={<MainPage/>}/>
                <Route path="/stock/:id" element={<StockPage/>}/>
            </Routes>
            <hr/>
        </div>
    );
}

export default App;
