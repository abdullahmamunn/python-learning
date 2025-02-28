<?php
trait Logger {
  public function log($message) {
    echo date('Y-m-d H:i:s') . " - " . $message . "\n";
  }
}

class FileUploader {
  use Logger;
  
  public function upload($filename) {
    $this->log("$filename uploaded successfully!");
  }
}

class EmailSender {
   
   use Logger;
   
   public function sendEmail($recipient, $subject) {
      $this->log("Email sent to $recipient with subject $subject");
   }
 }
 
while (1) {
    $fileUploader = new FileUploader();
    $fileUploader->upload("mamun.txt");

    $emailSender = new EmailSender();
    $emailSender->sendEmail("almamun@gmail.com", "Nice to meet you PHP trait");

    sleep(3); // Wait for 3 seconds before repeating
}
 

 
 

?>