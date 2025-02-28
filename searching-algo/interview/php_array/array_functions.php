<?php
// ✅ Example: Searching and Filtering Arrays

// Sample array of students and scores
$students = [
    "Alice" => 85,
    "Bob" => 78,
    "Charlie" => 92,
    "David" => 70,
    "Eve" => 88
];


// 🔍 1. in_array — Check if a score exists in the array
if (in_array(92, $students)) {
    echo "Someone scored 92!\n";
}

// 🔍 2. array_search — Find the student with a specific score
$key = array_search(85, $students);
if ($key !== false) {
    echo "$key scored 85!\n";
}

// 🧹 3. array_filter — Get students who scored above 80
$top_students = array_filter($students, function($score) {
    return $score > 80;
});
print_r($top_students);

// 🔄 4. array_map — Add a "Pass" or "Fail" status to each student
$status = array_map(function($score) {
    return $score >= 80 ? "Pass" : "Fail";
}, $students);
print_r($status);

// 🔥 5. array_reduce — Calculate the average score

$average = array_reduce($students, function($carry, $item) {
    return $carry + $item;
}) / count($students);
echo "Average score: $average\n";


// PHP 8.4 introduces several new array functions to simplify common operations:

//     array_find(): Returns the first element matching a specified condition.
//     array_find_key(): Retrieves the first key that meets a condition.
//     array_any(): Checks if any elements satisfy a condition.
//     array_all(): Confirms that all elements meet a specific condition.
?>
