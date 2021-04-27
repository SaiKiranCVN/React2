import React from 'react';
import './User.css'
import { Link, useHistory } from "react-router-dom";

function User({ userName,email,gender, age,address, phone,balance}) {


    return ( 
        <div className = 'login__container' >
        <h1 > Profile </h1>
        <h4 > Username :</h4> 
        <h6>{ userName }</h6> 
        <h4 > E - mail :</h4> 
        <h6>{ email }</h6> 
        <h4>Gender:</h4>
        <h6>{ gender }</h6>
        <h4>Age:</h4>
        <h6>{ age }</h6>
        <h4>Address:</h4>
        <h6>{ address }</h6>
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