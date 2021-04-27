import React from 'react';
import './History.css'


function History({ ticker, name,bid, pe,amountinUSD, amountofShares}) {

    return ( 
        <div className = 'checkoutProduct' >
    
        <div className = 'checkoutProduct__info'>
        <p className = 'checkoutProduct__title' > Name: { name} </p> 
        <p className = "checkoutProduct__price" >
        <p>pe / bid: {pe}/{bid} </p>
        <p >  amount in USD: <small>$ </small> <strong > {amountinUSD } </strong></p> 
        <p> amount of Shares: <strong >{amountofShares} </strong></p></p>

        </div></div>
)
}

export default History;