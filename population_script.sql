INSERT INTO public.product_category (id, name, featured, parent_category_id) VALUES (5, 'Games', false, NULL);
INSERT INTO public.product_category (id, name, featured, parent_category_id) VALUES (6, 'Accessories', false, NULL);
INSERT INTO public.product_category (id, name, featured, parent_category_id) VALUES (7, 'Atari', false, 4);
INSERT INTO public.product_category (id, name, featured, parent_category_id) VALUES (9, 'Playstation 2', false, 4);
INSERT INTO public.product_category (id, name, featured, parent_category_id) VALUES (8, 'NES', false, 4);
INSERT INTO public.product_category (id, name, featured, parent_category_id) VALUES (10, 'Playstation 1', false, 4);
INSERT INTO public.product_category (id, name, featured, parent_category_id) VALUES (11, 'Playstation 1', false, 5);
INSERT INTO public.product_category (id, name, featured, parent_category_id) VALUES (12, 'Sega', false, 4);
INSERT INTO public.product_category (id, name, featured, parent_category_id) VALUES (4, 'Consoles', true, NULL);


INSERT INTO public.product_manufacturer VALUES (3, 'Sony', 'https://www.sony.net/top/2017/img/icon/top-og.jpg', '2020-05-13 16:18:19+00');
INSERT INTO public.product_manufacturer VALUES (4, 'Nintendo', 'https://cdn02.nintendo-europe.com/media/images/10_share_images/others_3/SI_GenericNintendo.jpg', '2020-05-13 16:19:20+00');
INSERT INTO public.product_manufacturer VALUES (5, 'Microsoft', 'https://1gew6o3qn6vx9kp3s42ge0y1-wpengine.netdna-ssl.com/wp-content/uploads/2012/08/8867.Microsoft_5F00_Logo_2D00_for_2D00_screen.jpg', '2020-05-13 16:20:06+00');
INSERT INTO public.product_manufacturer VALUES (6, 'Atari', 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Atari_logo.png', '2020-05-13 16:21:06+00');
INSERT INTO public.product_manufacturer VALUES (7, 'Sega', 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/SEGA_logo.svg/1280px-SEGA_logo.svg.png', '2020-05-13 16:22:32+00');


INSERT INTO public.product_product VALUES (6, 'Nintendo NES', 'The Nintendo Entertainment System (NES) is an 8-bit third-generation home video game console produced, released, and marketed by Nintendo. It is a remodelled export version of the companys Family Computer (FC) platform in Japan, commonly known as the Famicom, which was launched on July 15, 1983. The NES was launched in a test market of New York City on October 18, 1985, followed by Los Angeles as a second test market in February 1986, followed by Chicago and San Francisco, then other top 12 American markets, followed by a full launch across North America and some countries in Europe in September 1986, followed by Australia and other countries in Europe in 1987.', 5000,true, 8, 4);
INSERT INTO public.product_product VALUES (5, 'SEGA Mega Drive', 'The Sega Genesis, known as the Mega Drive outside North America, is a 16-bit fourth generation home video game console developed and sold by Sega. The Genesis is Segas third console and the successor to the Master System. Sega released it as the Mega Drive in Japan in 1988, and later as the Genesis in North America in 1989. In 1990, it was distributed as the Mega Drive by Virgin Mastertronic in Europe, Ozisoft in Australasia, and Tec Toy in Brazil. In South Korea, it was distributed by Samsung as the Super Gam*Boy and later the Super Aladdin Boy', 3000, true, 12, 7);
INSERT INTO public.product_product VALUES (3, 'Atari 2600', 'The Atari 2600, originally branded as the Atari Video Computer System or Atari VCS for short until November 1982, is a home video game console from Atari, Inc. Released on September 11, 1977, it is credited with popularizing the use of microprocessor-based hardware and games stored on ROM cartridges (a format first used with the Fairchild Channel F in 1976) instead of dedicated hardware with games physically built into the unit. The 2600 was bundled with two joystick controllers, a conjoined pair of paddle controllers, and a game cartridge: initially Combat, and later Pac-Man', 2000,true, 7, 6);
INSERT INTO public.product_product VALUES (7, 'Playstation 1', 'The PlayStation (officially abbreviated as PS and commonly known as the PS1 or its codename PSX) is a home video game console developed and marketed by Sony Computer Entertainment. It was first released on 3 December 1994 in Japan, on 9 September 1995 in North America, on 29 September 1995 in Europe, and on 15 November 1995 in Australia, and was the first of the PlayStation lineup of video game consoles. As a fifth generation console, the PlayStation primarily competed with the Nintendo 64 and the Sega Saturn.', 8000,true, 10, 3 );
INSERT INTO public.product_product VALUES (4, 'Playstation 2', 'he PlayStation 2 (officially branded as PS2) is a home video game console developed and marketed by Sony Computer Entertainment. It was first released in Japan on March 4, 2000, in North America on October 26, 2000, and in Europe and Australia on November 24, 2000, and is the successor to the original PlayStation, as well as the second installment in the PlayStation console line-up. A sixth-generation console, it competed with Segas Dreamcast, Nintendos GameCube, and Microsofts original Xbox.', 7000, true, 9, 3 );


INSERT INTO public.product_productimage VALUES (3, 'http://localhost:8000/static/img/atari_console.jpg', 3);
INSERT INTO public.product_productimage VALUES (4, 'http://localhost:8000/static/img/ps2_console.png', 4);
INSERT INTO public.product_productimage VALUES (5, 'http://localhost:8000/static/img/sega_console.png', 5);
INSERT INTO public.product_productimage VALUES (6, 'http://localhost:8000/static/img/nes_console.png', 6);
INSERT INTO public.product_productimage VALUES (7, 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/PSX-Console-wController.jpg/800px-PSX-Console-wController.jpg', 7);


INSERT INTO public.product_promo VALUES (2, 'http://localhost:8000/static/img/ps2.jpg', true, 4);
INSERT INTO public.product_promo VALUES (3, 'http://localhost:8000/static/img/nes.jpg', true, 6);