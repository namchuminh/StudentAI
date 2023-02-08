-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 08, 2023 at 05:33 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `studentai`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance_attendanceinfo`
--

CREATE TABLE `attendance_attendanceinfo` (
  `id` bigint(20) NOT NULL,
  `date` date NOT NULL,
  `classname_id` bigint(20) NOT NULL,
  `student_id` bigint(20) NOT NULL,
  `subject_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `attendance_attendanceinfo`
--

INSERT INTO `attendance_attendanceinfo` (`id`, `date`, `classname_id`, `student_id`, `subject_id`) VALUES
(4, '2023-02-08', 1, 1, 1),
(5, '2023-02-08', 1, 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add info user', 7, 'add_infouser'),
(26, 'Can change info user', 7, 'change_infouser'),
(27, 'Can delete info user', 7, 'delete_infouser'),
(28, 'Can view info user', 7, 'view_infouser'),
(29, 'Can add class name', 8, 'add_classname'),
(30, 'Can change class name', 8, 'change_classname'),
(31, 'Can delete class name', 8, 'delete_classname'),
(32, 'Can view class name', 8, 'view_classname'),
(33, 'Can add specialization', 9, 'add_specialization'),
(34, 'Can change specialization', 9, 'change_specialization'),
(35, 'Can delete specialization', 9, 'delete_specialization'),
(36, 'Can view specialization', 9, 'view_specialization'),
(37, 'Can add students', 10, 'add_students'),
(38, 'Can change students', 10, 'change_students'),
(39, 'Can delete students', 10, 'delete_students'),
(40, 'Can view students', 10, 'view_students'),
(41, 'Can add subject', 11, 'add_subject'),
(42, 'Can change subject', 11, 'change_subject'),
(43, 'Can delete subject', 11, 'delete_subject'),
(44, 'Can view subject', 11, 'view_subject'),
(45, 'Can add scores', 12, 'add_scores'),
(46, 'Can change scores', 12, 'change_scores'),
(47, 'Can delete scores', 12, 'delete_scores'),
(48, 'Can view scores', 12, 'view_scores'),
(49, 'Can add attendance info', 13, 'add_attendanceinfo'),
(50, 'Can change attendance info', 13, 'change_attendanceinfo'),
(51, 'Can delete attendance info', 13, 'delete_attendanceinfo'),
(52, 'Can view attendance info', 13, 'view_attendanceinfo');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$320000$LesNZkJOZpoN5oltGGe2Sk$PWRweqovOSrJC8OlJ1uZOSJFH9nq1fhIOmKO2vT7ptc=', '2023-02-07 16:10:31.220642', 1, 'admin', 'Chu Minh', 'Nam', 'chuminhnamma@gmail.com', 1, 1, '2023-02-01 05:58:25.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci DEFAULT NULL,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-02-01 06:00:14.713305', '1', 'admin', 1, '[{\"added\": {}}]', 7, 1),
(2, '2023-02-01 06:01:28.774025', '1', 'Công Nghệ Thông Tin', 1, '[{\"added\": {}}]', 9, 1),
(3, '2023-02-01 06:01:36.605119', '2', 'Thương Mại Điện Tử', 1, '[{\"added\": {}}]', 9, 1),
(4, '2023-02-01 06:01:48.580736', '3', 'Mạng Lưới Điện', 1, '[{\"added\": {}}]', 9, 1),
(5, '2023-02-01 06:01:56.195173', '4', 'Tài Chính Ngân Hàng', 1, '[{\"added\": {}}]', 9, 1),
(6, '2023-02-01 06:02:06.997491', '5', 'Tự Động Hóa', 1, '[{\"added\": {}}]', 9, 1),
(7, '2023-02-01 06:02:15.855797', '6', 'Xây Dựng Công Trình', 1, '[{\"added\": {}}]', 9, 1),
(8, '2023-02-01 06:02:47.034460', '1', 'D15CNPM1', 1, '[{\"added\": {}}]', 8, 1),
(9, '2023-02-01 06:02:59.020596', '2', 'D15CNPM2', 1, '[{\"added\": {}}]', 8, 1),
(10, '2023-02-01 06:03:11.349219', '3', 'D15CNPM3', 1, '[{\"added\": {}}]', 8, 1),
(11, '2023-02-01 06:03:21.651646', '4', 'D15CNPM4', 1, '[{\"added\": {}}]', 8, 1),
(12, '2023-02-01 06:03:36.314511', '5', 'D15CNPM5', 1, '[{\"added\": {}}]', 8, 1),
(13, '2023-02-01 06:03:50.250524', '6', 'D15TMDT1', 1, '[{\"added\": {}}]', 8, 1),
(14, '2023-02-01 06:04:05.198606', '7', 'D15TDH1', 1, '[{\"added\": {}}]', 8, 1),
(15, '2023-02-01 06:04:28.571954', '1', 'Kỹ Thuật Lập Trình |  ', 1, '[{\"added\": {}}]', 11, 1),
(16, '2023-02-01 06:04:44.641933', '1', 'admin', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]', 4, 1),
(17, '2023-02-01 06:05:12.022537', '2', 'Lập Trình Hướng Đối Tượng | Chu Minh Nam', 1, '[{\"added\": {}}]', 11, 1),
(18, '2023-02-01 06:05:28.351070', '3', 'Cấu Trúc Dữ Liệu & Giải Thuật | Chu Minh Nam', 1, '[{\"added\": {}}]', 11, 1),
(19, '2023-02-01 06:05:53.702977', '4', 'Nhập Môn Học Máy | Chu Minh Nam', 1, '[{\"added\": {}}]', 11, 1),
(20, '2023-02-01 06:06:18.627403', '5', 'Kinh Tế Đại Cương | Chu Minh Nam', 1, '[{\"added\": {}}]', 11, 1),
(21, '2023-02-01 06:07:30.385757', '1', 'Nguyễn Tiến Đạt - D15CNPM1', 1, '[{\"added\": {}}]', 10, 1),
(22, '2023-02-01 06:08:05.620774', '2', 'Trần Thị Hương - D15CNPM1', 1, '[{\"added\": {}}]', 10, 1),
(23, '2023-02-01 06:08:38.009064', '3', 'Đào Bá Hưng - D15CNPM1', 1, '[{\"added\": {}}]', 10, 1),
(24, '2023-02-01 06:09:22.719757', '4', 'Chu Thành Nam - D15CNPM1', 1, '[{\"added\": {}}]', 10, 1),
(25, '2023-02-01 06:09:55.216020', '5', 'Trần Ngọc Hà - D15CNPM2', 1, '[{\"added\": {}}]', 10, 1),
(26, '2023-02-01 06:10:56.404953', '6', 'Trần Anh Tuấn - D15CNPM2', 1, '[{\"added\": {}}]', 10, 1),
(27, '2023-02-01 06:11:28.343706', '7', 'Trương Mai Anh - D15CNPM2', 1, '[{\"added\": {}}]', 10, 1),
(28, '2023-02-01 06:12:11.121380', '8', 'Đào Bá Hùng - D15CNPM2', 1, '[{\"added\": {}}]', 10, 1),
(29, '2023-02-01 06:13:07.661251', '9', 'Trương Hướng Dương - D15CNPM3', 1, '[{\"added\": {}}]', 10, 1),
(30, '2023-02-01 06:13:39.538015', '10', 'Đào Yến Nhi - D15CNPM3', 1, '[{\"added\": {}}]', 10, 1),
(31, '2023-02-01 06:14:28.417427', '11', 'Trương Văn Định - D15CNPM3', 1, '[{\"added\": {}}]', 10, 1),
(32, '2023-02-01 06:15:16.751819', '12', 'Dương Ngọc Tú - D15CNPM3', 1, '[{\"added\": {}}]', 10, 1),
(33, '2023-02-01 06:15:56.254073', '13', 'Lê Thu Thảo - D15TMDT1', 1, '[{\"added\": {}}]', 10, 1),
(34, '2023-02-01 06:17:08.101869', '1', 'Kỹ Thuật Lập Trình - Trần Ngọc Hà', 1, '[{\"added\": {}}]', 12, 1),
(35, '2023-02-01 06:19:29.473317', '8', 'D15TCNH1', 1, '[{\"added\": {}}]', 8, 1),
(36, '2023-02-02 07:29:05.119984', '1', 'Kỹ Thuật Lập Trình - Trần Ngọc Hà', 2, '[]', 12, 1),
(37, '2023-02-02 07:29:09.449746', '1', 'Kỹ Thuật Lập Trình - Trần Ngọc Hà', 2, '[]', 12, 1),
(38, '2023-02-02 07:29:14.506025', '2', 'Kỹ Thuật Lập Trình - Đào Bá Hùng', 2, '[]', 12, 1),
(39, '2023-02-02 07:29:19.121773', '3', 'Kỹ Thuật Lập Trình - Trần Anh Tuấn', 2, '[]', 12, 1),
(40, '2023-02-08 13:02:07.277352', '3', 'D15CNPM3 - Kỹ Thuật Lập Trình - 2023-02-08', 3, '', 13, 1),
(41, '2023-02-08 13:02:07.311259', '2', 'D15CNPM1 - Kỹ Thuật Lập Trình - 2023-02-08', 3, '', 13, 1),
(42, '2023-02-08 13:02:07.313254', '1', 'D15CNPM2 - Kỹ Thuật Lập Trình - 2023-02-08', 3, '', 13, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(13, 'attendance', 'attendanceinfo'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(12, 'scores', 'scores'),
(6, 'sessions', 'session'),
(8, 'students', 'classname'),
(9, 'students', 'specialization'),
(10, 'students', 'students'),
(11, 'subjects', 'subject'),
(7, 'user', 'infouser');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-02-01 05:57:25.198344'),
(2, 'auth', '0001_initial', '2023-02-01 05:57:25.675588'),
(3, 'admin', '0001_initial', '2023-02-01 05:57:25.781872'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-02-01 05:57:25.790849'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-02-01 05:57:25.800617'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-02-01 05:57:25.862587'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-02-01 05:57:25.912267'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-02-01 05:57:25.966147'),
(9, 'auth', '0004_alter_user_username_opts', '2023-02-01 05:57:25.973676'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-02-01 05:57:26.020924'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-02-01 05:57:26.025924'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-02-01 05:57:26.034887'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-02-01 05:57:26.052691'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-02-01 05:57:26.069311'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-02-01 05:57:26.124124'),
(16, 'auth', '0011_update_proxy_permissions', '2023-02-01 05:57:26.134172'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-02-01 05:57:26.150134'),
(18, 'students', '0001_initial', '2023-02-01 05:57:26.303749'),
(19, 'students', '0002_alter_students_specialization', '2023-02-01 05:57:26.408485'),
(20, 'students', '0003_students_status', '2023-02-01 05:57:26.427937'),
(21, 'students', '0004_classname_slug', '2023-02-01 05:57:26.471851'),
(22, 'user', '0001_initial', '2023-02-01 05:57:26.606945'),
(23, 'user', '0002_delete_subject', '2023-02-01 05:57:26.617251'),
(24, 'subjects', '0001_initial', '2023-02-01 05:57:26.696275'),
(25, 'subjects', '0002_subject_teaching', '2023-02-01 05:57:26.721206'),
(26, 'subjects', '0003_subject_specialization', '2023-02-01 05:57:26.769494'),
(27, 'subjects', '0004_subject_slug', '2023-02-01 05:57:26.817689'),
(28, 'scores', '0001_initial', '2023-02-01 05:57:27.025261'),
(29, 'scores', '0002_alter_scores_classname_alter_scores_specialization', '2023-02-01 05:57:27.451519'),
(30, 'sessions', '0001_initial', '2023-02-01 05:57:27.486973'),
(31, 'scores', '0003_scores_sum', '2023-02-02 07:28:48.963463'),
(32, 'attendance', '0001_initial', '2023-02-08 10:23:10.925673');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('422klpv721ditnatyvmcgbnvpv1y14oa', '.eJxVjDsOwjAQBe_iGln-xRtT0nMGa71e4wBypDipEHeHSCmgfTPzXiLitta4dV7ilMVZaHH63RLSg9sO8h3bbZY0t3WZktwVedAur3Pm5-Vw_w4q9vqtvdXkRsjWFwWJwCArr2GwBlRmSnYspJw3xlkHpvgccHAUKKRUgInE-wPJZDfV:1pOdXL:KR1GZnIrI38m6RZZQwQkeONEeGARZ_UNSwtMFrYfm_k', '2023-02-19 11:50:23.440026'),
('67m0ulj2bo9ilce9u7j5ohr73i1cafck', '.eJxVjDsOwjAQBe_iGln-xRtT0nMGa71e4wBypDipEHeHSCmgfTPzXiLitta4dV7ilMVZaHH63RLSg9sO8h3bbZY0t3WZktwVedAur3Pm5-Vw_w4q9vqtvdXkRsjWFwWJwCArr2GwBlRmSnYspJw3xlkHpvgccHAUKKRUgInE-wPJZDfV:1pNeOJ:H27BDfTSJFiJbi4qRNSYQ_G6ans7Wjx5J6CsDlNdrI4', '2023-02-16 18:32:59.740154'),
('mz292jm9x77ek1vh51ujfrbxtco8nzhn', '.eJxVjDsOwjAQBe_iGln-xRtT0nMGa71e4wBypDipEHeHSCmgfTPzXiLitta4dV7ilMVZaHH63RLSg9sO8h3bbZY0t3WZktwVedAur3Pm5-Vw_w4q9vqtvdXkRsjWFwWJwCArr2GwBlRmSnYspJw3xlkHpvgccHAUKKRUgInE-wPJZDfV:1pNeJo:3XfkKBfOzUmHZZsBDqT22KU1PIgPGtZvuGRbQ7tW2rE', '2023-02-16 18:28:20.311000'),
('odnl6cgi01dvxhqkeasw5wvz3bij2sc8', '.eJxVjDsOwjAQBe_iGln-xRtT0nMGa71e4wBypDipEHeHSCmgfTPzXiLitta4dV7ilMVZaHH63RLSg9sO8h3bbZY0t3WZktwVedAur3Pm5-Vw_w4q9vqtvdXkRsjWFwWJwCArr2GwBlRmSnYspJw3xlkHpvgccHAUKKRUgInE-wPJZDfV:1pNeJo:3XfkKBfOzUmHZZsBDqT22KU1PIgPGtZvuGRbQ7tW2rE', '2023-02-16 18:28:20.401757'),
('szmdr9bnpttlxx7andqg7bps49x3dyad', '.eJxVjDsOwjAQBe_iGln-xRtT0nMGa71e4wBypDipEHeHSCmgfTPzXiLitta4dV7ilMVZaHH63RLSg9sO8h3bbZY0t3WZktwVedAur3Pm5-Vw_w4q9vqtvdXkRsjWFwWJwCArr2GwBlRmSnYspJw3xlkHpvgccHAUKKRUgInE-wPJZDfV:1pNeOJ:H27BDfTSJFiJbi4qRNSYQ_G6ans7Wjx5J6CsDlNdrI4', '2023-02-16 18:32:59.822926'),
('z4kfkx3k9ppje18xyl7rcnedgay9hen0', '.eJxVjDsOwjAQBe_iGln-xRtT0nMGa71e4wBypDipEHeHSCmgfTPzXiLitta4dV7ilMVZaHH63RLSg9sO8h3bbZY0t3WZktwVedAur3Pm5-Vw_w4q9vqtvdXkRsjWFwWJwCArr2GwBlRmSnYspJw3xlkHpvgccHAUKKRUgInE-wPJZDfV:1pPQYB:NaIaMvhpQoTbUSgE4C_wufkzS0R0u7pUUzyVq6Qt2Ek', '2023-02-21 16:10:31.224629');

-- --------------------------------------------------------

--
-- Table structure for table `scores_scores`
--

CREATE TABLE `scores_scores` (
  `id` bigint(20) NOT NULL,
  `score1` double NOT NULL,
  `score2` double NOT NULL,
  `score3` double NOT NULL,
  `classname_id` bigint(20) DEFAULT NULL,
  `specialization_id` bigint(20) DEFAULT NULL,
  `student_id` bigint(20) NOT NULL,
  `subject_id` bigint(20) NOT NULL,
  `sum` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `scores_scores`
--

INSERT INTO `scores_scores` (`id`, `score1`, `score2`, `score3`, `classname_id`, `specialization_id`, `student_id`, `subject_id`, `sum`) VALUES
(1, 10, 9, 8, 2, 1, 5, 1, 8.399999999999999),
(2, 5, 6, 7, 2, 1, 8, 1, 6.6),
(3, 5, 5, 5, 2, 1, 6, 1, 5),
(4, 10, 10, 5, 2, 1, 7, 1, 6.5);

-- --------------------------------------------------------

--
-- Table structure for table `students_classname`
--

CREATE TABLE `students_classname` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `number` int(11) NOT NULL,
  `specialization_id` bigint(20) NOT NULL,
  `slug` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `students_classname`
--

INSERT INTO `students_classname` (`id`, `name`, `number`, `specialization_id`, `slug`) VALUES
(1, 'D15CNPM1', 70, 1, 'd15cnpm1'),
(2, 'D15CNPM2', 80, 1, 'd15cnpm2'),
(3, 'D15CNPM3', 65, 1, 'd15cnpm3'),
(4, 'D15CNPM4', 70, 1, 'd15cnpm4'),
(5, 'D15CNPM5', 85, 1, 'd15cnpm5'),
(6, 'D15TMDT1', 60, 2, 'd15tmdt1'),
(7, 'D15TDH1', 60, 5, 'd15tdh1'),
(8, 'D15TCNH1', 60, 4, 'd15tcnh1');

-- --------------------------------------------------------

--
-- Table structure for table `students_specialization`
--

CREATE TABLE `students_specialization` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `students_specialization`
--

INSERT INTO `students_specialization` (`id`, `name`) VALUES
(1, 'Công Nghệ Thông Tin'),
(2, 'Thương Mại Điện Tử'),
(3, 'Mạng Lưới Điện'),
(4, 'Tài Chính Ngân Hàng'),
(5, 'Tự Động Hóa'),
(6, 'Xây Dựng Công Trình');

-- --------------------------------------------------------

--
-- Table structure for table `students_students`
--

CREATE TABLE `students_students` (
  `id` bigint(20) NOT NULL,
  `fullname` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `birthday` date NOT NULL,
  `gender` tinyint(1) NOT NULL,
  `address` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `avatar` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `specialization_id` bigint(20) NOT NULL,
  `joining_date` date NOT NULL,
  `classname_id` bigint(20) NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `students_students`
--

INSERT INTO `students_students` (`id`, `fullname`, `birthday`, `gender`, `address`, `avatar`, `phone`, `specialization_id`, `joining_date`, `classname_id`, `status`) VALUES
(1, 'Chu Minh Nam', '1995-05-06', 1, 'Xuân Phương, Hà Đông, Hà Nội', 'students/avatar.png', '035695628', 1, '2023-02-01', 1, 1),
(2, 'Trần Thị Hương', '1999-03-02', 0, 'Phương Canh, Cầu Giấy, Hà Nội', 'students/anh-avatar-facebook-nu-toc-dai-buoc-no_SFASJlM.jpg', '0368523559', 1, '2023-02-01', 1, 1),
(3, 'Đào Bá Hưng', '2001-05-09', 1, 'Hồng Đức, Thụy Phương, Hà Nội', 'students/anh-dai-dien-dep_yle5UY4.jpg', '0369862658', 1, '2023-02-01', 1, 1),
(4, 'Chu Thành Nam', '2000-09-29', 1, 'Dịch Vọng Hậu, Cầu Giấy, Hà Nội', 'students/anh-avatar-supreme-dep-lam-dai-dien-facebook_gg8b2dt.jpg', '0986223586', 1, '2023-02-01', 1, 1),
(5, 'Trần Ngọc Hà', '2002-11-14', 0, 'Xuân Đỉnh, Bắc Từ Liêm, Hà Nội', 'students/anh-avatar-facebook-nu-toc-dai-buoc-no_swYemHh.jpg', '0999888999', 1, '2023-02-01', 2, 1),
(6, 'Trần Anh Tuấn', '2000-05-03', 1, 'Cổ Nhuế, Bắc Từ Liêm, Hà Nội', 'students/anh-dai-dien-dep_lTp7VKX.jpg', '0685956262', 1, '2023-02-01', 2, 1),
(7, 'Trương Mai Anh', '2000-08-09', 0, 'Hồng Phước, Thụy Phương, Hà Nội', 'students/anh-avatar-facebook-nu-toc-dai-buoc-no_NQom41V.jpg', '0988555666', 1, '2023-02-01', 2, 1),
(8, 'Đào Bá Hùng', '2000-06-03', 1, 'Xuân La, Tây Hồ, Hà Nội', 'students/anh-dai-dien-dep_EyPToFu.jpg', '0563256985', 1, '2023-02-01', 2, 1),
(9, 'Trương Hướng Dương', '2000-03-29', 1, 'Tây Sơn, Thanh Xuân, Hà Nội', 'students/anh-avatar-supreme-dep-lam-dai-dien-facebook_0N1rPtS.jpg', '0354629565', 1, '2023-02-01', 3, 1),
(10, 'Đào Yến Nhi', '2000-06-03', 0, 'Xuân Thủy, Cầu Giấy, Hà Nội', 'students/anh-avatar-facebook-nu-toc-dai-buoc-no_iBdTcnN.jpg', '0689623658', 1, '2023-02-01', 3, 1),
(11, 'Trương Văn Định', '2000-06-10', 1, 'Trương Đình, Ba Đình, Hà Nội', 'students/anh-dai-dien-dep_aYdfNVq.jpg', '0598632658', 1, '2023-02-01', 3, 1),
(12, 'Dương Ngọc Tú', '2000-06-14', 1, 'Thăng Long, Đông Anh, Hà Nội', 'students/anh-dai-dien-dep_XNezpt4.jpg', '0359862658', 1, '2023-02-01', 3, 1),
(13, 'Lê Thu Thảo', '2000-03-28', 0, 'Tây Đô, Đan Phượng, Hà Nội', 'students/anh-avatar-facebook-nu-toc-dai-buoc-no_9guT3xK.jpg', '0398626589', 1, '2023-02-01', 6, 1),
(14, 'Trần Đức Hoàng', '2000-06-05', 1, 'Ngọc Tảo, Phúc Thọ, Hà Nội', 'students/328714325_2219018465154114_7649671539834980274_n.jpg', '0658975324', 1, '2023-02-03', 5, 1),
(15, 'Phùng Tiến Đạt', '2000-06-05', 1, 'Ngọc Hồi, Phúc Thọ, Hà Nội', 'students/anh-dai-dien-dep.jpg', '0989632658', 1, '2023-02-03', 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `subjects_subject`
--

CREATE TABLE `subjects_subject` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `credits` int(11) NOT NULL,
  `infouser_id` bigint(20) NOT NULL,
  `teaching` tinyint(1) NOT NULL,
  `specialization_id` bigint(20) DEFAULT NULL,
  `slug` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `subjects_subject`
--

INSERT INTO `subjects_subject` (`id`, `name`, `credits`, `infouser_id`, `teaching`, `specialization_id`, `slug`) VALUES
(1, 'Kỹ Thuật Lập Trình', 3, 1, 1, 1, 'ky-thuat-lap-trinh'),
(2, 'Lập Trình Hướng Đối Tượng', 2, 1, 1, 1, 'lap-trinh-huong-oi-tuong'),
(3, 'Cấu Trúc Dữ Liệu & Giải Thuật', 3, 1, 1, 1, 'cau-truc-du-lieu-giai-thuat'),
(4, 'Nhập Môn Học Máy', 3, 1, 1, 1, 'nhap-mon-hoc-may'),
(5, 'Kinh Tế Đại Cương', 3, 1, 1, 4, 'kinh-te-ai-cuong'),
(6, 'Lập Trình Python', 1, 1, 1, 1, 'lap-trinh-python'),
(7, 'Phân Tích Thiết Kế Hướng Đối Tượng', 3, 1, 1, 1, 'phan-tich-thiet-ke-huong-oi-tuong');

-- --------------------------------------------------------

--
-- Table structure for table `user_infouser`
--

CREATE TABLE `user_infouser` (
  `id` bigint(20) NOT NULL,
  `avatar` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `birthday` date NOT NULL,
  `address` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `specialization` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `user_infouser`
--

INSERT INTO `user_infouser` (`id`, `avatar`, `phone`, `birthday`, `address`, `specialization`, `user_id`) VALUES
(1, 'uploads/avatar_uWbV5vI.png', '0379962045', '1988-02-07', 'Mĩ Đình, Nam Từ Liêm, Hà Nội', 'Công Nghệ Thông Tin', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance_attendanceinfo`
--
ALTER TABLE `attendance_attendanceinfo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `attendance_attendanc_classname_id_c9d4ce45_fk_students_` (`classname_id`),
  ADD KEY `attendance_attendanc_student_id_73fa65c5_fk_students_` (`student_id`),
  ADD KEY `attendance_attendanc_subject_id_c8d9f584_fk_subjects_` (`subject_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `scores_scores`
--
ALTER TABLE `scores_scores`
  ADD PRIMARY KEY (`id`),
  ADD KEY `scores_scores_student_id_5c60b6c9_fk_students_students_id` (`student_id`),
  ADD KEY `scores_scores_subject_id_f87bd7b3_fk_subjects_subject_id` (`subject_id`),
  ADD KEY `scores_scores_classname_id_ab8300da_fk_students_classname_id` (`classname_id`),
  ADD KEY `scores_scores_specialization_id_86562481_fk_students_` (`specialization_id`);

--
-- Indexes for table `students_classname`
--
ALTER TABLE `students_classname`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `students_classname_specialization_id_c0b8d163_fk_students_` (`specialization_id`);

--
-- Indexes for table `students_specialization`
--
ALTER TABLE `students_specialization`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students_students`
--
ALTER TABLE `students_students`
  ADD PRIMARY KEY (`id`),
  ADD KEY `students_students_classname_id_ad068c05_fk_students_classname_id` (`classname_id`),
  ADD KEY `students_students_specialization_id_3dec1801` (`specialization_id`);

--
-- Indexes for table `subjects_subject`
--
ALTER TABLE `subjects_subject`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `subjects_subject_infouser_id_34301fc9_fk_user_infouser_id` (`infouser_id`),
  ADD KEY `subjects_subject_specialization_id_1c256dd8_fk_students_` (`specialization_id`);

--
-- Indexes for table `user_infouser`
--
ALTER TABLE `user_infouser`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_infouser_user_id_e8aeb529_fk_auth_user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendance_attendanceinfo`
--
ALTER TABLE `attendance_attendanceinfo`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `scores_scores`
--
ALTER TABLE `scores_scores`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `students_classname`
--
ALTER TABLE `students_classname`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `students_specialization`
--
ALTER TABLE `students_specialization`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `students_students`
--
ALTER TABLE `students_students`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `subjects_subject`
--
ALTER TABLE `subjects_subject`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `user_infouser`
--
ALTER TABLE `user_infouser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendance_attendanceinfo`
--
ALTER TABLE `attendance_attendanceinfo`
  ADD CONSTRAINT `attendance_attendanc_classname_id_c9d4ce45_fk_students_` FOREIGN KEY (`classname_id`) REFERENCES `students_classname` (`id`),
  ADD CONSTRAINT `attendance_attendanc_student_id_73fa65c5_fk_students_` FOREIGN KEY (`student_id`) REFERENCES `students_students` (`id`),
  ADD CONSTRAINT `attendance_attendanc_subject_id_c8d9f584_fk_subjects_` FOREIGN KEY (`subject_id`) REFERENCES `subjects_subject` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `scores_scores`
--
ALTER TABLE `scores_scores`
  ADD CONSTRAINT `scores_scores_classname_id_ab8300da_fk_students_classname_id` FOREIGN KEY (`classname_id`) REFERENCES `students_classname` (`id`),
  ADD CONSTRAINT `scores_scores_specialization_id_86562481_fk_students_` FOREIGN KEY (`specialization_id`) REFERENCES `students_specialization` (`id`),
  ADD CONSTRAINT `scores_scores_student_id_5c60b6c9_fk_students_students_id` FOREIGN KEY (`student_id`) REFERENCES `students_students` (`id`),
  ADD CONSTRAINT `scores_scores_subject_id_f87bd7b3_fk_subjects_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subjects_subject` (`id`);

--
-- Constraints for table `students_classname`
--
ALTER TABLE `students_classname`
  ADD CONSTRAINT `students_classname_specialization_id_c0b8d163_fk_students_` FOREIGN KEY (`specialization_id`) REFERENCES `students_specialization` (`id`);

--
-- Constraints for table `students_students`
--
ALTER TABLE `students_students`
  ADD CONSTRAINT `students_students_classname_id_ad068c05_fk_students_classname_id` FOREIGN KEY (`classname_id`) REFERENCES `students_classname` (`id`),
  ADD CONSTRAINT `students_students_specialization_id_3dec1801_fk_students_` FOREIGN KEY (`specialization_id`) REFERENCES `students_specialization` (`id`);

--
-- Constraints for table `subjects_subject`
--
ALTER TABLE `subjects_subject`
  ADD CONSTRAINT `subjects_subject_infouser_id_34301fc9_fk_user_infouser_id` FOREIGN KEY (`infouser_id`) REFERENCES `user_infouser` (`id`),
  ADD CONSTRAINT `subjects_subject_specialization_id_1c256dd8_fk_students_` FOREIGN KEY (`specialization_id`) REFERENCES `students_specialization` (`id`);

--
-- Constraints for table `user_infouser`
--
ALTER TABLE `user_infouser`
  ADD CONSTRAINT `user_infouser_user_id_e8aeb529_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
