<?php
	function insertionSort($ar) {
	  $n = count($ar);
	  for($i = 1; $i<$n; $i++) {
	    $key = $ar[$i];
	    $j = $i - 1;
	    while ($j >= 0 and $ar[$j] > $key) {
	      $ar[$j+1] = $ar[$j];
	      $j--;
	    }
	     $ar[$j + 1] = $key;
	    
	  }
	  
	  return $ar;
	}
	
	$ar = [2,5,3,10,8,7];
	$sorted = insertionSort($ar);
	echo "Sorted array: ". implode(", ", $sorted);
	
// 	Time Complexity: O(n^2)
?>