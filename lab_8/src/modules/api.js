
export const getStocks = async () =>{
    return fetch(`http://localhost:8000/stocks/`)
        .then((response) => {
            return response.json();
        }).catch(() => {
            return []
        })
}

export const getStockById = async (id) =>{
    return await fetch(`http://localhost:8000/stocks/${id}/`)
        .then((response) => {
            return response.json();
        }).catch(() => {
            return {}
        })
}