-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 06, 2023 at 01:50 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cms_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `course_name` varchar(200) NOT NULL,
  `department_name` varchar(200) NOT NULL,
  `duration` int(20) NOT NULL,
  `time_units` varchar(200) NOT NULL,
  `fee` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`course_name`, `department_name`, `duration`, `time_units`, `fee`) VALUES
('B.A. Journalism & Mass Communication', 'Journalism &Mass Communication', 3, 'Years', 300000),
('B.TECH. CSE', 'Engineering &Technology', 4, 'Months', 800000),
('B.TECH. ECE', 'Engineering &Technology', 4, 'Years', 780000),
('B.TECH. ENC', 'Engineering &Technology', 4, 'Years', 790000),
('BA LLB', 'LAW', 5, 'Years', 600000),
('BCOM LLB', 'LAW', 5, 'Years', 800000),
('LLB', 'LAW', 4, 'Years', 350000),
('M.A. Journalism &Mass Communication', 'Journalism &Mass Communication', 2, 'Years', 200000),
('M.TECH. CSE', 'Engineering &Technology', 2, 'Years', 200000),
('M.TECH. ECE', 'Engineering &Technology', 2, 'Years', 190000),
('M.TECH. ENC', 'Engineering &Technology', 2, 'Years', 180000);

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `department_name` varchar(200) NOT NULL,
  `head_of_department` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`department_name`, `head_of_department`) VALUES
('Engineering &Technology', 'Dr.Jyoteesh Malhotra'),
('Journalism &Mass Communication', 'Dr.Namarta Joshi'),
('LAW', 'Dr.Rupam Jagota');

-- --------------------------------------------------------

--
-- Table structure for table `fee_detail`
--

CREATE TABLE `fee_detail` (
  `rollno` int(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `paid_fees` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fee_detail`
--

INSERT INTO `fee_detail` (`rollno`, `name`, `paid_fees`) VALUES
(101, 'Mohit', 200000),
(101, 'Mohit', 200000),
(101, 'Mohit', 400000),
(102, 'Rahul', 300000),
(102, 'Rahul', 100000),
(103, 'smile', 200000),
(104, 'Robin', 200000),
(102, 'Rahul', 100000),
(102, 'Rahul', 50000),
(102, 'Rahul', 20000),
(102, 'Rahul', 10000),
(102, 'Rahul', 10000),
(103, 'smile', 50000),
(103, 'smile', 5);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `rollno` int(150) NOT NULL,
  `name` varchar(200) NOT NULL,
  `phone` int(20) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `address` varchar(200) NOT NULL,
  `department` varchar(200) NOT NULL,
  `course` varchar(200) NOT NULL,
  `pic` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`rollno`, `name`, `phone`, `gender`, `dob`, `address`, `department`, `course`, `pic`) VALUES
(101, 'Mohit', 2147483647, 'Male', '2003-09-24', '159-Jalandhar', 'Engineering &Technology', 'B.TECH. CSE', '1688221832passport size pic.jpg'),
(102, 'Rahul', 2147483647, 'Male', '2002-06-12', '12-Lamba Pind', 'LAW', 'BA LLB', '1688146945ps_2.jpg'),
(103, 'smile', 2147483647, 'Male', '2000-07-27', 'Jal.', 'Journalism &Mass Communication', 'B.A. Journalism & Mass Communication', '1688471426ps_1.jpg'),
(104, 'Robin', 2147483647, 'Male', '2001-07-06', 'Chandigarh', 'LAW', 'BCOM LLB', 'defaultimage.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `teacher_id` int(11) NOT NULL,
  `teacher_name` varchar(200) NOT NULL,
  `phone` int(11) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `dob` date NOT NULL,
  `address` varchar(200) NOT NULL,
  `qualification` varchar(200) NOT NULL,
  `pic` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`teacher_id`, `teacher_name`, `phone`, `gender`, `dob`, `address`, `qualification`, `pic`) VALUES
(1001, 'Dr.Deep Kamal Randhawa', 1478963251, 'Male', '1994-07-14', 'Jal.', 'P.h.D.', '1688302348ps_6.jpg'),
(1002, 'Rohit', 1236987451, 'Male', '1995-07-13', 'Himachal', 'BSc in Electronics', '1688302411ps_2.jpg'),
(1003, 'Dr.Pankajdeep', 2147483647, 'Male', '1997-07-17', 'Jalandhar', 'Bsc. in medical science', '1688629842ps_4.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE `usertable` (
  `username` varchar(200) NOT NULL,
  `password` int(100) NOT NULL,
  `usertype` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usertable`
--

INSERT INTO `usertable` (`username`, `password`, `usertype`) VALUES
('himanshu', 987, 'Employee'),
('Mohit', 159, 'Admin'),
('rahul', 951, 'Employee');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_name`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`department_name`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`rollno`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`teacher_id`);

--
-- Indexes for table `usertable`
--
ALTER TABLE `usertable`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
