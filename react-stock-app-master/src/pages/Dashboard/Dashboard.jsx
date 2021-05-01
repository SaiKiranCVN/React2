import React from "react";

import { ConditionallyRender } from "react-util-kit";

import Header from "../../components/Header/Header";
import Subheader from "../../components/Subheader/Subheader";
import ExchangeList from "../../components/ExchangeList/ExchangeList";
import TopFiveDividendStocksList from "../../components/TopFiveDividendStocksList/TopFiveDividendStocksList";
import InfoCard from "../../components/InfoCard/InfoCard";
import StockList from "../../components/StockList/StockList";
import Layout from "../../components/Layout/Layout";

import { getTopFiveDividendStocks, getInfoCardData } from "./helpers";
// import data from "../../data.js";
import styles from "./Dashboard.module.css";

const Dashboard = ({ exchanges, stocks, setStocks }) => {
  return (
    <>
    {
      console.log(stocks, "stocks in dashboard")
    }
      <Header />
      <Subheader>
        <ExchangeList exchanges={exchanges} />
        <TopFiveDividendStocksList stocks={getTopFiveDividendStocks(stocks)} />
        
        <InfoCard
          title="Highest dividend yield in current year"
          stock={getInfoCardData("current", stocks)}
        />
        <InfoCard
          title="Highest dividend yield all time"
          stock={getInfoCardData("history", stocks)}
        />
        <InfoCard
          title="Highest dividend yield growth in past 3 years"
          stock={getInfoCardData("growth", stocks)}
          darkmode
        />
        
      </Subheader>
  

      <Layout>
        <ConditionallyRender
          ifTrue={stocks.length}
          show={<StockList stocks={stocks} setStocks={setStocks} />}
        />
      </Layout>
    </>
  );
};

export default Dashboard;
