<html>
<!--Collaborate with Qiqi Wang and Wenzhe Liu-->
<head>
  <title>Exercise 3 - A Web Journal</title>
  <link rel="stylesheet" type="text/css" href="css/style.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
</head>

<?php
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
?>

<body>
  <div class="compose-button">
    <a href="create_post.php" title="create post">
      <i class="material-icons">create</i>
    </a>
  </div>

  <h1>Yueyang Zhang's Web Journal</h1>

  <?php   
    $stmt = $conn->prepare("SELECT posts.id as post_id, title, slug, posts.body as post_body, comments.body as comment_body, 
    author FROM posts LEFT OUTER JOIN comments ON posts.id = comments.post_id
     ORDER BY post_id, comments.id");
    $stmt->execute();
    $result = $stmt->get_result();
    // arrays to store data from sql query
    $bodyData =  array();
    $authorData =  array();
    $slugData = array();
    $titleData = array();
    $postBodyDate = array();
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
      // save data in array
      $post_id = strval($row['post_id']);
      $body = strval($row['comment_body']);
      $author = strval($row['author']);
      $title = strval($row['title']);
      $post_body = strval($row['post_body']);
      $slug = strval($row['slug']);
      if (!array_key_exists($post_id,$titleData)) {
        $titleData[$post_id] = $title;
        $slugData[$post_id] = $slug;
        $postBodyData[$post_id] = $post_body;
      }
      if (!array_key_exists($post_id,$bodyData)) {  
        $bodyData[$post_id] = array($body);
        $authorData[$post_id] = array($author);
      }
      else{
        array_push($bodyData[$post_id], $body);
        array_push($authorData[$post_id], $author);
      }
    }
    // get keys
    $keys = array();
    if(!empty($postBodyData)){
      foreach ($postBodyData as $key => $value){
        array_push($keys, $key);
      }
    }

  if(!empty($postBodyData)){
    // for each post
    for ($indx = sizeof($keys)-1; $indx>=0; $indx-- ){
      $key = $keys[$indx];
      ?>
      <div class="post" id=<?php echo $key?>>
      <h2 class= post-title id= "<?php echo $slugData[$key] ?>" >
        <?php echo $titleData[$key]?>
        <a href="#<?php echo $slugData[$key]?>">
          <i class="material-icons">link</i>
        </a>
      </h2>
      <div class="post-body">
        <?php echo $postBodyData[$key]?>
      </div>
      <h3><?php echo empty($bodyData[$key][0]) ? 0 : sizeof($bodyData[$key]) ?> Comments</h3>
      <div class="comment-block">
        <?php
        // for each comment
        for ($i =0; $i < sizeof($bodyData[$key]); $i ++){
        ?>
          <div class="comment">
          <div class="comment-body">
            <?php echo $bodyData[$key][$i] ?>
          </div>
          <div class="comment-author">
          <?php echo $authorData[$key][$i] ?>
          </div>
        </div>
        <?php
        }
        ?>
        <a href="leave_comment.php?post_id=<?php echo $key?>">
          <i class="material-icons">create</i>
          Leave a comment
        </a>
      </div> 
    </div>
      <?php
    }
  }
  ?>
  </div> <!-- end of posts block -->
</body>
