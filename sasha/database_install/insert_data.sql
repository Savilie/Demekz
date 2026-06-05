USE chitaigorod;
SET NAMES utf8mb4;
START TRANSACTION;

-- Suppliers
INSERT INTO suppliers (name) VALUES ('Аркадий Гайдар');
INSERT INTO suppliers (name) VALUES ('Виктор Астафьев');
INSERT INTO suppliers (name) VALUES ('Гилберт Кит Честертон');
INSERT INTO suppliers (name) VALUES ('Дмитрий Мережковский');
INSERT INTO suppliers (name) VALUES ('Дмитрий Щербаков');
INSERT INTO suppliers (name) VALUES ('Дэниел Джей Барретт');
INSERT INTO suppliers (name) VALUES ('Екатерина Габарта, Ирина Игнатьева');
INSERT INTO suppliers (name) VALUES ('Иосиф Бродский');
INSERT INTO suppliers (name) VALUES ('Кирилл Каланджи');
INSERT INTO suppliers (name) VALUES ('Любовь Беликова, Инна Ерофеева, Татьяна Шутова');
INSERT INTO suppliers (name) VALUES ('Людмила Улицкая');
INSERT INTO suppliers (name) VALUES ('Роджер Осборн, Дэн Стерджис');
INSERT INTO suppliers (name) VALUES ('Сергей Моргачев');
INSERT INTO suppliers (name) VALUES ('Татьяна Лопаткина, Софья Маннапова');
INSERT INTO suppliers (name) VALUES ('Шон Кэрролл');
INSERT INTO suppliers (name) VALUES ('Юрий Родичев');
INSERT INTO suppliers (name) VALUES ('Яков Гордин');
INSERT INTO suppliers (name) VALUES ('Янь Чуннянь Янь Чуннянь');

-- Manufacturers
INSERT INTO manufacturers (name) VALUES ('Амрита-Русь');
INSERT INTO manufacturers (name) VALUES ('Аспект Пресс');
INSERT INTO manufacturers (name) VALUES ('ВКН');
INSERT INTO manufacturers (name) VALUES ('Время');
INSERT INTO manufacturers (name) VALUES ('Златоуст');
INSERT INTO manufacturers (name) VALUES ('Лениздат');
INSERT INTO manufacturers (name) VALUES ('Неолит');
INSERT INTO manufacturers (name) VALUES ('Прогресс книга');
INSERT INTO manufacturers (name) VALUES ('Т8 Издательские технологии');
INSERT INTO manufacturers (name) VALUES ('Яуза');

-- Categories
INSERT INTO categories (name) VALUES ('Учебник для вузов');
INSERT INTO categories (name) VALUES ('Учебное пособие');
INSERT INTO categories (name) VALUES ('Хрестоматия');
INSERT INTO categories (name) VALUES ('Художественная литература');

-- Users
INSERT INTO users (role, full_name, login, password) VALUES ('Администратор', 'Никифорова Анна Семеновна', '94d5ous@gmail.com', 'uzWC67');
INSERT INTO users (role, full_name, login, password) VALUES ('Администратор', 'Стелина Евгения Петровна', 'uth4iz@mail.com', '2L6KZG');
INSERT INTO users (role, full_name, login, password) VALUES ('Администратор', 'Михайлюк Анна Вячеславовна', '5d4zbu@tutanota.com', 'rwVDh9');
INSERT INTO users (role, full_name, login, password) VALUES ('Менеджер', 'Ситдикова Елена Анатольевна', 'ptec8ym@yahoo.com', 'LdNyos');
INSERT INTO users (role, full_name, login, password) VALUES ('Менеджер', 'Ворсин Петр Евгеньевич', '1qz4kw@mail.com', 'gynQMT');
INSERT INTO users (role, full_name, login, password) VALUES ('Менеджер', 'Старикова Елена Павловна', '4np6se@mail.com', 'AtnDjr');
INSERT INTO users (role, full_name, login, password) VALUES ('Авторизированный клиент', 'Никифорова Весения Николаевна', 'yzls62@outlook.com', 'JlFRCZ');
INSERT INTO users (role, full_name, login, password) VALUES ('Авторизированный клиент', 'Сазонов Руслан Германович', '1diph5e@tutanota.com', '8ntwUp');
INSERT INTO users (role, full_name, login, password) VALUES ('Авторизированный клиент', 'Одинцов Серафим Артёмович', 'tjde7c@yahoo.com', 'YOyhfR');
INSERT INTO users (role, full_name, login, password) VALUES ('Авторизированный клиент', 'Степанов Михаил Артёмович', 'wpmrc3do@tutanota.com', 'RSbvHv');

