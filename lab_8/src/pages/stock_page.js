import React, {useEffect, useState} from 'react';
import {Button, Spinner} from "react-bootstrap";
import StockInfo from "../components/stock_info.js";
import {getStockById} from '../modules/api.js'
import {useNavigate, useParams} from "react-router-dom";

function StockPage() {
    const history = useNavigate();
    const pk = useParams();

    const [loading, setLoading] = useState(false)
    const [value, setValue] = useState()

    function to_project() {
        history(`/stocks`);
    }

    useEffect(() => {
        (async () => {
            // Ставим загрузку
            await setLoading(true);
            const results = await getStockById(pk["id"]);
            // Добавляем в состояние только треки
            await setValue(results);
            // Убираем загрузку
            await setLoading(false)
        })()
    }, [pk])

    return (
        <>
        <Button className="cardButton" onClick={to_project} target="_blank" variant="primary">Назад</Button>
        {loading && <div className="loadingBg"><Spinner animation="border"/></div>}
        <StockInfo {...value}/>
        </>
    );
}

export default StockPage;