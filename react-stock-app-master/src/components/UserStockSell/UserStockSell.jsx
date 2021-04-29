import React, { useState } from "react";

import styles from "./UserStockSell.module.css";
import History from "./History";
import {auth} from "../../firebase";
import { useStateValue } from "../../StateProvider";
// import { getbalance } from "../../reducer";
const UserStockSell = () => {
 
  const [{  user, userProfile,basket }, dispatch] = useStateValue();
  
  var result = [];
  
  Array.from(new Set(basket.map(x => x.name))).forEach(x => {

  result.push(basket.filter(y => y.name === x).reduce((output,item) => {
    let val1 = output[x] === undefined?0:output[x];
    output[x] = ( parseInt(item.amountinUSD )+  val1); 
   return output;
},{}));

})
  
  console.log(result);

  return (
    <section className={styles.calculator}>
      <h3 className={styles.header}> Your Stock amount: </h3>
      <h4 > Balance :</h4> 
      <h6>{userProfile[0].balance }</h6>
      { result.map(item => ( 
        < History 
                  name = { Object.keys(item) }
                  
                  amountinUSD = {Object.values(item)}
                  />
        
            ))}
    </section>
  );}


export default UserStockSell;
