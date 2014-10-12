<?php
session_start();
?>
<html>
<head>
 <meta charset="utf-8">
	  <title>Upload</title>
	  <script type="text/javascript" src="js/jquery.js"></script>
	  <script type="text/javascript" src="js/ajax.js"></script>
	  <style>
	  .meter { 
	height: 20px;  /* Can be anything */
	position: relative;
	background: #555;
	-moz-border-radius: 25px;
	-webkit-border-radius: 25px;
	border-radius: 25px;
	padding: 10px;
	-webkit-box-shadow: inset 0 -1px 1px rgba(255,255,255,0.3);
	-moz-box-shadow   : inset 0 -1px 1px rgba(255,255,255,0.3);
	box-shadow        : inset 0 -1px 1px rgba(255,255,255,0.3);
}
.meter > span {
	display: block;
	height: 100%;
	   -webkit-border-top-right-radius: 8px;
	-webkit-border-bottom-right-radius: 8px;
	       -moz-border-radius-topright: 8px;
	    -moz-border-radius-bottomright: 8px;
	           border-top-right-radius: 8px;
	        border-bottom-right-radius: 8px;
	    -webkit-border-top-left-radius: 20px;
	 -webkit-border-bottom-left-radius: 20px;
	        -moz-border-radius-topleft: 20px;
	     -moz-border-radius-bottomleft: 20px;
	            border-top-left-radius: 20px;
	         border-bottom-left-radius: 20px;
	background-color: rgb(43,194,83);
	background-image: -webkit-gradient(
	  linear,
	  left bottom,
	  left top,
	  color-stop(0, rgb(43,194,83)),
	  color-stop(1, rgb(84,240,84))
	 );
	background-image: -webkit-linear-gradient(
	  center bottom,
	  rgb(43,194,83) 37%,
	  rgb(84,240,84) 69%
	 );
	background-image: -moz-linear-gradient(
	  center bottom,
	  rgb(43,194,83) 37%,
	  rgb(84,240,84) 69%
	 );
	background-image: -ms-linear-gradient(
	  center bottom,
	  rgb(43,194,83) 37%,
	  rgb(84,240,84) 69%
	 );
	background-image: -o-linear-gradient(
	  center bottom,
	  rgb(43,194,83) 37%,
	  rgb(84,240,84) 69%
	 );
	-webkit-box-shadow: 
	  inset 0 2px 9px  rgba(255,255,255,0.3),
	  inset 0 -2px 6px rgba(0,0,0,0.4);
	-moz-box-shadow: 
	  inset 0 2px 9px  rgba(255,255,255,0.3),
	  inset 0 -2px 6px rgba(0,0,0,0.4);
	position: relative;
	overflow: hidden;
}
.meter > span:after {
	content: "";
	position: absolute;
	top: 0; left: 0; bottom: 0; right: 0;
	background-image: 
	   -webkit-gradient(linear, 0 0, 100% 100%, 
	      color-stop(.25, rgba(255, 255, 255, .2)), 
	      color-stop(.25, transparent), color-stop(.5, transparent), 
	      color-stop(.5, rgba(255, 255, 255, .2)), 
	      color-stop(.75, rgba(255, 255, 255, .2)), 
	      color-stop(.75, transparent), to(transparent)
	   );
	background-image: 
		-webkit-linear-gradient(
		  -45deg, 
	      rgba(255, 255, 255, .2) 25%, 
	      transparent 25%, 
	      transparent 50%, 
	      rgba(255, 255, 255, .2) 50%, 
	      rgba(255, 255, 255, .2) 75%, 
	      transparent 75%, 
	      transparent
	   );
	background-image: 
		-moz-linear-gradient(
		  -45deg, 
	      rgba(255, 255, 255, .2) 25%, 
	      transparent 25%, 
	      transparent 50%, 
	      rgba(255, 255, 255, .2) 50%, 
	      rgba(255, 255, 255, .2) 75%, 
	      transparent 75%, 
	      transparent
	   );
	background-image: 
		-ms-linear-gradient(
		  -45deg, 
	      rgba(255, 255, 255, .2) 25%, 
	      transparent 25%, 
	      transparent 50%, 
	      rgba(255, 255, 255, .2) 50%, 
	      rgba(255, 255, 255, .2) 75%, 
	      transparent 75%, 
	      transparent
	   );
	background-image: 
		-o-linear-gradient(
		  -45deg, 
	      rgba(255, 255, 255, .2) 25%, 
	      transparent 25%, 
	      transparent 50%, 
	      rgba(255, 255, 255, .2) 50%, 
	      rgba(255, 255, 255, .2) 75%, 
	      transparent 75%, 
	      transparent
	   );
	z-index: 1;
	-webkit-background-size: 50px 50px;
	-moz-background-size:    50px 50px;
	background-size:         50px 50px;
	-webkit-animation: move 2s linear infinite;
	   -webkit-border-top-right-radius: 8px;
	-webkit-border-bottom-right-radius: 8px;
	       -moz-border-radius-topright: 8px;
	    -moz-border-radius-bottomright: 8px;
	           border-top-right-radius: 8px;
	        border-bottom-right-radius: 8px;
	    -webkit-border-top-left-radius: 20px;
	 -webkit-border-bottom-left-radius: 20px;
	        -moz-border-radius-topleft: 20px;
	     -moz-border-radius-bottomleft: 20px;
	            border-top-left-radius: 20px;
	         border-bottom-left-radius: 20px;
	overflow: hidden;
}  
	  </style>
</head>
<body>
 <?php
		require('dbconnect.php');
		$handle = fopen("final.sua", "r");
		if ($handle) 
		{
			$Num_to_insert=0;
			while (($line = fgets($handle)) !== false) 
			{
				$row_data=explode("<!|!>",$line);
				$Num_to_insert++;
			}
			$_SESSION['total']=$Num_to_insert;
			echo '<button onclick="upload('.$Num_to_insert.')" >Click to start</button>';
		}	

		?>
<div id="result">
</div>

<div class="meter" style="width:500px;">
	<span style="width: 0%;"></span>
</div>

</body>
</html>
