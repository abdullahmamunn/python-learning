<?php
	function selectionSort($ar) {
	  $n = count($ar);
	  for($i = 0; $i<$n; $i++) {
	    $min = $i;
	    for($j=$i+1; $j<$n; $j++) {
	      if($ar[$j] < $ar[$min]) {
	        $min = $j;
	      }
	    }
	    
	    $temp = $ar[$i];
	    $ar[$i] = $ar[$min];
	    $ar[$min] = $temp; 
	  }
	  
	  return $ar;
	}
	
	$ar = [2,5,3,10,8,7];
	$sorted = selectionSort($ar);
	echo "Sorted array: ". implode(", ", $sorted);
	
// 	Time Complexity: O(n^2)
?>