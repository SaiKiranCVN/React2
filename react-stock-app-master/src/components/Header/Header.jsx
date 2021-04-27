import React from "react";

import styles from "./Header.module.css";
import { ReactComponent as Logo } from "../../assets/icons/chart-line.svg";
import { Link } from "react-router-dom";
import { useContext } from "react";
import {auth} from "../../firebase";
import { useStateValue } from "../../StateProvider";
const Header = () => {
  const [{  user }, dispatch] = useStateValue();


  
  const handleAuthenticaton = () => {
    if (user) {
        auth.signOut();
    }
  }


  return (
    <header className={styles.header}>
      <div className={styles.container}>
        <Link to="/" className={styles.logoContainer}>
          <Logo className={styles.logo} />
          <span>StockApp</span>
        </Link>
        
        
        
        <div 
        className = {styles.header__option} >{!user?
        <span className = {styles.header__optionLineOne} >Hello  Guest ! </span> :<Link to = {user && '/profile' } className={styles.logoContainer}>
        <span className = {styles.header__optionLineOne} >Hello { user.email } ! </span> </Link>}
        <Link to = {!user && '/login' } className={styles.logoContainer}>
        <span className = {styles.header__optionLineTwo} onClick = { handleAuthenticaton }> {user ? 'Sign Out' : 'Sign In'} </span> </Link>
        
        </div > 
        

        
      </div>
    </header>
  );
};
 
       
        
export default Header
