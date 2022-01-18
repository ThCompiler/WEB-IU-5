import {Card} from "react-bootstrap";
import React from "react";

const StockInfo = (data) => {
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
            <div  className="textStyle">
                <Card.Text>
                    {data.is_growing ?"Растёт":"Не растёт"}
                </Card.Text>
            </div>
            <div  className="textStyle">
                <Card.Text>
                    {data.date_modified}
                </Card.Text>
            </div>
        </Card.Body>
    </Card>
}

export default StockInfo;