echo "Sorted array: " . implode(", ", $sortedArr);
<?php
	function BubbleSort($ar) {
	  $n = count($ar);
	  
	  for($i = 0; $i <$n; $i++) {
	    $swapped = false;
	    for($j = 0; $j <$n-$i-1; $j++) {
	      if ($ar[$j] > $ar[$j+1]) {
	        $temp = $ar[$j];
	        $ar[$j] = $ar[$j+1];
	        $ar[$j+1] = $temp;
	        
	        $swapped = true;
	      }
	    }
	    if(!$swapped)
	    break;
	  }
	  
	  return $ar;
	}
	
	
$arr = [64, 34, 25, 12, 22, 11, 90];
$sortedArr = BubbleSort($arr);
echo "Sorted array: ". implode(" ", $sortedArr);
// Example implode(separator, array)
// note implode takes array and join strings, so it convert array to string
?>