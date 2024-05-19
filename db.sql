CREATE DATABASE /*!32312 IF NOT EXISTS*/`community_law_db` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `community_law_db`;

/*Table structure for table `noti` */

DROP TABLE IF EXISTS `noti`;

CREATE TABLE `noti` (
  `n_id` int(11) NOT NULL AUTO_INCREMENT,
  `b_id` int(11) DEFAULT NULL,
  KEY `n_id` (`n_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `register` */

DROP TABLE IF EXISTS `register`;

CREATE TABLE `register` (
  `l_id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) default NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`l_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `register` */

insert  into `register`(`l_id`,`fname`,`email`,`password`) values 
(1,'admin','admin@gamil.com','admin');