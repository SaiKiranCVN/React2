import React, { useState } from "react";

import styles from "./DividendsBuyAmount.module.css";
import { getCurrentYear } from "../../helpers";

import {auth} from "../../firebase";
import { useStateValue } from "../../StateProvider";
const DividendsBuyAmount = ({ stock, stocks }) => {
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

  const calculateProjectedDividend = () => {
    const shares = getAmountOfShares();
    const total = shares * currentYearDividend;

    return total.toFixed(2);
  };
  const addToBasket = () => {
    // dispatch the item into the data layer
    
    dispatch({
      type: "ADD_TO_BASKET",
      item: {
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
      },
     
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
      <button onClick={addToBasket} className={styles.buy}>Buy</button>
      </div>

    
    </section>
  );
};

export default DividendsBuyAmount;
