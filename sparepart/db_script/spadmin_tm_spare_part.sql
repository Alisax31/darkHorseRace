-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: spadmin
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tm_spare_part`
--

DROP TABLE IF EXISTS `tm_spare_part`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tm_spare_part` (
  `sid` int NOT NULL AUTO_INCREMENT,
  `sno` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `desc` text COLLATE utf8_bin,
  `amount` int DEFAULT NULL,
  `price_per_unit` double DEFAULT NULL,
  `total_price` double DEFAULT NULL,
  `asset_no` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  `i_warehouse_date` datetime DEFAULT NULL,
  `p_type` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `o_warehouse_date` datetime DEFAULT NULL,
  PRIMARY KEY (`sid`),
  KEY `sno_index` (`sno`) /*!80000 INVISIBLE */,
  KEY `asset_no_index` (`asset_no`) /*!80000 INVISIBLE */,
  KEY `sno_asset_no_index` (`sno`,`asset_no`),
  KEY `sno_asset_no_date_index` (`sno`,`asset_no`,`o_warehouse_date`)
) ENGINE=InnoDB AUTO_INCREMENT=334762 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-22 17:43:23
