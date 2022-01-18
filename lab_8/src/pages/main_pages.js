import React, {useEffect, useState} from 'react';
import {Col, Row, Spinner} from "react-bootstrap";
import StockCard from "../components/stock_card.js";
import {getStocks} from '../modules/api.js'
import useWindowSize from '../modules/huk.js'

function MainPage() {
    const [loading, setLoading] = useState(false)
    const [value, setValue] = useState([])

    useEffect(() => {
        (async () => {
            // Ставим загрузку
            await setLoading(true);
            const results = await getStocks();
            // Добавляем в состояние только треки
            await setValue(results);
            // Убираем загрузку
            await setLoading(false)
        })()
    }, [])

    const {width} = useWindowSize();
    const isMobile = width && width <= 600;

    return (
        <div className={`container ${loading && 'containerLoading'}`}>
            {loading && <div className="loadingBg"><Spinner animation="border"/></div>}
            {!value.length ? <h1>К сожалению, пока ничего не найдено :(</h1> :
                <Row xs={1} md={isMobile ? 1 : 4} className="g-4">
                    {value.map((item, index) => {
                        return isMobile ? <StockCard {...item} key={index}/> : (
                            <Col key={index}>
                                <StockCard {...item}/>
                            </Col>
                        )
                    })}
                </Row>
            }
        </div>
    );
}

export default MainPage;