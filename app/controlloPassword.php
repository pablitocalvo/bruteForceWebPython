<?php
  //recupero user e pass dal form di login
  $user = (isset($_POST['utente'])) ? $_POST['utente'] : '';
  $pass = (isset($_POST['password'])) ? $_POST['password'] : '';

  //verifico user e pass
  if ((strcasecmp($user, 'paolo') == 0 
              && strcmp($pass, 'koala') == 0)
  ) {
    echo 'Login effettuto.';
  } else {
    echo 'Login fallito.';
  }
?>