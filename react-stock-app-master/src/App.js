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


  const getPrice = async () => {
    await fetch('http://localhost:8000/api/price/',{
        'method':'GET',
        headers:{
          'Content-Type': 'application/json',
          'Authorization' : 'Token 8d34f3dd98857f786c1db13373d6254053f8db1c'
        }
      }).then(resp => resp.json())
      .then(resp => {
        setPrice(resp);
        // console.log('Setted------',price)
      })
      .catch(error => console.log(error));
  }

  const getItem = async () => {

  }

  const getData = async () => {
    //backend, to get exchange and stock info

    await getPrice();

    const exchanges = data.exchanges;
    const stocks = data.stocks;
    // const stocks = price;
    // console.log('Assigning - ',price)
    return {
      exchanges,
      stocks,
    };
  };









  useEffect(async() => {
    const { exchanges, stocks } = await getData();

    setExchanges(exchanges);
    setStocks(stocks);
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
       console.log(price, "=====>")
     }
      <Router>
        <Route
          exact
          path="/"
          render={(props) => (
            <Dashboard
              exchanges={exchanges}
              stocks={stocks}
              setStocks={setStocks}
              {...props}
            />
          )}
        />
        <Route
          path="/stocks/:ticker"
          render={(props) => <StockView {...props} stocks={stocks} />}
        />
        <Route  path="/buy/:ticker"
        render={(props) => <Buy {...props} stocks={stocks} />}/>


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