-- Pickup Points
INSERT INTO pickup_points (address) VALUES ('420151, г. Лесной, ул. Вишневая, 32');
INSERT INTO pickup_points (address) VALUES ('125061, г. Лесной, ул. Подгорная, 8');
INSERT INTO pickup_points (address) VALUES ('630370, г. Лесной, ул. Шоссейная, 24');
INSERT INTO pickup_points (address) VALUES ('400562, г. Лесной, ул. Зеленая, 32');
INSERT INTO pickup_points (address) VALUES ('614510, г. Лесной, ул. Маяковского, 47');
INSERT INTO pickup_points (address) VALUES ('410542, г. Лесной, ул. Светлая, 46');
INSERT INTO pickup_points (address) VALUES ('620839, г. Лесной, ул. Цветочная, 8');
INSERT INTO pickup_points (address) VALUES ('443890, г. Лесной, ул. Коммунистическая, 1');
INSERT INTO pickup_points (address) VALUES ('603379, г. Лесной, ул. Спортивная, 46');
INSERT INTO pickup_points (address) VALUES ('603721, г. Лесной, ул. Гоголя, 41');
INSERT INTO pickup_points (address) VALUES ('410172, г. Лесной, ул. Северная, 13');
INSERT INTO pickup_points (address) VALUES ('614611, г. Лесной, ул. Молодежная, 50');
INSERT INTO pickup_points (address) VALUES ('454311, г.Лесной, ул. Новая, 19');
INSERT INTO pickup_points (address) VALUES ('660007, г.Лесной, ул. Октябрьская, 19');
INSERT INTO pickup_points (address) VALUES ('603036, г. Лесной, ул. Садовая, 4');
INSERT INTO pickup_points (address) VALUES ('394060, г.Лесной, ул. Фрунзе, 43');
INSERT INTO pickup_points (address) VALUES ('410661, г. Лесной, ул. Школьная, 50');
INSERT INTO pickup_points (address) VALUES ('625590, г. Лесной, ул. Коммунистическая, 20');
INSERT INTO pickup_points (address) VALUES ('625683, г. Лесной, ул. 8 Марта');
INSERT INTO pickup_points (address) VALUES ('450983, г.Лесной, ул. Комсомольская, 26');
INSERT INTO pickup_points (address) VALUES ('394782, г. Лесной, ул. Чехова, 3');
INSERT INTO pickup_points (address) VALUES ('603002, г. Лесной, ул. Дзержинского, 28');
INSERT INTO pickup_points (address) VALUES ('450558, г. Лесной, ул. Набережная, 30');
INSERT INTO pickup_points (address) VALUES ('344288, г. Лесной, ул. Чехова, 1');
INSERT INTO pickup_points (address) VALUES ('614164, г.Лесной,  ул. Степная, 30');
INSERT INTO pickup_points (address) VALUES ('394242, г. Лесной, ул. Коммунистическая, 43');
INSERT INTO pickup_points (address) VALUES ('660540, г. Лесной, ул. Солнечная, 25');
INSERT INTO pickup_points (address) VALUES ('125837, г. Лесной, ул. Шоссейная, 40');
INSERT INTO pickup_points (address) VALUES ('125703, г. Лесной, ул. Партизанская, 49');
INSERT INTO pickup_points (address) VALUES ('625283, г. Лесной, ул. Победы, 46');
INSERT INTO pickup_points (address) VALUES ('614753, г. Лесной, ул. Полевая, 35');
INSERT INTO pickup_points (address) VALUES ('426030, г. Лесной, ул. Маяковского, 44');
INSERT INTO pickup_points (address) VALUES ('450375, г. Лесной ул. Клубная, 44');
INSERT INTO pickup_points (address) VALUES ('625560, г. Лесной, ул. Некрасова, 12');
INSERT INTO pickup_points (address) VALUES ('630201, г. Лесной, ул. Комсомольская, 17');
INSERT INTO pickup_points (address) VALUES ('190949, г. Лесной, ул. Мичурина, 26');

