var textarea = document.getElementById('textarea');
var button = document.getElementById('button');

var firebaseHead = document.getElementById("head");

var firebaseHeadref = firebase.database().ref().child("Heading");
#retrieving data
firebaseHeadref.on('value',function(data){
  firebaseHead.innerText = data.val();
});

function submit(){
  var dbref = firebase.database().ref();
  var msg = textarea.value;
  dbref.child('Heading').set(msg);
  window.alert('hello');
}
