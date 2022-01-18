import {Button, Card} from "react-bootstrap";
import React from "react";
import {useNavigate} from "react-router-dom";

const StockCard = (data) => {
    const history = useNavigate();

    function to_project() {
        history(`/stock/${data.pk}/`);
    }

    return <Card className="card">
        <Card.Body>
            <div className="textStyle">
                <Card.Title>{data.company_name}</Card.Title>
            </div>
            <div  className="textStyle">
                <Card.Text>
                    {data.price}
                </Card.Text>
            </div>
            <Button className="cardButton" onClick={to_project} target="_blank" variant="primary">Подробнее...</Button>
        </Card.Body>
    </Card>
}

export default StockCard;