-- Products
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'А112Т4', 'Прокляты и убиты', 'шт.', 585.00, (SELECT id FROM suppliers WHERE name = 'Виктор Астафьев'), (SELECT id FROM manufacturers WHERE name = 'Яуза'), (SELECT id FROM categories WHERE name = 'Художественная литература'), 25.0, 6, 'Роман-эпопею "Прокляты и убиты" Виктора Астафьева по праву считают одним из самых сильных и пронзительных произведений отечественной военной прозы.', '1.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'G843H5', 'Тайны и загадки отца БраунаТайны и загадки отца Брауна', 'шт.', 193.00, (SELECT id FROM suppliers WHERE name = 'Гилберт Кит Честертон'), (SELECT id FROM manufacturers WHERE name = 'Яуза'), (SELECT id FROM categories WHERE name = 'Художественная литература'), 30.0, 9, 'Гилберт Кит Честертон — признанный классик английской литературы, один из самых ярких писателей первой половины XX века. Классикой стали его романы и многочисленные эссе, однако любовь массового читателя принесли ему рассказы об отце Брауне, тихом, застенчивом священнике, мастерски раскрывающем наиболее запутанные загадки и преступления.', '2.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'D325D4', 'Девайс', 'шт.', 1599.00, (SELECT id FROM suppliers WHERE name = 'Кирилл Каланджи'), (SELECT id FROM manufacturers WHERE name = 'Т8 Издательские технологии'), (SELECT id FROM categories WHERE name = 'Художественная литература'), 5.0, 12, 'Молодой фрилансер Захар Скаро устраивается на очередную подработку. Задача, казалось бы, тривиальная: тестирование нового устройства. Вот только вопрос в том, тестированием какой реальности занимается этот новый Девайс?', '3.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'S432T5', 'Необыкновенное обыкновенное чудо. Школьные истории', 'шт.', 549.00, (SELECT id FROM suppliers WHERE name = 'Людмила Улицкая'), (SELECT id FROM manufacturers WHERE name = 'Т8 Издательские технологии'), (SELECT id FROM categories WHERE name = 'Художественная литература'), 15.0, 15, NULL, '4.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'F325D4', 'Чук и Гек', 'шт.', 209.00, (SELECT id FROM suppliers WHERE name = 'Аркадий Гайдар'), (SELECT id FROM manufacturers WHERE name = 'Т8 Издательские технологии'), (SELECT id FROM categories WHERE name = 'Художественная литература'), 18.0, 3, 'В книгу вошли повести и рассказы Аркадия Петровича Гайдара: "Чук и Гек", "Горячий камень" и "Сказка о военной тайне, о Мальчише-Кибальчише и его твердом слове"', '5.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'G432G6', 'Информационная безопасность. Национальные стандарты Российской Федерации. 3-е издание. Учебное пособие', 'шт.', 3899.00, (SELECT id FROM suppliers WHERE name = 'Юрий Родичев'), (SELECT id FROM manufacturers WHERE name = 'Прогресс книга'), (SELECT id FROM categories WHERE name = 'Учебник для вузов'), 22.0, 3, 'В учебном пособии рассмотрено более 300 действующих открытых документов национальной системы стандартизации Российской Федерации, включая международные и межгосударственные стандарты в области информационной безопасности по состоянию на начало 2023 года.', '6.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'H542F5', 'Linux. Командная строка. Лучшие практики', 'шт.', 1799.00, (SELECT id FROM suppliers WHERE name = 'Дэниел Джей Барретт'), (SELECT id FROM manufacturers WHERE name = 'Прогресс книга'), (SELECT id FROM categories WHERE name = 'Учебник для вузов'), 4.0, 5, 'Перейдите на новый уровень работы в Linux! Если вы системный администратор, разработчик программного обеспечения, SRE-инженер или пользователь Linux, книга поможет вам работать быстрее, элегантнее и эффективнее.', '7.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'C346F5', 'Квантовые миры и возникновение пространства-времени', 'шт.', 1349.00, (SELECT id FROM suppliers WHERE name = 'Шон Кэрролл'), (SELECT id FROM manufacturers WHERE name = 'Прогресс книга'), (SELECT id FROM categories WHERE name = 'Учебник для вузов'), 5.0, 4, 'Шон Кэрролл — физик-теоретик и один из самых известных в мире популяризаторов науки — заставляет нас по-новому взглянуть на физику. Столкновение с главной загадкой квантовой механики полностью поменяет наши представления о пространстве и времени.', '8.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'F256G6', 'Вселенная. Происхождение жизни, смысл нашего существования и огромный космос', 'шт.', 1799.00, (SELECT id FROM suppliers WHERE name = 'Шон Кэрролл'), (SELECT id FROM manufacturers WHERE name = 'Прогресс книга'), (SELECT id FROM categories WHERE name = 'Учебник для вузов'), 6.0, 2, 'Знаменитый физик Шон Кэрролл в свойственной ему увлекательной манере объясняет принципы, которые лежат в основах научных революций от Дарвина до Эйнштейна, и показывает как невероятные научные открытия последнего столетия изменили наш мир.', NULL;
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'J532V5', 'Пушкин. Бродский. Империя и судьба. В 2-х томах (комплект из 2-х книг)', 'шт.', 529.00, (SELECT id FROM suppliers WHERE name = 'Яков Гордин'), (SELECT id FROM manufacturers WHERE name = 'Время'), (SELECT id FROM categories WHERE name = 'Хрестоматия'), 8.0, 6, 'Первая книга двухтомника «Пушкин. Бродский. Империя и судьба» пронизана пушкинской темой. Пушкин — «певец империи и свободы» — присутствует даже там, где он впрямую не упоминается, ибо его судьба, как и судьба других героев книги, органично связана с трагедией великой империи.', '10.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'G643F4', 'Иосиф Бродский. Избранные эссе (комплект из 6-ти книг)', 'шт.', 4925.00, (SELECT id FROM suppliers WHERE name = 'Иосиф Бродский'), (SELECT id FROM manufacturers WHERE name = 'Лениздат'), (SELECT id FROM categories WHERE name = 'Хрестоматия'), 2.0, 24, 'Шесть сборников избранных эссе Иосифа Бродского (1940-1996), великого поэта, драматурга, мыслителя, лауреата Нобелевской премии по литературе (1987): «Будущее или далекое прошлое», «Верь своей боли», «Как читать книгу», «О русской литературе», «О тирании», «Путеводитель по переименованному городу». Все тексты представлены на английском языке и в переводе на русский и открывают автора не только как поэта, но как историка, критика, и глубокого и ироничного мыслителя.', '11.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'J326V5', 'Тысячелетие императорской керамикиv', 'шт.', 2599.00, (SELECT id FROM suppliers WHERE name = 'Янь Чуннянь Янь Чуннянь'), (SELECT id FROM manufacturers WHERE name = 'Лениздат'), (SELECT id FROM categories WHERE name = 'Хрестоматия'), 5.0, 4, 'Фарфор стал величайшим символом китайской культуры. Это одно из выдающихся изобретений, внесших неоценимый вклад в мировую цивилизацию.', '12.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'J632F6', 'Вечные спутники: Портреты из всемирной литературы', 'шт.', 1599.00, (SELECT id FROM suppliers WHERE name = 'Дмитрий Мережковский'), (SELECT id FROM manufacturers WHERE name = 'Лениздат'), (SELECT id FROM categories WHERE name = 'Хрестоматия'), 0.0, 6, 'Книга "Вечные спутники" - это цикл критических очерков о культуре и великих литераторах, сопровождавших жизнь и творчество русского писателя, поэта, литературного критика и общественного деятеля Дмитрия Мережковского (1865–1941).', '13.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'G632H6', 'Формирование литературной репутации Н.Г.Чернышевского в ХIX-XXI веках', 'шт.', 1349.00, (SELECT id FROM suppliers WHERE name = 'Дмитрий Щербаков'), (SELECT id FROM manufacturers WHERE name = 'Неолит'), (SELECT id FROM categories WHERE name = 'Хрестоматия'), 2.0, 8, 'Монография Д. А. Щербакова - новаторская. Поэтапно рассмотрены не только многочисленные суждения известных отечественных и зарубежных критиков, литературоведов, философов и политиков, различным образом характеризовавших Н. Г. Чернышевского в связи и вне связи со знаменитым романом "Что делать?', '14.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'M642E5', 'Теория искусства. Краткий путеводитель', 'шт.', 879.00, (SELECT id FROM suppliers WHERE name = 'Роджер Осборн, Дэн Стерджис'), (SELECT id FROM manufacturers WHERE name = 'Неолит'), (SELECT id FROM categories WHERE name = 'Хрестоматия'), 3.0, 2, NULL, '15.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'G543F5', 'Религиозные верования с древнейших времен до наших дней', 'шт.', 879.00, (SELECT id FROM suppliers WHERE name = 'Дмитрий Щербаков'), (SELECT id FROM manufacturers WHERE name = 'Амрита-Русь'), (SELECT id FROM categories WHERE name = 'Хрестоматия'), 4.0, 6, 'Настоящее издание представляет собой сборник переводов лекций по истории дохристианских и нехристианских религий, прочитанных в Лондоне в период с 1888 по 1891 гг. авторитетными исследователями данного раздела религиоведения.', '16.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'B653G6', 'Русский язык: Первые шаги. Часть 3. Учебное пособие', 'шт.', 2699.00, (SELECT id FROM suppliers WHERE name = 'Любовь Беликова, Инна Ерофеева, Татьяна Шутова'), (SELECT id FROM manufacturers WHERE name = 'Златоуст'), (SELECT id FROM categories WHERE name = 'Учебное пособие'), 8.0, 9, 'Пособие является завершающей частью учебного комплекса. Третья часть содержит 10 уроков (21-30, последний-повторительный). Усвоение лексико-грамматического материала рассчитано примерно на 200-240 часов аудиторных занятий.', '17.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'J735J7', 'Синтетический образ индивидуального психического мира', 'шт.', 1099.00, (SELECT id FROM suppliers WHERE name = 'Сергей Моргачев'), (SELECT id FROM manufacturers WHERE name = 'Златоуст'), (SELECT id FROM categories WHERE name = 'Хрестоматия'), 9.0, 4, 'Психика подобна определенным объектам, это фиксируют сами люди в языке и искусстве. В данном исследовании рассматриваются в этом плане образы сосуда, воронки, дерева и крепости.', '18.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'H436H7', 'Английский язык в спорте: Учебное пособие', 'шт.', 1999.00, (SELECT id FROM suppliers WHERE name = 'Екатерина Габарта, Ирина Игнатьева'), (SELECT id FROM manufacturers WHERE name = 'Аспект Пресс'), (SELECT id FROM categories WHERE name = 'Учебное пособие'), 2.0, 0, 'Учебное пособие подготовлено для слушателей, изу чающих английский язык как язык специальности', '19.jpg';
INSERT INTO products (article, name, unit, price, supplier_id, manufacturer_id, category_id, discount, quantity, description, photo) SELECT 'H475R5', 'Лексика и грамматика современного китайского языка (к тому II учебника «Новый практический курс китайского языка» под редакцией Лю Сюня): учебное пособие', 'шт.', 608.00, (SELECT id FROM suppliers WHERE name = 'Татьяна Лопаткина, Софья Маннапова'), (SELECT id FROM manufacturers WHERE name = 'ВКН'), (SELECT id FROM categories WHERE name = 'Учебное пособие'), 25.0, 12, 'Пособие выступает дополнением ко второму тому учебника «Новый практический курс китайского языка» (под редакцией Лю Сюня).', '20.jpg';

