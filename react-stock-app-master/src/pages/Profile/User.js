import React from 'react';
import './User.css'
import { Link, useHistory } from "react-router-dom";

function User({ userName,firstName,lastName,email,gender,balance, age,address,city,state,zip,card_no,cvv, phone,}) {


    return ( 
        <div className = 'login__container' >
        <h1 > Profile </h1>
        <h4 > Username :</h4> 
        <h6>{ userName }</h6> 
        <h4 > First name :</h4> 
        <h6>{ firstName }</h6> 
        <h4 > Last name :</h4> 
        <h6>{ lastName }</h6> 
        <h4 > E - mail :</h4> 
        <h6>{ email }</h6> 
        <h4>Gender:</h4>
        <h6>{ gender }</h6>
        <h4>Age:</h4>
        <h6>{ age }</h6>
        <h4>Address:</h4>
        <h6>{ address }</h6>
        <h4>City:</h4>
        <h6>{ city }</h6>
        <h4>State:</h4>
        <h6>{ state }</h6>
        <h4>Zip:</h4>
        <h6>{zip }</h6>
        <h4>Card No:</h4>
        <h6>{ card_no }</h6>
        <h4>Cvv:</h4>
        <h6>{ cvv }</h6>
        <h4>Phone:</h4>
        <h6>{ phone }</h6>
        <h4 > Balance :</h4> 
        <h6>{balance  }</h6>
        <Link to = { '/editprofile' }  >
        <button className = 'login__registerButton' > Edit  your Profile</button>
        </Link>
        </div >
         
)
}

export default User;