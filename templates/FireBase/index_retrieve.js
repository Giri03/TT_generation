$(document).ready(function(){
var rootRef = firebase.database().ref();
rootRef.on("child_added",function(data){

  var name = data.child("name").val();
  var email = data.child("Email").val();

  $('#table_body').append(
    "<tr><td>" + name + "</td><td>" + email +
    "</td><td><button>remove</button></td>");
});
)} 