-- Orders + Order Items
INSERT INTO orders (id, order_date, delivery_date, pickup_point_id, user_id, pickup_code, status) SELECT 1, '2024-02-27', '2024-04-20', 1, (SELECT id FROM users WHERE full_name = 'Степанов Михаил Артёмович' LIMIT 1), 901, 'Завершен' WHERE NOT EXISTS (SELECT 1 FROM orders WHERE id = 1);
INSERT INTO order_items (order_id, product_article, quantity) SELECT 1, 'А112Т4', 2 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 1) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 1 AND product_article = 'А112Т4');
INSERT INTO order_items (order_id, product_article, quantity) SELECT 1, 'G843H5', 2 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 1) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 1 AND product_article = 'G843H5');
INSERT INTO orders (id, order_date, delivery_date, pickup_point_id, user_id, pickup_code, status) SELECT 2, '2023-09-28', '2024-04-21', 11, (SELECT id FROM users WHERE full_name = 'Никифорова Весения Николаевна' LIMIT 1), 902, 'Завершен' WHERE NOT EXISTS (SELECT 1 FROM orders WHERE id = 2);
INSERT INTO order_items (order_id, product_article, quantity) SELECT 2, 'G843H5', 1 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 2) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 2 AND product_article = 'G843H5');
INSERT INTO order_items (order_id, product_article, quantity) SELECT 2, 'А112Т4', 1 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 2) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 2 AND product_article = 'А112Т4');
INSERT INTO orders (id, order_date, delivery_date, pickup_point_id, user_id, pickup_code, status) SELECT 3, '2024-03-21', '2024-04-22', 2, (SELECT id FROM users WHERE full_name = 'Сазонов Руслан Германович' LIMIT 1), 903, 'Завершен' WHERE NOT EXISTS (SELECT 1 FROM orders WHERE id = 3);
INSERT INTO order_items (order_id, product_article, quantity) SELECT 3, 'D325D4', 10 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 3) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 3 AND product_article = 'D325D4');
INSERT INTO order_items (order_id, product_article, quantity) SELECT 3, 'S432T5', 10 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 3) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 3 AND product_article = 'S432T5');
INSERT INTO orders (id, order_date, delivery_date, pickup_point_id, user_id, pickup_code, status) SELECT 4, '2024-02-20', '2024-04-23', 11, (SELECT id FROM users WHERE full_name = 'Одинцов Серафим Артёмович' LIMIT 1), 904, 'Завершен' WHERE NOT EXISTS (SELECT 1 FROM orders WHERE id = 4);
INSERT INTO order_items (order_id, product_article, quantity) SELECT 4, 'F325D4', 5 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 4) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 4 AND product_article = 'F325D4');
INSERT INTO order_items (order_id, product_article, quantity) SELECT 4, 'D325D4', 4 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 4) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 4 AND product_article = 'D325D4');
INSERT INTO orders (id, order_date, delivery_date, pickup_point_id, user_id, pickup_code, status) SELECT 5, '2024-03-17', '2024-04-24', 2, (SELECT id FROM users WHERE full_name = 'Степанов Михаил Артёмович' LIMIT 1), 905, 'Завершен' WHERE NOT EXISTS (SELECT 1 FROM orders WHERE id = 5);
INSERT INTO order_items (order_id, product_article, quantity) SELECT 5, 'G432G6', 20 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 5) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 5 AND product_article = 'G432G6');
INSERT INTO order_items (order_id, product_article, quantity) SELECT 5, 'H542F5', 20 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 5) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 5 AND product_article = 'H542F5');
INSERT INTO orders (id, order_date, delivery_date, pickup_point_id, user_id, pickup_code, status) SELECT 6, '2024-03-01', '2024-04-25', 15, (SELECT id FROM users WHERE full_name = 'Никифорова Весения Николаевна' LIMIT 1), 906, 'Завершен' WHERE NOT EXISTS (SELECT 1 FROM orders WHERE id = 6);
INSERT INTO order_items (order_id, product_article, quantity) SELECT 6, 'А112Т4', 2 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 6) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 6 AND product_article = 'А112Т4');
INSERT INTO order_items (order_id, product_article, quantity) SELECT 6, 'G843H5', 2 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 6) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 6 AND product_article = 'G843H5');
INSERT INTO orders (id, order_date, delivery_date, pickup_point_id, user_id, pickup_code, status) SELECT 7, '2024-02-29', '2024-04-26', 3, (SELECT id FROM users WHERE full_name = 'Сазонов Руслан Германович' LIMIT 1), 907, 'Завершен' WHERE NOT EXISTS (SELECT 1 FROM orders WHERE id = 7);
INSERT INTO order_items (order_id, product_article, quantity) SELECT 7, 'C346F5', 3 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 7) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 7 AND product_article = 'C346F5');
INSERT INTO order_items (order_id, product_article, quantity) SELECT 7, 'F256G6', 3 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 7) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 7 AND product_article = 'F256G6');
INSERT INTO orders (id, order_date, delivery_date, pickup_point_id, user_id, pickup_code, status) SELECT 8, '2024-03-31', '2024-04-27', 19, (SELECT id FROM users WHERE full_name = 'Одинцов Серафим Артёмович' LIMIT 1), 908, 'Новый' WHERE NOT EXISTS (SELECT 1 FROM orders WHERE id = 8);
INSERT INTO order_items (order_id, product_article, quantity) SELECT 8, 'F325D4', 1 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 8) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 8 AND product_article = 'F325D4');
INSERT INTO order_items (order_id, product_article, quantity) SELECT 8, 'G432G6', 1 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 8) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 8 AND product_article = 'G432G6');
INSERT INTO orders (id, order_date, delivery_date, pickup_point_id, user_id, pickup_code, status) SELECT 9, '2024-04-02', '2024-04-28', 5, (SELECT id FROM users WHERE full_name = 'Степанов Михаил Артёмович' LIMIT 1), 909, 'Новый' WHERE NOT EXISTS (SELECT 1 FROM orders WHERE id = 9);
INSERT INTO order_items (order_id, product_article, quantity) SELECT 9, 'J532V5', 5 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 9) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 9 AND product_article = 'J532V5');
INSERT INTO order_items (order_id, product_article, quantity) SELECT 9, 'F256G6', 1 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 9) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 9 AND product_article = 'F256G6');
INSERT INTO orders (id, order_date, delivery_date, pickup_point_id, user_id, pickup_code, status) SELECT 10, '2024-04-03', '2024-04-29', 19, (SELECT id FROM users WHERE full_name = 'Степанов Михаил Артёмович' LIMIT 1), 910, 'Новый' WHERE NOT EXISTS (SELECT 1 FROM orders WHERE id = 10);
INSERT INTO order_items (order_id, product_article, quantity) SELECT 10, 'F256G6', 5 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 10) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 10 AND product_article = 'F256G6');
INSERT INTO order_items (order_id, product_article, quantity) SELECT 10, 'J532V5', 5 WHERE EXISTS (SELECT 1 FROM orders WHERE id = 10) AND NOT EXISTS (SELECT 1 FROM order_items WHERE order_id = 10 AND product_article = 'J532V5');

COMMIT;