<html>
<head>
  <title>Leave a Comment</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
</head>
<body>
  <h1>Yueyang Zhang's Web Journal</h1>

  <?php
    // set mysql parameters
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "exercise";
    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    // prepare query
    $stmt = $conn->prepare("SELECT slug, title, posts.body as post_body, comments.body as comment_body, author FROM posts LEFT OUTER JOIN comments 
    ON posts.id = comments.post_id where posts.id = ? ;");
    $stmt->bind_param("s", $_GET['post_id']);
    $stmt->execute();
    $result = $stmt->get_result();
    // save author and body data
    $bodyData = array();
    $authorData = array();
    // for each row of table
    while($row = mysqli_fetch_assoc($result)) {
      $slug = $row['slug'];
      $title  = $row['title'];
      $post_body = $row['post_body'];
      array_push($bodyData, strval($row['comment_body']));
      array_push($authorData, strval($row['author']));
    }
    ?>

  <div class="leave-comment">
    <h2>
      Leave a Comment on
      <a href="weblog.php#<?php echo $slug ?>"><?php echo $title ?></a>
    </h2>
    <div class="post-body">
      <?php echo $post_body ?>
    </div>
    <h2>
      Previous Comments:
    </h2>
    <div class="comment-block">
    <?php
      for($i=0; $i < sizeof($bodyData); $i++) {
        $author = $authorData[$i];
        $comment_body = $bodyData[$i];
    ?>
        <div class="comment">
          <div class="comment-body">
            <?php echo $comment_body?>
          </div>
          <div class="comment-author">
          <?php echo $author?>
          </div>
        </div>
    <?php
      }
    ?>
    </div>

    <form method="post">
      <label for="body">Comment</label>
      <textarea name="body"></textarea>
      <label for="name">Your name</label>
      <input name="name"></input>
      <input type="hidden" name="post_id" value="1"></input>
      <input type="submit" name="submit" value="Leave Comment"></input>
    </form>

    <?php
      $post_id = $_GET['post_id'];
      if(array_key_exists('submit',$_POST)){
        //convert body and author
        $body = strval($_POST['body']);
        $body = htmlspecialchars($body, ENT_QUOTES);
        $author = strval($_POST['name']);
        $author = htmlspecialchars($author, ENT_QUOTES);
        // prepare query
        $stmt = $conn->prepare("INSERT INTO comments (post_id, body, author) VALUES   (?, ?, ?)");
        $stmt->bind_param("sss", $post_id, $body, $author);
        if (!($stmt->execute() === TRUE)) {
          echo "error";
        }
        else{
          echo "Comment Successfully!";
        }
        header("Refresh:0");
      }
    ?>
  </div>
</body>
</html>
