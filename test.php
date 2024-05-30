<?php
$userid = $_POST['id'];

$username =$_POST['username'];
$pass = $_POST['pass'];
$lname = $_POST['lname'];
$fname = $_POST['fname'];

if(empty($_POST['mname'])){
    $mname = " ";
}
else {
    $mname = $_POST['mname'];
}

$bdate = $_POST['bdate'];
$useremail = $_POST['useremail'];
$cnum = $_POST['cnum'];
$gender = $_POST['gender'];
$empstatus = $_POST['empstatus'];
$disability = $_POST['disability'];

if(empty($_POST['additional'])){
    $additional = " ";
}
else {
    $additional = $_POST['additional'];
}

$address1 = $_POST['address1'];

if(empty($_POST['address2'])){
    $address2 = " ";
}
else {
    $address2 = $_POST['address2'];
}

$country = $_POST['country'];
$region = $_POST['region'];
$prov = $_POST['prov'];
$city = $_POST['city'];
$brgy = $_POST['brgy'];
$pcode = $_POST['pcode'];
$membertyper = $_POST['membertyper'];
$memberdur = $_POST['memberdur'];

if(empty($_POST['ref'])){
    $ref = " ";
}
else {
    $ref = $_POST['ref'];
}

if(empty($_POST['memberfile'])){
    $memberfile = " ";
}
else {
    $memberfile = $_POST['memberfile'];
}

$verif1 = $_POST['verif1'];
$verif2 = $_POST['verif2'];

$conn = mysqli_connect('localhost', 'root', '', 'database');
if(!$conn){
    die('Connection Failed : '.mysqli_connect_error());
}
else{
    $query1 = mysqli_query($conn, "UPDATE `registration` SET `username` = '$username', `pass` = '$pass', `lname` = '$lname', `fname` = '$fname', `mname` = '$mname', `bdate` = '$bdate', `useremail` = '$useremail', `cnum` = '$cnum', `gender` = '$gender', `empstatus` = '$empstatus', `disability` = '$disability', `additional` = '$additional', `address1` = '$address1', `address2` = '$address2', `country` = '$country', `region` = '$region', `prov` = '$prov', `city` = '$city', `brgy` = '$brgy', `pcode` = '$pcode', `membertyper` = '$membertyper', `memberdur` = '$memberdur', `ref` = '$ref', `memberfile` = '$memberfile', `verif1` = '$verif1', `verif2` = '$verif2' WHERE `registration`.`id` = $userid");
}$userid = $_POST['id'];

$username =$_POST['username'];
$pass = $_POST['pass'];
$lname = $_POST['lname'];
$fname = $_POST['fname'];

if(empty($_POST['mname'])){
    $mname = " ";
}
else {
    $mname = $_POST['mname'];
}

$bdate = $_POST['bdate'];
$useremail = $_POST['useremail'];
$cnum = $_POST['cnum'];
$gender = $_POST['gender'];
$empstatus = $_POST['empstatus'];
$disability = $_POST['disability'];

if(empty($_POST['additional'])){
    $additional = " ";
}
else {
    $additional = $_POST['additional'];
}

$address1 = $_POST['address1'];

if(empty($_POST['address2'])){
    $address2 = " ";
}
else {
    $address2 = $_POST['address2'];
}

$country = $_POST['country'];
$region = $_POST['region'];
$prov = $_POST['prov'];
$city = $_POST['city'];
$brgy = $_POST['brgy'];
$pcode = $_POST['pcode'];
$membertyper = $_POST['membertyper'];
$memberdur = $_POST['memberdur'];

if(empty($_POST['ref'])){
    $ref = " ";
}
else {
    $ref = $_POST['ref'];
}

if(empty($_POST['memberfile'])){
    $memberfile = " ";
}
else {
    $memberfile = $_POST['memberfile'];
}

$verif1 = $_POST['verif1'];
$verif2 = $_POST['verif2'];

$conn = mysqli_connect('localhost', 'root', '', 'database');
if(!$conn){
    die('Connection Failed : '.mysqli_connect_error());
}
else{
    $query1 = mysqli_query($conn, "UPDATE `registration` SET `username` = '$username', `pass` = '$pass', `lname` = '$lname', `fname` = '$fname', `mname` = '$mname', `bdate` = '$bdate', `useremail` = '$useremail', `cnum` = '$cnum', `gender` = '$gender', `empstatus` = '$empstatus', `disability` = '$disability', `additional` = '$additional', `address1` = '$address1', `address2` = '$address2', `country` = '$country', `region` = '$region', `prov` = '$prov', `city` = '$city', `brgy` = '$brgy', `pcode` = '$pcode', `membertyper` = '$membertyper', `memberdur` = '$memberdur', `ref` = '$ref', `memberfile` = '$memberfile', `verif1` = '$verif1', `verif2` = '$verif2' WHERE `registration`.`id` = $userid");
}