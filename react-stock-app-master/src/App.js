import React, {  useEffect, useState } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
// import './App.css';
// import Header from './components/Header/Header';
// import Subheader from './components/Subheader/Subheader';
// import ExchangeList from './components/ExchangeList/ExchangeList';
// import TopFiveDividendStocksList from "./components/TopFiveDividendStocksList/TopFiveDividendStocksList";
// import InfoCard from "./components/InfoCard/InfoCard";
// import StockList from "./components/StockList/StockList";
import Dashboard from "./pages/Dashboard/Dashboard";
import StockView from "./pages/StockView/StockView";
import Buy from "./pages/Buy/Buy";
import Sell from "./pages/Sell/Sell";
import Login from "./pages/Login/Login";
import Profile from "./pages/Profile/Profile";
import EditProfile from "./pages/EditProfile/EditProfile";
// import styles from"./App.module.css";
import data from "./data.js";
import Test from "./Test.js";
import { auth } from "./firebase";
import { useStateValue } from "./StateProvider";
// import{getTopFiveDividendStocks,getInfoCardData} from "./helpers.js";



function App() {

  const [{}, dispatch] = useStateValue();

  const [exchanges, setExchanges] = useState([]);
  const [stocks, setStocks] = useState([]);
  const [price,setPrice] = useState([]);


  // const getPrice = async () => {
  //   await fetch('http://localhost:8000/api/price/',{
  //       'method':'GET',
  //       headers:{
  //         'Content-Type': 'application/json',
  //         'Authorization' : 'Token 8d34f3dd98857f786c1db13373d6254053f8db1c'
  //       }
  //     }).then(resp => resp.json())
  //     .then(resp => {
  //       setPrice(resp);
  //       // console.log('Setted------',price)
  //     })
  //     .catch(error => console.log(error));
  // }

  const getItem = async () => {

  }

  const getData = async () => {
    //backend, to get exchange and stock info
    var stoc = []
    // await getPrice();
    fetch('http://localhost:8000/api/price/',{
        'method':'GET',
        headers:{
          'Content-Type': 'application/json',
          'Authorization' : 'Token 8d34f3dd98857f786c1db13373d6254053f8db1c'
        }
      }).then(resp => resp.json())
      .then(resp => {
        console.log('RESPPPPPP',resp)
        setPrice(resp);
        stoc = resp;
        // const stocks = resp; 
        // const stocks = resp;
        // console.log('Setted------',price)
      })
      .catch(error => console.log(error));
    const exchanges = data.exchanges;
    // const stocks = data.stocks;
    const stocks = stoc;
    console.log('Assigning stoc - ',stoc)
    return {
      exchanges,
      stocks,
    };
  };
  // 123

  const getUserProfile = (email) => {
    
  }









  useEffect(async() => {
    const { exchanges, stocks } = await getData();

    setExchanges(exchanges);
    console.log('Asigment done here , so check',price)
    setStocks(stocks);
    // setStocks(price);
  }, []);
  useEffect(() => {
    // will only run once when the app component loads...

    auth.onAuthStateChanged((authUser) => {
        console.log("THE USER IS >>> ", authUser);

        if (authUser) {
            // the user just logged in / the user was logged in

            dispatch({
                type: "SET_USER",
                user: authUser,
            });
        } else {
            // the user is logged out
            dispatch({
                type: "SET_USER",
                user: null,
            });
        }
    });
}, []);
  

  return (
    <div className="App">
     {
       console.log(price,stocks, "price=====>")
     }
      <Router>
        <Route
          exact
          path="/"
          render={(props) => (
            <Dashboard
              exchanges={exchanges}
              // stocks={stocks}
              stocks={price}
              setStocks={setStocks}
              {...props}
            />
          )}
        />
        <Route
          path="/stocks/:ticker"
          render={(props) => <StockView {...props} stocks={price} />}
        />
        
        <Route  path="/buy/:ticker"
        render={(props) => <Buy {...props} stocks={price} />}/>
        <Route  path="/sell/:name"
        render={(props) => <Sell {...props} stocks={price} />}/>


        < Route path = "/login" >
        < Login/>
        </Route> 
        < Route path = "/profile" >
        < Profile/>
        </Route>
        < Route path = "/editprofile" >
        < EditProfile/>
        </Route>
        < Route path = "/test" >
        < Test/>
        </Route>
      </Router>
     
    </div>
  );
}


export default App;
