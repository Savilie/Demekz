-- MySQL dump 10.13  Distrib 8.2.0, for Win64 (x86_64)
--
-- Host: localhost    Database: chitaigorod
-- ------------------------------------------------------
-- Server version	8.2.0

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
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Учебник для вузов'),(2,'Учебное пособие'),(3,'Хрестоматия'),(4,'Художественная литература');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturers`
--

DROP TABLE IF EXISTS `manufacturers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturers`
--

LOCK TABLES `manufacturers` WRITE;
/*!40000 ALTER TABLE `manufacturers` DISABLE KEYS */;
INSERT INTO `manufacturers` VALUES (1,'Амрита-Русь'),(2,'Аспект Пресс'),(3,'ВКН'),(4,'Время'),(5,'Златоуст'),(6,'Лениздат'),(7,'Неолит'),(8,'Прогресс книга'),(9,'Т8 Издательские технологии'),(10,'Яуза');
/*!40000 ALTER TABLE `manufacturers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_items`
--

DROP TABLE IF EXISTS `order_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_id` int NOT NULL,
  `product_article` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_order_product` (`order_id`,`product_article`),
  KEY `product_article` (`product_article`),
  KEY `idx_order_items_order` (`order_id`),
  CONSTRAINT `order_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE,
  CONSTRAINT `order_items_ibfk_2` FOREIGN KEY (`product_article`) REFERENCES `products` (`article`) ON DELETE RESTRICT,
  CONSTRAINT `order_items_chk_1` CHECK ((`quantity` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_items`
--

LOCK TABLES `order_items` WRITE;
/*!40000 ALTER TABLE `order_items` DISABLE KEYS */;
INSERT INTO `order_items` VALUES (1,1,'А112Т4',2),(2,1,'G843H5',2),(3,2,'G843H5',1),(4,2,'А112Т4',1),(5,3,'D325D4',10),(6,3,'S432T5',10),(7,4,'F325D4',5),(8,4,'D325D4',4),(9,5,'G432G6',20),(10,5,'H542F5',20),(11,6,'А112Т4',2),(12,6,'G843H5',2),(13,7,'C346F5',3),(14,7,'F256G6',3),(15,8,'F325D4',1),(16,8,'G432G6',1),(17,9,'J532V5',5),(18,9,'F256G6',1),(19,10,'F256G6',5),(20,10,'J532V5',5);
/*!40000 ALTER TABLE `order_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Номер заказа',
  `order_date` date NOT NULL,
  `delivery_date` date DEFAULT NULL,
  `pickup_point_id` int NOT NULL,
  `user_id` int NOT NULL COMMENT 'Авторизированный клиент',
  `pickup_code` int NOT NULL COMMENT 'Код для получения',
  `status` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'Новый',
  PRIMARY KEY (`id`),
  KEY `pickup_point_id` (`pickup_point_id`),
  KEY `user_id` (`user_id`),
  KEY `idx_orders_status` (`status`),
  KEY `idx_orders_date` (`order_date`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`pickup_point_id`) REFERENCES `pickup_points` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'2024-02-27','2024-04-20',1,10,901,'Завершен'),(2,'2023-09-28','2024-04-21',11,7,902,'Завершен'),(3,'2024-03-21','2024-04-22',2,8,903,'Завершен'),(4,'2024-02-20','2024-04-23',11,9,904,'Завершен'),(5,'2024-03-17','2024-04-24',2,10,905,'Завершен'),(6,'2024-03-01','2024-04-25',15,7,906,'Завершен'),(7,'2024-02-29','2024-04-26',3,8,907,'Завершен'),(8,'2024-03-31','2024-04-27',19,9,908,'Новый'),(9,'2024-04-02','2024-04-28',5,10,909,'Новый'),(10,'2024-04-03','2024-04-29',19,10,910,'Новый');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pickup_points`
--

DROP TABLE IF EXISTS `pickup_points`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pickup_points` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `address` (`address`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pickup_points`
--

LOCK TABLES `pickup_points` WRITE;
/*!40000 ALTER TABLE `pickup_points` DISABLE KEYS */;
INSERT INTO `pickup_points` VALUES (2,'125061, г. Лесной, ул. Подгорная, 8'),(29,'125703, г. Лесной, ул. Партизанская, 49'),(28,'125837, г. Лесной, ул. Шоссейная, 40'),(36,'190949, г. Лесной, ул. Мичурина, 26'),(24,'344288, г. Лесной, ул. Чехова, 1'),(16,'394060, г.Лесной, ул. Фрунзе, 43'),(26,'394242, г. Лесной, ул. Коммунистическая, 43'),(21,'394782, г. Лесной, ул. Чехова, 3'),(4,'400562, г. Лесной, ул. Зеленая, 32'),(11,'410172, г. Лесной, ул. Северная, 13'),(6,'410542, г. Лесной, ул. Светлая, 46'),(17,'410661, г. Лесной, ул. Школьная, 50'),(1,'420151, г. Лесной, ул. Вишневая, 32'),(32,'426030, г. Лесной, ул. Маяковского, 44'),(8,'443890, г. Лесной, ул. Коммунистическая, 1'),(33,'450375, г. Лесной ул. Клубная, 44'),(23,'450558, г. Лесной, ул. Набережная, 30'),(20,'450983, г.Лесной, ул. Комсомольская, 26'),(13,'454311, г.Лесной, ул. Новая, 19'),(22,'603002, г. Лесной, ул. Дзержинского, 28'),(15,'603036, г. Лесной, ул. Садовая, 4'),(9,'603379, г. Лесной, ул. Спортивная, 46'),(10,'603721, г. Лесной, ул. Гоголя, 41'),(25,'614164, г.Лесной,  ул. Степная, 30'),(5,'614510, г. Лесной, ул. Маяковского, 47'),(12,'614611, г. Лесной, ул. Молодежная, 50'),(31,'614753, г. Лесной, ул. Полевая, 35'),(7,'620839, г. Лесной, ул. Цветочная, 8'),(30,'625283, г. Лесной, ул. Победы, 46'),(34,'625560, г. Лесной, ул. Некрасова, 12'),(18,'625590, г. Лесной, ул. Коммунистическая, 20'),(19,'625683, г. Лесной, ул. 8 Марта'),(35,'630201, г. Лесной, ул. Комсомольская, 17'),(3,'630370, г. Лесной, ул. Шоссейная, 24'),(14,'660007, г.Лесной, ул. Октябрьская, 19'),(27,'660540, г. Лесной, ул. Солнечная, 25');
/*!40000 ALTER TABLE `pickup_points` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `article` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Артикул товара',
  `name` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `unit` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'шт.',
  `price` decimal(10,2) NOT NULL,
  `supplier_id` int NOT NULL,
  `manufacturer_id` int NOT NULL,
  `category_id` int NOT NULL,
  `discount` decimal(5,1) NOT NULL DEFAULT '0.0',
  `quantity` int NOT NULL DEFAULT '0',
  `description` text COLLATE utf8mb4_unicode_ci,
  `photo` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Имя файла изображения',
  PRIMARY KEY (`article`),
  KEY `supplier_id` (`supplier_id`),
  KEY `manufacturer_id` (`manufacturer_id`),
  KEY `idx_products_category` (`category_id`),
  KEY `idx_products_price` (`price`),
  KEY `idx_products_discount` (`discount`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `products_ibfk_2` FOREIGN KEY (`manufacturer_id`) REFERENCES `manufacturers` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `products_ibfk_3` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `products_chk_1` CHECK ((`price` >= 0)),
  CONSTRAINT `products_chk_2` CHECK (((`discount` >= 0) and (`discount` <= 100))),
  CONSTRAINT `products_chk_3` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('B653G6','Русский язык: Первые шаги. Часть 3. Учебное пособие','шт.',2699.00,10,5,2,8.0,9,'Пособие является завершающей частью учебного комплекса. Третья часть содержит 10 уроков (21-30, последний-повторительный). Усвоение лексико-грамматического материала рассчитано примерно на 200-240 часов аудиторных занятий.','17.jpg'),('C346F5','Квантовые миры и возникновение пространства-времени','шт.',1349.00,15,8,1,5.0,4,'Шон Кэрролл — физик-теоретик и один из самых известных в мире популяризаторов науки — заставляет нас по-новому взглянуть на физику. Столкновение с главной загадкой квантовой механики полностью поменяет наши представления о пространстве и времени.','8.jpg'),('D325D4','Девайс','шт.',1599.00,9,9,4,5.0,12,'Молодой фрилансер Захар Скаро устраивается на очередную подработку. Задача, казалось бы, тривиальная: тестирование нового устройства. Вот только вопрос в том, тестированием какой реальности занимается этот новый Девайс?','3.jpg'),('F256G6','Вселенная. Происхождение жизни, смысл нашего существования и огромный космос','шт.',1799.00,15,8,1,6.0,2,'Знаменитый физик Шон Кэрролл в свойственной ему увлекательной манере объясняет принципы, которые лежат в основах научных революций от Дарвина до Эйнштейна, и показывает как невероятные научные открытия последнего столетия изменили наш мир.',NULL),('F325D4','Чук и Гек','шт.',209.00,1,9,4,18.0,3,'В книгу вошли повести и рассказы Аркадия Петровича Гайдара: \"Чук и Гек\", \"Горячий камень\" и \"Сказка о военной тайне, о Мальчише-Кибальчише и его твердом слове\"','5.jpg'),('G432G6','Информационная безопасность. Национальные стандарты Российской Федерации. 3-е издание. Учебное пособие','шт.',3899.00,16,8,1,22.0,3,'В учебном пособии рассмотрено более 300 действующих открытых документов национальной системы стандартизации Российской Федерации, включая международные и межгосударственные стандарты в области информационной безопасности по состоянию на начало 2023 года.','6.jpg'),('G543F5','Религиозные верования с древнейших времен до наших дней','шт.',879.00,5,1,3,4.0,6,'Настоящее издание представляет собой сборник переводов лекций по истории дохристианских и нехристианских религий, прочитанных в Лондоне в период с 1888 по 1891 гг. авторитетными исследователями данного раздела религиоведения.','16.jpg'),('G632H6','Формирование литературной репутации Н.Г.Чернышевского в ХIX-XXI веках','шт.',1349.00,5,7,3,2.0,8,'Монография Д. А. Щербакова - новаторская. Поэтапно рассмотрены не только многочисленные суждения известных отечественных и зарубежных критиков, литературоведов, философов и политиков, различным образом характеризовавших Н. Г. Чернышевского в связи и вне связи со знаменитым романом \"Что делать?','14.jpg'),('G643F4','Иосиф Бродский. Избранные эссе (комплект из 6-ти книг)','шт.',4925.00,8,6,3,2.0,24,'Шесть сборников избранных эссе Иосифа Бродского (1940-1996), великого поэта, драматурга, мыслителя, лауреата Нобелевской премии по литературе (1987): «Будущее или далекое прошлое», «Верь своей боли», «Как читать книгу», «О русской литературе», «О тирании», «Путеводитель по переименованному городу». Все тексты представлены на английском языке и в переводе на русский и открывают автора не только как поэта, но как историка, критика, и глубокого и ироничного мыслителя.','11.jpg'),('G843H5','Тайны и загадки отца БраунаТайны и загадки отца Брауна','шт.',193.00,3,10,4,30.0,9,'Гилберт Кит Честертон — признанный классик английской литературы, один из самых ярких писателей первой половины XX века. Классикой стали его романы и многочисленные эссе, однако любовь массового читателя принесли ему рассказы об отце Брауне, тихом, застенчивом священнике, мастерски раскрывающем наиболее запутанные загадки и преступления.','2.jpg'),('H436H7','Английский язык в спорте: Учебное пособие','шт.',1999.00,7,2,2,2.0,0,'Учебное пособие подготовлено для слушателей, изу чающих английский язык как язык специальности','19.jpg'),('H475R5','Лексика и грамматика современного китайского языка (к тому II учебника «Новый практический курс китайского языка» под редакцией Лю Сюня): учебное пособие','шт.',608.00,14,3,2,25.0,12,'Пособие выступает дополнением ко второму тому учебника «Новый практический курс китайского языка» (под редакцией Лю Сюня).','20.jpg'),('H542F5','Linux. Командная строка. Лучшие практики','шт.',1799.00,6,8,1,4.0,5,'Перейдите на новый уровень работы в Linux! Если вы системный администратор, разработчик программного обеспечения, SRE-инженер или пользователь Linux, книга поможет вам работать быстрее, элегантнее и эффективнее.','7.jpg'),('J326V5','Тысячелетие императорской керамикиv','шт.',2599.00,18,6,3,5.0,4,'Фарфор стал величайшим символом китайской культуры. Это одно из выдающихся изобретений, внесших неоценимый вклад в мировую цивилизацию.','12.jpg'),('J532V5','Пушкин. Бродский. Империя и судьба. В 2-х томах (комплект из 2-х книг)','шт.',529.00,17,4,3,8.0,6,'Первая книга двухтомника «Пушкин. Бродский. Империя и судьба» пронизана пушкинской темой. Пушкин — «певец империи и свободы» — присутствует даже там, где он впрямую не упоминается, ибо его судьба, как и судьба других героев книги, органично связана с трагедией великой империи.','10.jpg'),('J632F6','Вечные спутники: Портреты из всемирной литературы','шт.',1599.00,4,6,3,0.0,6,'Книга \"Вечные спутники\" - это цикл критических очерков о культуре и великих литераторах, сопровождавших жизнь и творчество русского писателя, поэта, литературного критика и общественного деятеля Дмитрия Мережковского (1865–1941).','13.jpg'),('J735J7','Синтетический образ индивидуального психического мира','шт.',1099.00,13,5,3,9.0,4,'Психика подобна определенным объектам, это фиксируют сами люди в языке и искусстве. В данном исследовании рассматриваются в этом плане образы сосуда, воронки, дерева и крепости.','18.jpg'),('M642E5','Теория искусства. Краткий путеводитель','шт.',879.00,12,7,3,3.0,2,NULL,'15.jpg'),('S432T5','Необыкновенное обыкновенное чудо. Школьные истории','шт.',549.00,11,9,4,15.0,15,NULL,'4.jpg'),('А112Т4','Прокляты и убиты','шт.',585.00,2,10,4,25.0,6,'Роман-эпопею \"Прокляты и убиты\" Виктора Астафьева по праву считают одним из самых сильных и пронзительных произведений отечественной военной прозы.','1.jpg');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES (1,'Аркадий Гайдар'),(2,'Виктор Астафьев'),(3,'Гилберт Кит Честертон'),(4,'Дмитрий Мережковский'),(5,'Дмитрий Щербаков'),(6,'Дэниел Джей Барретт'),(7,'Екатерина Габарта, Ирина Игнатьева'),(8,'Иосиф Бродский'),(9,'Кирилл Каланджи'),(10,'Любовь Беликова, Инна Ерофеева, Татьяна Шутова'),(11,'Людмила Улицкая'),(12,'Роджер Осборн, Дэн Стерджис'),(13,'Сергей Моргачев'),(14,'Татьяна Лопаткина, Софья Маннапова'),(15,'Шон Кэрролл'),(16,'Юрий Родичев'),(17,'Яков Гордин'),(18,'Янь Чуннянь Янь Чуннянь');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `role` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Администратор / Менеджер / Авторизированный клиент',
  `full_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `login` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login` (`login`),
  KEY `idx_users_role` (`role`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Администратор','Никифорова Анна Семеновна','94d5ous@gmail.com','uzWC67'),(2,'Администратор','Стелина Евгения Петровна','uth4iz@mail.com','2L6KZG'),(3,'Администратор','Михайлюк Анна Вячеславовна','5d4zbu@tutanota.com','rwVDh9'),(4,'Менеджер','Ситдикова Елена Анатольевна','ptec8ym@yahoo.com','LdNyos'),(5,'Менеджер','Ворсин Петр Евгеньевич','1qz4kw@mail.com','gynQMT'),(6,'Менеджер','Старикова Елена Павловна','4np6se@mail.com','AtnDjr'),(7,'Авторизированный клиент','Никифорова Весения Николаевна','yzls62@outlook.com','JlFRCZ'),(8,'Авторизированный клиент','Сазонов Руслан Германович','1diph5e@tutanota.com','8ntwUp'),(9,'Авторизированный клиент','Одинцов Серафим Артёмович','tjde7c@yahoo.com','YOyhfR'),(10,'Авторизированный клиент','Степанов Михаил Артёмович','wpmrc3do@tutanota.com','RSbvHv');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-05 15:41:06
