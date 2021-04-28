import React, { useEffect, useState } from 'react';
import './EditProfile.css'
import { Link, useHistory } from "react-router-dom";
import { ReactComponent as Logo } from "../../assets/icons/chart-line.svg";
import { auth } from "../../firebase";
import { useStateValue } from "../../StateProvider";



function EditProfile() {
    const [username, setName] = useState(' ');
    const [lastName, setLastName] = useState(' ');
    const [firstName, setFirstName] = useState(' ');
    const [age, setAge] = useState(' ');
    const [address, setAddress] = useState(' ');
    const [city, setCity] = useState(' ');
    const [state, setState] = useState(' ');
    const [zip,setZip] = useState(' ');
    const [card_no, setCardNo]  = useState(' ');
    const [phone, setPhone] = useState(' ');
    const [gender, setGender] = useState(' ');
    const [exp_date,setExp_date] = useState(' ');
    const [cvv,setCvv] = useState(' ');

    
   
   
    
    const [{  user, userProfile,basket }, dispatch] = useStateValue();
    const saveProfile = () => {
        // remove the item from the basket
        const userProfile = {
            userName: username ,
            firstName: firstName,
            lastName: lastName,
            email: user.email,
            userPwd: user.password,
            age:age,
            address:address,
            city:city,
            state:state,
            zip:zip,
            card_no:card_no,
            cvv:cvv,
            exp_date:exp_date,
            phone:phone,
            gender:gender,
            balance :1000
        }; 
        // Add extra fields for the rest
        // Needs dictionary of format {'first_name': 'sai','last_name':'dai','email':'sai@gmail.com','username': 'saidai','DOB':'08-26-1997',
        // 'gender':'M','street_address':'375 56','city':'New York','state':'NY','zipcode':11220,'card_no':123456789,'exp_date':'08-26-2025','name':'Sai Dai',
        // 'cvv':234} -> This should be the userProfile that is being passed, and call this function once user clicks save your profile.
        fetch('http://localhost:8000/api/userdata/',{
          'method':'POST',
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
        value = { username }
       
        onChange = { e => setName(e.target.value)}
        />
        <h4 > First name :</h4> 
        <input type = 'text'
        value = { firstName }
       
        onChange = { e => setFirstName(e.target.value)}
        />
        <h4 > Last name :</h4> 
        <input type = 'text'
        value = { lastName }
       
        onChange = { e => setLastName(e.target.value)}
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
        <h4>City:</h4>
        <input type = 'text'
        value = { city }
       
        onChange = { e => setCity(e.target.value)}
        />
        <h4>State:</h4>
        <input type = 'text'
        value = { state }
       
        onChange = { e => setState(e.target.value)}
        />
        <h4>Zipcode:</h4>
        <input type = 'text'
        value = { zip }
       
        onChange = { e => setZip(e.target.value)}
        />
        <h4>Card No:</h4>
        <input type = 'text'
        value = { card_no }
       
        onChange = { e => setCardNo(e.target.value)}
        />

        <h4>Exp Date:</h4>
        <input type = 'text'
        value = { exp_date }
       
        onChange = { e => setExp_date(e.target.value)}
        />
        <h4>Cvv:</h4>
        <input type = 'text'
        value = { cvv }
       
        onChange = { e => setCvv(e.target.value)}
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