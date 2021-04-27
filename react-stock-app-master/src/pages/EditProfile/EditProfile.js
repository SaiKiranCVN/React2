import React, { useEffect, useState } from 'react';
import './EditProfile.css'
import { Link, useHistory } from "react-router-dom";
import { ReactComponent as Logo } from "../../assets/icons/chart-line.svg";
import { auth } from "../../firebase";
import { useStateValue } from "../../StateProvider";



function EditProfile() {
    const [name, setName] = useState(' ');
    const [age, setAge] = useState(' ');
    const [address, setAddress] = useState(' ');
    const [phone, setPhone] = useState(' ');
    const [gender, setGender] = useState(' ');
   
    
    const [{  user, userProfile,basket }, dispatch] = useStateValue();
    const saveProfile = () => {
        // remove the item from the basket
        const userProfile = {
            userName: name ,
            email: user.email,
            userPwd: user.password,
            age:age,
            address:address,
            phone:phone,
            gender:gender,
            balance :100
        };
    
        fetch('http://localhost:8000/api/userdata/',{
          'method':'PUT',
          'body': JSON.stringify(userProfile),
          headers:{
            'Content-Type': 'application/json',
            'Authorization' : 'Token f2d664ce87773e9a8f58660ce6c246f2e70fa277'
          }
        }).then(resp => resp.json())
        .then(resp => console.log(resp))
        .catch(error => console.log(error))
  

        dispatch({
            type: 'save_Profile',
            userProfile
        });
    }

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

        < div className = 'login__container' >
        <h1 > Edit Profile </h1>
        <h4 > Username :</h4> 
        <input type = 'text'
        value = { name }
       
        onChange = { e => setName(e.target.value)}
        />
        
        <h4 > E - mail :</h4> 
        <h6>{ user.email }</h6> 
       
        <h4>Gender:</h4>
        <input type = 'text'
        value = { gender }
       
        onChange = { e => setGender(e.target.value)}
        />
        <h4>Age:</h4>
        <input type = 'text'
        value = { age }
       
        onChange = { e => setAge(e.target.value)}
        />
        <h4>Address:</h4>
        <input type = 'text'
        value = { address }
       
        onChange = { e => setAddress(e.target.value)}
        />
        <h4>Phone:</h4>
        <input type = 'text'
        value = { phone }
       
        onChange = { e => setPhone(e.target.value)}
        />
        <h4 > Balance :</h4> 
        <h6>{ userProfile[0].balance}</h6>
     

       <Link to = { '/profile' }  >
        <button 
        onClick = { saveProfile }
        className = 'login__registerButton' >Save  your Profile</button></Link>
        </div >
        </div>
    )
}


export default EditProfile;