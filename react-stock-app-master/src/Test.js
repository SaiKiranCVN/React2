import React, { useState } from 'react';
import './pages/Profile/Profile.css'
import { Link, useHistory } from "react-router-dom";

import { useStateValue } from "./StateProvider";
function Profile() {
    const [name, setName] = useState(' ');
    const [{   userProfile ,user}, dispatch] = useStateValue();
   
    console.log(userProfile)
    return ( 
        <div className = 'login' >
        

        < div className = 'login__container' >
        <h1 > Profile </h1>

        <form>
        <h5 > username </h5> 
        </form>
        <h5 > E - mail </h5> 
        < h5>{ userProfile?.userEmail }</h5> 
        <h5 > Password </h5> 
        < h5>{ userProfile?.userPwd}</h5> 
      

        
        </div >
        <h5 > balance </h5> 
        {userProfile.map(userProfile => userProfile.balance)}
        </div>
        
    )
        
    
}


export default Profile;