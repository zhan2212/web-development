<html>
<head>
  <title>Create a Post</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
</head>
<body>

  <h1>Yueyang Zhang's Web Journal</h1>
  <h2>
  <a href="weblog.php">Go Back</a>    
  </h2>
  <div class="create-post">
    <h2>Create a Post</h2>
    <form method="post">
      <label for="title">Title</label>
      <input name="title"></input>
      <label for="body">Post Body</label>
      <textarea name="body"></textarea>
      <label for="password">Secret Password</label>
      <input type="password" name="password"></input>
      <input type="submit" name="submit" value="Create Post"></input>    
    </form>
    <?php
    // set mysql parameters
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "exercise";
    // set secret password
    $secret = '123';

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
    }

    if(array_key_exists('submit',$_POST)){
      if ($secret ==  strval($_POST['password'])){
        // convert slug
        $title = $_POST['title'];
        $slug = strtolower($title);
        $slug = preg_replace('/[^A-Za-z0-9\-]/', '_', $slug);
        // convert body and title
        $body = strval($_POST['body']);
        $body = htmlspecialchars($body, ENT_QUOTES);
        $title = htmlspecialchars($title, ENT_QUOTES);
        // insert data
        $stmt = $conn->prepare("INSERT INTO posts (slug, title, body) VALUES  (?, ?, ?)");
        $stmt->bind_param("sss", $slug, $title, $body);
        // check insertion
        if (!($stmt->execute() === TRUE)) {
            echo "error";
        }
        else{
          echo "Post Successfully!";
        }
      }
      else{
        echo "Wrong Password!";
      }
    }
    ?>
  </div>
</body>
</html>
