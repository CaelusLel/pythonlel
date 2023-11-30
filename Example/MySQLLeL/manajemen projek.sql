CREATE DATABASE IF NOT EXISTS pengelolaan_proyek;

USE pengelolaan_proyek;

CREATE TABLE IF NOT EXISTS proyek (
    id_proyek INT AUTO_INCREMENT PRIMARY KEY,
    nama_proyek VARCHAR(255) NOT NULL,
    tanggal_mulai DATE NOT NULL,
    tanggal_selesai DATE
);

CREATE TABLE IF NOT EXISTS tugas (
    id_tugas INT AUTO_INCREMENT PRIMARY KEY,
    id_proyek INT,
    nama_tugas VARCHAR(255) NOT NULL,
    status ENUM('Belum Selesai', 'Selesai') DEFAULT 'Belum Selesai',
    tenggat_waktu DATE,
    FOREIGN KEY (id_proyek) REFERENCES proyek(id_proyek)
);

CREATE TABLE IF NOT EXISTS anggota_tim (
    id_anggota INT AUTO_INCREMENT PRIMARY KEY,
    id_proyek INT,
    nama_anggota VARCHAR(255) NOT NULL,
    posisi VARCHAR(255),
    FOREIGN KEY (id_proyek) REFERENCES proyek(id_proyek)
);
