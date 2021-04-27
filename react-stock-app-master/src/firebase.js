// For Firebase JS SDK v7.20.0 and later, measurementId is optional
import firebase from "firebase";
const firebaseConfig = {
    apiKey: "AIzaSyBtyI2UeHTeHiS4GG9MWmuqikU8vgedmt8",
    authDomain: "ring-e6c93.firebaseapp.com",
    databaseURL: "https://ring-e6c93-default-rtdb.firebaseio.com",
    projectId: "ring-e6c93",
    storageBucket: "ring-e6c93.appspot.com",
    messagingSenderId: "156103537467",
    appId: "1:156103537467:web:8f8cd7ed30159d76e67d1e",
    measurementId: "G-FNPRL4T579"
  };
const firebaseApp = firebase.initializeApp(firebaseConfig);

const db = firebaseApp.firestore();
const auth = firebase.auth();


export { db, auth };