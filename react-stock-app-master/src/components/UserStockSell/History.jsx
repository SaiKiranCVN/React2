import React from 'react';
import './History.css'
import { Link } from "react-router-dom";
import { useStateValue } from "../../StateProvider";
import styles from "./UserStockSell.module.css";
function History({  name,amountinUSD,ticker }) {

    const [{  user, userProfile,basket }, dispatch] = useStateValue();


    return ( 
        <div className = 'checkoutProduct' >
       {!user?"":<Link className={styles.link} to={`/sell/${name}`}><button className={styles.buyButton}>Sell</button></Link>}
        <div className = 'checkoutProduct__info'>
        <p className = 'checkoutProduct__title' > Name: { name} </p> 
        <p className = "checkoutProduct__price" >
        <p>{ticker}</p>
        <p >  amount in USD: <small>$ </small> <strong > {amountinUSD } </strong></p> </p>
        

        </div></div>
)
}

export default History;