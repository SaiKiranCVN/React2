import React, { useState } from "react";

import styles from "./DividendsSellAmount.module.css";
import { getCurrentYear } from "../../helpers";

import {auth} from "../../firebase";
import { useStateValue } from "../../StateProvider";
const DividendsSellAmount = ({ stock, stocks }) => {
  const [amount, setAmount] = useState(0);
  const currentYear = getCurrentYear();
  const currentYearDividend = stock.dividends[currentYear];
  const [{  user, userProfile,basket }, dispatch] = useStateValue();
  const getAmountOfShares = () => {
   
    if (amount > 0) {
      const shares = amount / stock.ask;
      return shares.toFixed(2);
    }
    return 0;
  };


  const item= {
    name: stock.name,
    ticker: stock.ticker,
    bid: stock.bid,
    ask: stock.ask,
    sector: stock.sector,
    change: stock.change,
    dividends: stock.dividends,
    pe: stock.pe,
    amountofShares: getAmountOfShares(),
    amountinUSD: amount,
    type:"S",
    email: user.email
  };

  const calculateProjectedDividend = () => {
    const shares = getAmountOfShares();
    const total = shares * currentYearDividend;

    return total.toFixed(2);
  };
  const removeFromBasket = () => {
    // dispatch the item into the data layer
    // console.log('gkuefgewkufg')
    fetch('http://localhost:8000/api/trade/',{
      'method':'POST',
      'body': JSON.stringify(item),
      headers:{
        'Content-Type': 'application/json',
        'Authorization' : 'Token 8d34f3dd98857f786c1db13373d6254053f8db1c'
      }
    }).then(resp => resp.json())
    .then(resp => console.log(resp))
    .catch(error => console.log(error))

  



    dispatch({
      type: "Remove_From_BASKET",
      item,     
    });
  };

  return (
    <section className={styles.calculator}>
      <h3 className={styles.header}>Amount to Buy</h3>

      <div className={styles.container}>
        <div className={styles.innerContainer}>
          <p className={styles.descriptor}>Amount in USD</p>
          <input
            value={amount}
            name="amount"
            type="number"
            onChange={(e) => setAmount(e.target.value)}
            className={styles.input}
          />
        </div>
        <div className={styles.innerContainer}>
          <p className={styles.descriptor}>Current ask</p>
          <p className={styles.ask}>{stock.ask} USD</p>
        </div>
      </div>
      <div className={styles.container}>
        <div className={styles.innerContainer}>
          <p className={styles.descriptor}>Amount of shares</p>
          <p className={styles.shares}>{getAmountOfShares()}</p>
        </div>
        <div className={styles.innerContainer}>
          <p className={styles.descriptor}>Projected dividend</p>
          <p className={styles.projectedDividend}>
            {calculateProjectedDividend()} USD
          </p>
        </div>
       
        
      </div>
      <div className={styles.buycontainer}>
      <button onClick={()=>{console.log("remove from basket");removeFromBasket();}} className={styles.buy}>Sell</button>
      </div>

    
    </section>
  );
};

export default DividendsSellAmount;
