<?php
/**
 * Created by PhpStorm.
 * User: chunh
 * Date: 4/5/2018
 * Time: 1:11 PM
 */

if(isset($_POST['temperature'])) {
    $message = "";
	$command = $_GET['temperature'];
    $output = passthru("python main.py $command");

} else {
	$message = "ERROR!";
}

?>
<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Custom Map Generation</title>

    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom fonts -->
    <link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic,900,900italic' rel='stylesheet' type='text/css'>

    <!-- Custom styles -->
    <link href="css/admin.css" rel="stylesheet">

  </head>

  <body id="page-top">

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
      <div class="container">
        <a class="navbar-brand js-scroll-trigger" href="#page-top">Custom Map Admin</a>
      </div>
    </nav>

    <section id="about">
      <div class="container no-gutters">
        <div class="row">
          <!-- <div class="col-md-3 mx-auto my-5">
            <ul class="option-menu">
              <li class="menu-item active">Item 1</li>
              <li class="menu-item">Item 2</li>
              <li class="menu-item">Item 3</li>
              <li class="menu-item">Item 4</li>
              <li class="menu-item">Item 5</li>
              <li class="menu-item">Item 6</li>
              <li class="menu-item">Item 7</li>
              <li class="menu-item">Item 8</li>
              <li class="menu-item">Item 9</li>
              <li class="menu-item">Item 10</li>
            </ul>
          </div> -->
          <div class="col-xs-12 mx-auto my-5">
            <h2 class="section-heading text-center text-muted my-4">Create a <span class="bg-red">Custom Map<span></h2>
            <!-- <p class="text-muted mb-4">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. -->
            <form class="cmap-form" id="weather" method="POST" action="">
              <select class="slct" name="temperature">
                <option>High Temperature</option>
                <option>Low Temperature</option>
              </select>
              <button class="btn btn-primary btn-xl js-scroll-trigger" type="submit" name="submit">Get Started!</button>
            </form>
              <?php
              echo $message;
              if(isset($_POST['submit'])) {
                  echo '<img src="./test.png">';
              } else {
                  echo '<img src="./img/gears.png">';
              }
              ?>

          </div>
        </div>
      </div>
    </section>

    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Custom scripts -->
    <script src="js/admin.js"></script>

  </body>

</html>
