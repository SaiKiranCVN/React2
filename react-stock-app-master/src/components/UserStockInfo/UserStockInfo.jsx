import React, { useState } from "react";

import styles from "./UserStockInfo.module.css";
import History from "./History";
import {auth} from "../../firebase";
import { useStateValue } from "../../StateProvider";
// import { getbalance } from "../../reducer";
const UserStockInfo = () => {
 
  const [{  user, userProfile,basket }, dispatch] = useStateValue();
  console.log(userProfile, "userProfile===>");
  return (
    <section className={styles.calculator}>
      <h3 className={styles.header}> Your Transaction History</h3>
      <h4 > Balance :</h4> 
      <h6>{userProfile[0].balance }</h6>
      {basket.slice(0).reverse().map(item => ( 
        < History ticker = { item.ticker }
                  name = { item.name }
                  bid = { item.bid }
                  pe = { item.pe }
                  amountinUSD = { item.amountinUSD }
                 amountofShares = { item.amountofShares} 
                 type = {item.type}/>
            ))}
    </section>
  );}


export default UserStockInfo;
