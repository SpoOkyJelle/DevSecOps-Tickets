-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Gegenereerd op: 15 mrt 2021 om 14:16
-- Serverversie: 8.0.21
-- PHP-versie: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_tickets`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `tickets`
--

DROP TABLE IF EXISTS `tickets`;
CREATE TABLE IF NOT EXISTS `tickets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ticket_name` varchar(255) NOT NULL,
  `ticket_description` varchar(255) NOT NULL,
  `solved` tinyint(1) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Gegevens worden geëxporteerd voor tabel `tickets`
--

INSERT INTO `tickets` (`id`, `ticket_name`, `ticket_description`, `solved`, `created_at`) VALUES
(1, 'Systeem', 'Waarom werkt dit systeem niet', NULL, '2021-03-12 10:23:22.000000'),
(2, 'Hey deze doet het', 'Moeie kieken man', 1, '2021-03-12 10:28:00.000000'),
(3, 'nog een', 'asdasdasd', NULL, '2021-03-12 10:37:14.000000'),
(4, 'iausdasdhf', 'hafkjsdfhkjasdhfkjasd', NULL, '2021-03-12 10:37:14.000000'),
(5, 'Fakka neem', 'asjdhaksjdhakjsd', NULL, '2021-03-10 10:37:36.000000'),
(6, 'asd', 'asd', NULL, '2021-03-12 10:56:58.856293'),
(7, 'Fakka neef', 'Wolah me', 1, '2021-03-12 10:59:09.783157'),
(8, 'Nog een test wejo', 'Hihi kijk mij dan', NULL, '2021-03-12 13:19:31.403294');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
