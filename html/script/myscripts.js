    // Your web app's Firebase configuration
    // For Firebase JS SDK v7.20.0 and later, measurementId is optional

    var firebaseConfig = {
      apiKey: "AIzaSyAOn5k6mMfyQNJT2K20vCQ2zpxMnh2KtJ8",
      authDomain: "self-evaluation-f4b63.firebaseapp.com",
      projectId: "self-evaluation-f4b63",
      storageBucket: "self-evaluation-f4b63.appspot.com",
      messagingSenderId: "1002832901774",
      appId: "1:1002832901774:web:6fffaed9b32547893a3bdf",
      measurementId: "G-ZYER7VP5BF",
      databaseURL: "https://self-evaluation-f4b63-default-rtdb.firebaseio.com/"
    };
    // Initialize Firebase

    firebase.initializeApp(firebaseConfig);


    var db = firebase.firestore();

    const addBtn = document.getElementById("addBtn")
    const trophyname = document.getElementById("trophyname")
    const time = new Date();

    if(trophyname){
      addBtn.addEventListener('click', e => {
        e.preventDefault();
        db.collection("efficacy").add({
        first: "Bomi",
        last: "Lovelace",
        born: 1815,
        trophyname : trophyname.value,
        time: time
          })
          .then(function(docRef) {
              console.log("Document written with ID: ", docRef.id);
          })
          .catch(function(error) {
              console.error("Error adding document: ", error);
          });
        });

    }



