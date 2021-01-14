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

    var emoji;
    var emoji_plan;
    var autonomy_response = document.getElementById("autonomy_response")
    var autonomy_plans = document.getElementById("autonomy_plans")

    var addBtn = document.getElementById("addBtn")
    var addBtn2 = document.getElementById("addBtn2")

    var trophyname = document.getElementById("trophyname")
    var barriers = document.getElementById("barriers")
    var efficacy_plans = document.getElementById("efficacy_plans")
 
    var time = new Date();


/*     autonomy      */
    $(function(){
        $('input[class="positive"]').click(function() {
            emoji = $(this).val();
            return (emoji);
    });
                });
    $(function(){
        $('input[class="negative"]').click(function() {
            emoji = $(this).val();
            return (emoji);
    });
                });

    $(function(){
        $('input[class="future_emoji"]').click(function() {
            emoji_plan = $(this).val();
            alert(emoji_plan);
            return (emoji_plan);
    });
   });

    $(function(){
        $(addBtn).click(function(e){
          e.preventDefault();
          alert(emoji);
        db.collection("autonomy1").add({
          p_id: "T_001",
          emoji : emoji,
          autonomy_response : autonomy_response.value,
          phase: "1st",
          time: time
            })
          .then(function() {
              window.location.href='autonomy2.html';
          })
          });              
        });


    $(function(){
        $(addBtn2).click(function(e){
          e.preventDefault();
          alert(emoji_plan);
        db.collection("autonomy2").add({
          p_id: "T_001",
          emoji_plan : emoji_plan,
          autonomy_plans: autonomy_plans.value,
          phase: "1st",
          time: time
            })
          .then(function() {
              window.location.href='success.html';
          })
          });              
        });




/*     efficacy      */
    if(trophyname){
      addBtn.addEventListener('click', e => {
        e.preventDefault();
        db.collection("efficacy1").add({
        p_id: "T_001",
        trophyname : trophyname.value,
        time: time
          })
          .then(function() {
              alert('success');
              window.location.href='efficacy2.html';
          })
          .catch(function(error) {
              console.error("Error adding document: ", error);
          });
        });
    }

    if(barriers){
      addBtn.addEventListener('click', e => {
        e.preventDefault();
        db.collection("efficacy2").add({
        p_id: "T_001",
        barriers : barriers.value,
        time: time
          })
          .then(function() {            
              window.location.href='success.html';
          })
          .catch(function(error) {
              console.error("Error adding document: ", error);
          });
        });
    }

    if(efficacy_plans){
      addBtn.addEventListener('click', e => {
        e.preventDefault();
        db.collection("efficacy3").add({
        p_id: "T_001",
        efficacy_plans : efficacy_plans.value,
        time: time
          })
          .then(function() {
              alert('success');
              window.location.href='success.html';
          })
          .catch(function(error) {
              console.error("Error adding document: ", error);
          });
        });
    }


/*     combined      
    $(function(){
        $("#addBtn").click(function(){
          alert(emoji);
        db.collection("combined").add({
          p_id: "T_001",
          emoji : emoji,
          autonomy_response : autonomy_response.value,
          trophyname : trophyname.value,
          future_emoji: future_emoji,
          phase: "1st",
          time: time
            })
          });              
        });
*/