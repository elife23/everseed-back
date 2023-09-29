-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.30 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour everseeddb
CREATE DATABASE IF NOT EXISTS `everseeddb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `everseeddb`;

-- Listage de la structure de table everseeddb. auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.auth_group : ~0 rows (environ)

-- Listage de la structure de table everseeddb. auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.auth_group_permissions : ~0 rows (environ)

-- Listage de la structure de table everseeddb. auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.auth_permission : ~64 rows (environ)
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
	(13, 'Can add content type', 4, 'add_contenttype'),
	(14, 'Can change content type', 4, 'change_contenttype'),
	(15, 'Can delete content type', 4, 'delete_contenttype'),
	(16, 'Can view content type', 4, 'view_contenttype'),
	(17, 'Can add session', 5, 'add_session'),
	(18, 'Can change session', 5, 'change_session'),
	(19, 'Can delete session', 5, 'delete_session'),
	(20, 'Can view session', 5, 'view_session'),
	(21, 'Can add user', 6, 'add_user'),
	(22, 'Can change user', 6, 'change_user'),
	(23, 'Can delete user', 6, 'delete_user'),
	(24, 'Can view user', 6, 'view_user'),
	(25, 'Can add meeting', 7, 'add_meeting'),
	(26, 'Can change meeting', 7, 'change_meeting'),
	(27, 'Can delete meeting', 7, 'delete_meeting'),
	(28, 'Can view meeting', 7, 'view_meeting'),
	(29, 'Can add meetingroom', 8, 'add_meetingroom'),
	(30, 'Can change meetingroom', 8, 'change_meetingroom'),
	(31, 'Can delete meetingroom', 8, 'delete_meetingroom'),
	(32, 'Can view meetingroom', 8, 'view_meetingroom'),
	(33, 'Can add subscription', 9, 'add_subscription'),
	(34, 'Can change subscription', 9, 'change_subscription'),
	(35, 'Can delete subscription', 9, 'delete_subscription'),
	(36, 'Can view subscription', 9, 'view_subscription'),
	(37, 'Can add whiteboard', 10, 'add_whiteboard'),
	(38, 'Can change whiteboard', 10, 'change_whiteboard'),
	(39, 'Can delete whiteboard', 10, 'delete_whiteboard'),
	(40, 'Can view whiteboard', 10, 'view_whiteboard'),
	(41, 'Can add usersubscription', 11, 'add_usersubscription'),
	(42, 'Can change usersubscription', 11, 'change_usersubscription'),
	(43, 'Can delete usersubscription', 11, 'delete_usersubscription'),
	(44, 'Can view usersubscription', 11, 'view_usersubscription'),
	(45, 'Can add participant', 12, 'add_participant'),
	(46, 'Can change participant', 12, 'change_participant'),
	(47, 'Can delete participant', 12, 'delete_participant'),
	(48, 'Can view participant', 12, 'view_participant'),
	(49, 'Can add commentwhiteboard', 13, 'add_commentwhiteboard'),
	(50, 'Can change commentwhiteboard', 13, 'change_commentwhiteboard'),
	(51, 'Can delete commentwhiteboard', 13, 'delete_commentwhiteboard'),
	(52, 'Can view commentwhiteboard', 13, 'view_commentwhiteboard'),
	(53, 'Can add commentmeeting', 14, 'add_commentmeeting'),
	(54, 'Can change commentmeeting', 14, 'change_commentmeeting'),
	(55, 'Can delete commentmeeting', 14, 'delete_commentmeeting'),
	(56, 'Can view commentmeeting', 14, 'view_commentmeeting'),
	(57, 'Can add blacklisted token', 15, 'add_blacklistedtoken'),
	(58, 'Can change blacklisted token', 15, 'change_blacklistedtoken'),
	(59, 'Can delete blacklisted token', 15, 'delete_blacklistedtoken'),
	(60, 'Can view blacklisted token', 15, 'view_blacklistedtoken'),
	(61, 'Can add outstanding token', 16, 'add_outstandingtoken'),
	(62, 'Can change outstanding token', 16, 'change_outstandingtoken'),
	(63, 'Can delete outstanding token', 16, 'delete_outstandingtoken'),
	(64, 'Can view outstanding token', 16, 'view_outstandingtoken');

-- Listage de la structure de table everseeddb. commentmeeting
CREATE TABLE IF NOT EXISTS `commentmeeting` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `dateTime` datetime(6) NOT NULL,
  `author` varchar(255) NOT NULL,
  `deleted` int NOT NULL,
  `meetingId` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `commentmeeting_meetingId_2692aa61_fk_meeting_id` (`meetingId`),
  CONSTRAINT `commentmeeting_meetingId_2692aa61_fk_meeting_id` FOREIGN KEY (`meetingId`) REFERENCES `meeting` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.commentmeeting : ~0 rows (environ)

-- Listage de la structure de table everseeddb. commentwhiteboard
CREATE TABLE IF NOT EXISTS `commentwhiteboard` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `dateTime` datetime(6) NOT NULL,
  `author` varchar(255) NOT NULL,
  `deleted` int NOT NULL,
  `whiteboardId` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `commentwhiteboard_whiteboardId_a40998d1_fk_whiteboard_id` (`whiteboardId`),
  CONSTRAINT `commentwhiteboard_whiteboardId_a40998d1_fk_whiteboard_id` FOREIGN KEY (`whiteboardId`) REFERENCES `whiteboard` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.commentwhiteboard : ~0 rows (environ)

-- Listage de la structure de table everseeddb. django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.django_admin_log : ~0 rows (environ)

-- Listage de la structure de table everseeddb. django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.django_content_type : ~16 rows (environ)
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(14, 'backend', 'commentmeeting'),
	(13, 'backend', 'commentwhiteboard'),
	(7, 'backend', 'meeting'),
	(8, 'backend', 'meetingroom'),
	(12, 'backend', 'participant'),
	(9, 'backend', 'subscription'),
	(6, 'backend', 'user'),
	(11, 'backend', 'usersubscription'),
	(10, 'backend', 'whiteboard'),
	(4, 'contenttypes', 'contenttype'),
	(5, 'sessions', 'session'),
	(15, 'token_blacklist', 'blacklistedtoken'),
	(16, 'token_blacklist', 'outstandingtoken');

-- Listage de la structure de table everseeddb. django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.django_migrations : ~30 rows (environ)
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2023-09-26 16:01:33.718585'),
	(2, 'backend', '0001_initial', '2023-09-26 16:01:37.110997'),
	(3, 'admin', '0001_initial', '2023-09-26 16:01:37.771884'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2023-09-26 16:01:37.819877'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-09-26 16:01:37.879865'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2023-09-26 16:01:38.357784'),
	(7, 'auth', '0001_initial', '2023-09-26 16:01:39.724549'),
	(8, 'auth', '0002_alter_permission_name_max_length', '2023-09-26 16:01:40.038497'),
	(9, 'auth', '0003_alter_user_email_max_length', '2023-09-26 16:01:40.104482'),
	(10, 'auth', '0004_alter_user_username_opts', '2023-09-26 16:01:40.159474'),
	(11, 'auth', '0005_alter_user_last_login_null', '2023-09-26 16:01:40.220464'),
	(12, 'auth', '0006_require_contenttypes_0002', '2023-09-26 16:01:40.262455'),
	(13, 'auth', '0007_alter_validators_add_error_messages', '2023-09-26 16:01:40.323445'),
	(14, 'auth', '0008_alter_user_username_max_length', '2023-09-26 16:01:40.379437'),
	(15, 'auth', '0009_alter_user_last_name_max_length', '2023-09-26 16:01:40.436427'),
	(16, 'auth', '0010_alter_group_name_max_length', '2023-09-26 16:01:40.603397'),
	(17, 'auth', '0011_update_proxy_permissions', '2023-09-26 16:01:40.690383'),
	(18, 'auth', '0012_alter_user_first_name_max_length', '2023-09-26 16:01:40.746374'),
	(19, 'sessions', '0001_initial', '2023-09-26 16:01:41.002330'),
	(20, 'token_blacklist', '0001_initial', '2023-09-26 16:01:41.960167'),
	(21, 'token_blacklist', '0002_outstandingtoken_jti_hex', '2023-09-26 16:01:42.104142'),
	(22, 'token_blacklist', '0003_auto_20171017_2007', '2023-09-26 16:01:42.202122'),
	(23, 'token_blacklist', '0004_auto_20171017_2013', '2023-09-26 16:01:42.646047'),
	(24, 'token_blacklist', '0005_remove_outstandingtoken_jti', '2023-09-26 16:01:42.932999'),
	(25, 'token_blacklist', '0006_auto_20171017_2113', '2023-09-26 16:01:43.084971'),
	(26, 'token_blacklist', '0007_auto_20171017_2214', '2023-09-26 16:01:44.054805'),
	(27, 'token_blacklist', '0008_migrate_to_bigautofield', '2023-09-26 16:01:45.129619'),
	(28, 'token_blacklist', '0010_fix_migrate_to_bigautofield', '2023-09-26 16:01:45.220604'),
	(29, 'token_blacklist', '0011_linearizes_history', '2023-09-26 16:01:45.264598'),
	(30, 'token_blacklist', '0012_alter_outstandingtoken_user', '2023-09-26 16:01:45.345584');

-- Listage de la structure de table everseeddb. django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.django_session : ~0 rows (environ)

-- Listage de la structure de table everseeddb. meeting
CREATE TABLE IF NOT EXISTS `meeting` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `dateTime` datetime(6) NOT NULL,
  `duration` decimal(10,0) NOT NULL,
  `deleted` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.meeting : ~0 rows (environ)

-- Listage de la structure de table everseeddb. meetingroom
CREATE TABLE IF NOT EXISTS `meetingroom` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `maxCapacity` int NOT NULL,
  `deleted` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.meetingroom : ~0 rows (environ)

-- Listage de la structure de table everseeddb. participant
CREATE TABLE IF NOT EXISTS `participant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(255) NOT NULL,
  `meetingId` bigint NOT NULL,
  `userId` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `participant_meetingId_43c0da8b_fk_meeting_id` (`meetingId`),
  KEY `participant_userId_f702efd8_fk_user_id` (`userId`),
  CONSTRAINT `participant_meetingId_43c0da8b_fk_meeting_id` FOREIGN KEY (`meetingId`) REFERENCES `meeting` (`id`),
  CONSTRAINT `participant_userId_f702efd8_fk_user_id` FOREIGN KEY (`userId`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.participant : ~0 rows (environ)

-- Listage de la structure de table everseeddb. subscription
CREATE TABLE IF NOT EXISTS `subscription` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `price` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.subscription : ~0 rows (environ)

-- Listage de la structure de table everseeddb. token_blacklist_blacklistedtoken
CREATE TABLE IF NOT EXISTS `token_blacklist_blacklistedtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `blacklisted_at` datetime(6) NOT NULL,
  `token_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_id` (`token_id`),
  CONSTRAINT `token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk` FOREIGN KEY (`token_id`) REFERENCES `token_blacklist_outstandingtoken` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.token_blacklist_blacklistedtoken : ~0 rows (environ)

-- Listage de la structure de table everseeddb. token_blacklist_outstandingtoken
CREATE TABLE IF NOT EXISTS `token_blacklist_outstandingtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `expires_at` datetime(6) NOT NULL,
  `user_id` bigint DEFAULT NULL,
  `jti` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq` (`jti`),
  KEY `token_blacklist_outstandingtoken_user_id_83bc629a_fk_user_id` (`user_id`),
  CONSTRAINT `token_blacklist_outstandingtoken_user_id_83bc629a_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.token_blacklist_outstandingtoken : ~4 rows (environ)
INSERT INTO `token_blacklist_outstandingtoken` (`id`, `token`, `created_at`, `expires_at`, `user_id`, `jti`) VALUES
	(1, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NTgzMzM2NCwiaWF0IjoxNjk1NzQ2OTY0LCJqdGkiOiIwMGQyMmQ0ODYzYjY0MmYyOTFhZTY3ZjRlZGJlYzA1MyIsInVzZXJfaWQiOjF9.Du6RWbY8jodkpRxTP55VI2iCfGvpv-Rys-E9UUp5Ht4', '2023-09-26 16:49:24.778889', '2023-09-27 16:49:24.000000', 1, '00d22d4863b642f291ae67f4edbec053'),
	(2, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NTgzMzQwNCwiaWF0IjoxNjk1NzQ3MDA0LCJqdGkiOiI1ZDMyNTVhZDYzNGU0MDJlYTcyOTNmN2U5YWMwYWEzOCIsInVzZXJfaWQiOjF9.UDW4ZZUYB8aeMeag8joa50GNcmrth-77yRM8BrW_xak', '2023-09-26 16:50:04.930079', '2023-09-27 16:50:04.000000', 1, '5d3255ad634e402ea7293f7e9ac0aa38'),
	(3, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NTgzNDA1MSwiaWF0IjoxNjk1NzQ3NjUxLCJqdGkiOiJjOWIyZDFlMTU1NDA0OGI2YWY2YTAyZDNkYjQ5OTVmMiIsInVzZXJfaWQiOjF9.d4xbjV3Zg37uaHmhU4a-IKjXbKAqjbWue2OtVAKL_NU', '2023-09-26 17:00:51.161814', '2023-09-27 17:00:51.000000', 1, 'c9b2d1e1554048b6af6a02d3db4995f2'),
	(4, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NTgzNTI3MSwiaWF0IjoxNjk1NzQ4ODcxLCJqdGkiOiJkYzEwZjhjOWQ3ZmY0YmVjYWU4YjM2NjUzY2RiYWUwYiIsInVzZXJfaWQiOjF9.hmA24bSePJpPrJ9bWrOeFsPUleaNdcadVcLHiPuOfPE', '2023-09-26 17:21:11.730879', '2023-09-27 17:21:11.000000', 1, 'dc10f8c9d7ff4becae8b36653cdbae0b'),
	(5, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NTgzNjQzMCwiaWF0IjoxNjk1NzUwMDMwLCJqdGkiOiJiZjEzYjA5ZmJhYWQ0YjFmYTQ1ZWNlMTc4NGMwOTc0ZiIsInVzZXJfaWQiOjF9.-HqcczkpxNi2GCm34CXPBzUeFytc7rNcCXCHk6KJp34', '2023-09-26 17:40:30.881018', '2023-09-27 17:40:30.000000', 1, 'bf13b09fbaad4b1fa45ece1784c0974f');

-- Listage de la structure de table everseeddb. user
CREATE TABLE IF NOT EXISTS `user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `deleted` int NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `firstname` (`firstname`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.user : ~2 rows (environ)
INSERT INTO `user` (`id`, `password`, `firstname`, `lastname`, `email`, `deleted`, `is_admin`) VALUES
	(1, 'pbkdf2_sha256$600000$C7M6kcFLxrgf5jzlqYYLOW$zYxEz3zjN4j2Ccls+8yJAhFfVNV/RW6SfDQ3Y/HRuMc=', 'Blast', 'max', 'maxsm_d12@gmail.com', 0, 0),
	(2, 'pbkdf2_sha256$600000$wQphxV50zNtnoUUuZKOCGA$utJxYuRr4dLQnWL7raVzSyLfh+LmzthXduNYGSMCCJs=', 'Youko', 'Yorgan', 'bladsf_ds12@gmail.com', 0, 0);

-- Listage de la structure de table everseeddb. usersubscription
CREATE TABLE IF NOT EXISTS `usersubscription` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `expirationDate` datetime(6) NOT NULL,
  `deleted` int NOT NULL,
  `subscriptionId` bigint NOT NULL,
  `userId` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usersubscription_subscriptionId_b898521c_fk_subscription_id` (`subscriptionId`),
  KEY `usersubscription_userId_79176f01_fk_user_id` (`userId`),
  CONSTRAINT `usersubscription_subscriptionId_b898521c_fk_subscription_id` FOREIGN KEY (`subscriptionId`) REFERENCES `subscription` (`id`),
  CONSTRAINT `usersubscription_userId_79176f01_fk_user_id` FOREIGN KEY (`userId`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.usersubscription : ~0 rows (environ)

-- Listage de la structure de table everseeddb. whiteboard
CREATE TABLE IF NOT EXISTS `whiteboard` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table everseeddb.whiteboard : ~0 rows (environ)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
