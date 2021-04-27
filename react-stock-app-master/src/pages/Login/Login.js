import React, { useState } from 'react';
import './Login.css'
import { Link, useHistory } from "react-router-dom";
import { ReactComponent as Logo } from "../../assets/icons/chart-line.svg";
import { auth } from "../../firebase";

function Login() {
    const history = useHistory();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const signIn = e => {
        e.preventDefault();

        auth
            .signInWithEmailAndPassword(email, password)
            .then(auth => {
                history.push('/')
            })
            .catch(error => alert(error.message))
    }

    const saveToDB = (userInfo) => {
        console.log(userInfo)
        fetch('http://localhost:8000/api/userdata/',{
            'method':'POST',
            'body': JSON.stringify(userInfo),
            headers:{
              'Content-Type': 'application/json',
              'Authorization' : 'Token e0cd06a4d6bae558933254d55bb773d6dab1acd2'
            }
          }).then(resp => resp.json())
          .then(resp => console.log(resp))
          .catch(error => console.log(error))
    }

    const register = e => {
        e.preventDefault();

        auth
            .createUserWithEmailAndPassword(email, password)
            .then((auth) => {
                // it successfully created a new user with email and password
                console.log("=======> auth success!");
                saveToDB(auth);

                if (auth) {
                    // history.push('/');
                }
            })
            .catch(error => alert(error.message))
    }

    return ( 
        <div className = 'login' >
        <header className='header'>
            <div className='container'>
                <Link to="/" className='logoContainer'>
                    <Logo className='logo'/>
                    <span>StockApp</span>
                </Link>
            </div>
        </header>

        < div className = 'login__container' >
        <h1 > Sign - in </h1>

        <form>
        <h5 > E - mail </h5> 
        < input type = 'text'
        value = { email }
        onChange = { e => setEmail(e.target.value) }
        />

        <h5 > Password </h5> 
        <
        input type = 'password'
        value = { password }
        onChange = { e => setPassword(e.target.value) }
        />

        <button type = 'submit'
        onClick = { signIn }
        className = 'login__signInButton' > Sign In </button> 
        </form>

        <p>
        By signing - in you agree to the Ring Conditions of Use & Sale.Please see our Privacy Notice, our Cookies Notice and our Interest - Based Ads Notice.
         </p>

        <button 
        onClick = { register }
        className = 'login__registerButton' > Create your Ring Account </button>
         </div >
          </div>
    )
}

export default Login;