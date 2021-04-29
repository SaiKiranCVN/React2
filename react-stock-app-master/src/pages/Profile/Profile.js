import React, { useState } from 'react';
import './Profile.css'
import User from'./User'
import { Link, useHistory } from "react-router-dom";
import { ReactComponent as Logo } from "../../assets/icons/chart-line.svg";
import { auth } from "../../firebase";
import UserStockInfo from "../../components/UserStockInfo/UserStockInfo"
import { useStateValue } from "../../StateProvider";
function Profile() {
    const [{  user, userProfile,basket }, dispatch] = useStateValue();
  
    return ( 
        <div className = 'login' >
        <header className='header'>
            <div className='container'>
                <Link to="/" className='logoContainer'>
                    <Logo className='logo'/>
                    <div>Ring</div>
                </Link>
            </div>
        </header>
        <div className = 'container'>
      
        {  userProfile.map(item => ( 
        < User userName = { item.userName }
        firstName = {item.firstName}
        lastName = {item.lastName}
        email = { item.email }
        gender = { item.gender }
        age = { item.age }
        address = { item.address }
        city = { item.city }
        state = { item.state }
        zip = { item.zip }
        card_no = { item.card_no }
        cvv = { item.cvv }

        phone = { item.phone}
        balance = { item.balance} 
        />
            ))}

        
        <div className = 'login__container' ><UserStockInfo/></div>
       
        </div>
        
        </div>
    )
}


export default Profile;