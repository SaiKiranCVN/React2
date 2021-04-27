import React, { useEffect } from "react";
import { Link } from "react-router-dom";
import styles from "./StockList.module.css";
import{sortStocksByDividendYield,sortStocksByCompoundedYield} from "../../helpers";
import Select from "../Select/Select";
import {auth} from "../../firebase";
import { useStateValue } from "../../StateProvider";
const StockList = ({ stocks,setStocks }) => {
  const [{  user }, dispatch] = useStateValue();
  useEffect(() =>{
    setStocksByDividendYieldCurrentYear();
  },[]);

  const renderListItems = () => {
   
    return stocks.map((stock) => {
      return(
        
      <li className={styles.listItem} key={stock.ticker }>
         {!user?"":<Link className={styles.link} to={`/buy/${stock.ticker}`}><button className={styles.buyButton}>Buy</button></Link>}
        <Link className={styles.link} to={`/stocks/${stock.ticker}`}>
        <div className={styles.listItemName}>{stock.name}</div>
        <div className={styles.listItemTicker}>{stock.ticker}</div>
        <div className={styles.listItemAsk}>{stock.ask}</div>
        <div className={styles.listItemBid}>{stock.bid}</div>
      
        <div className={styles.listItemDps}>
          {getDividendPerShare(stock)} USD
        </div>
        <div className={styles.listItemDp1000Spent}>
          {getDividendPer1000Spent(stock)} USD
        </div>
        <div className={styles.listItemPe}>{stock.pe}</div>
        <div className={styles.listItemSector}>{stock.sector}</div>
        </Link>
      </li>
      
      )}
    );
  };

  const getOptions = () => {
    return [
      {
        displayValue: "Highest dividend yield 2020",
        value: "dividendyieldcurrentyear",
      },
      {
        displayValue: "Highest dividend yield overall",
        value: "dividendyieldoverall",
      },
    ];
  };

  const setStocksByDividendYieldOverall = () => {
    const sorted = sortStocksByCompoundedYield(stocks);
    setStocks(sorted);
  };

  const setStocksByDividendYieldCurrentYear = () => {
    const sorted = sortStocksByDividendYield(stocks);
    setStocks(sorted);
  };

  const onSelectChange = (e) => {
    const descriptor = e.target.value;

    if (descriptor === "dividendyieldoverall") {
      setStocksByDividendYieldOverall();
    } else if (descriptor === "dividendyieldcurrentyear") {
      setStocksByDividendYieldCurrentYear();
    }
  };

  const getDividendPerShare = (stock) => {
    const date = new Date();
    const year = date.getFullYear();
    return stock.dividends[year];
  };

  const getDividendPer1000Spent = (stock) => {
    const dividendPerShare = getDividendPerShare(stock);
    const amountOfStocks = 1000 / stock.ask;

    const total = amountOfStocks * dividendPerShare;
    return total.toFixed(2);
  };

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1 className={styles.heading}>Ring Exchange</h1>
        <Select
          options={getOptions()}
          onChange={onSelectChange}
          className={styles.select}
        />
      </div>

      <div className={styles.listContainer}>
        <div className={styles.listHeaders}>
          <div className={styles.nameHeader}>Name</div>
          <div className={styles.tickerHeader}>Ticker</div>
          <div className={styles.askHeader}>Ask</div>
          <div className={styles.bidHeader}>Bid</div>
          <div className={styles.dpsHeader}>Dividend p/s</div>
          <div className={styles.dpspentHeader}>Dividend per 1000 spent</div>
          <div className={styles.peHeader}>P/E</div>
          <div className={styles.sectorHeader}>Sector</div>
        </div>
        <ul className={styles.stockList}>{renderListItems()}</ul>
      </div>
    </div>
  );
};

export default StockList;
