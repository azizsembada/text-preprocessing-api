-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 02 Feb 2020 pada 02.02
-- Versi server: 10.4.8-MariaDB
-- Versi PHP: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `text_preprocessing_auth`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `md_users`
--

CREATE TABLE `md_users` (
  `users_id` bigint(20) NOT NULL,
  `user_fullname` varchar(30) NOT NULL,
  `access_token` text NOT NULL,
  `access_token_secret` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `md_users`
--

INSERT INTO `md_users` (`users_id`, `user_fullname`, `access_token`, `access_token_secret`) VALUES
(1, 'buruhkoding', 'faa8b4e04305538892b10a08b873049c', '$2y$10$UNjpg8tDMq.tSqCmcOvtLO2qvGfLOXlctkYqm5Wo9V9vo3UQkRu.m');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `md_users`
--
ALTER TABLE `md_users`
  ADD PRIMARY KEY (`users_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
