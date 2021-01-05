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
    
    var database = firebase.database();

    function writeData() {
      var postListRef = firebase.database().ref('user');
      var newPostRef = postListRef.push();
      newPostRef.set({
        trophyname: document.getElementById("trophyname").value
      });

    }
    firebase.analytics();
