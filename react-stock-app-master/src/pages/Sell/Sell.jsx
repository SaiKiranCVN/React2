import React, { useEffect, useState } from "react";

import { useParams, Route, useRouteMatch } from "react-router-dom";
import { ConditionallyRender } from "react-util-kit";

import Header from "../../components/Header/Header";
import Subheader from "../../components/Subheader/Subheader";
import StockInfo from "../../components/StockInfo/StockInfo";
import Highlights from "../../components/Highlights/Highlights";
import DividendsSellAmount from "../../components/DividendsSellAmount/DividendsSellAmount";
import UserStockInfo from "../../components/UserStockInfo/UserStockInfo"
import styles from "./Sell.module.css";
import Resources from "../../components/Resources/Resources";

import { auth } from "../../firebase";


import { sortStocksByDividendYield } from "../../helpers";

const initialObject = {
  name: "",
  ticker: "",
  bid: 0,
  ask: 0,
  sector: "",
  change: 0,
  dividends: {},
  homepage: "",
  investorpage: "",
  pe: 0,
  research: [],
};

const Sell = ({ stocks }) => {
  
  const match = useRouteMatch();
  const { name } = useParams();
  const [stock, setStock] = useState(initialObject);

  useEffect(() => {
    const getData = () => {
      if (stocks.length === 0) return;
      const stock = stocks.find((stock) => stock.name === name);
      setStock(stock);
    };

    getData();
  }, [stocks, name]);

// buy_sell - 'B' for buying and, 'S' for selling
// 'trade' Variable should have, the following dict format, {'email':'sai@gmail.com','quantity':23,'buy_sell':'B','price':234,'ticker':'AAPL'}
// Same function should be called even for selling with 'buy_sell' : 'S'.



  // fetch('http://localhost:8000/api/trade/',{
  //   'method':'POST',
  //   'body': JSON.stringify(trade),
  //   headers:{
  //     'Content-Type': 'application/json',
  //     'Authorization' : 'Token 8d34f3dd98857f786c1db13373d6254053f8db1c'
  //   }
  // }).then(resp => resp.json())
  // .then(resp => console.log(resp))
  // .catch(error => console.log(error))





  const getCurrentYearDividendYieldRating = (stocks) => {
    const sorted = sortStocksByDividendYield(stocks);
    let ranking;

    sorted.forEach((stockItem, index) => {
      if (stockItem.ticker === stock.ticker) {
        ranking = index + 1;
      }
    });

    return ranking;
  };

  const setResearch = (researchObject) => {
    setStock((prev) => ({
      ...prev,
      research: [...prev.research, researchObject],
    }));
  };

  return (
    <>
      <Header />
      <Subheader>
        <ConditionallyRender
          ifTrue={stock}
          show={
            <>
              <StockInfo stock={stock} />
              <Highlights stock={stock} stocks={stocks} />
              <Resources
               homepage={stock.homepage}
               investorpage={stock.investorpage}
              /> 
            </>
          } 
         /> 
      </Subheader>


      <div className={styles.dividend}>
      <DividendsSellAmount stock={stock} stocks={stocks}/>
      <UserStockInfo/>

 
      </div>

    </>
  );
};

export default Sell;
