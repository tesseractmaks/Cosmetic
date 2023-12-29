import random

values_data = [
    {
        "title": "Dolce &amp; Gabbana Light Blue",
        "price": random.randint(600, 2710),
        "image": "../uploads/posts/2021-05/1621438635_product-961805-0-productpagedesktop.jpg",
        "label": random.choice(["new", "", ""]),
        "link_detail": "26-shorty-triplex-red.html",
        "num_goods": "goods_26",
        "data_goods": "26|Dolce & Gabbana Light Blue|1772,25|-|http://raro.prowebmarket.ru/ptoduct/26-shorty-triplex-red.html|"
    },
    {
        "image": "../uploads/posts/2021-05/1621240233_1.jpg",
        "link_detail": "25-shorty-bolero-black.html",
        "title": "Payot Masque Radiance Mask",
        "price": random.randint(600, 2710),
        "label": random.choice(["new", "", ""]),
        "num_goods": "goods_25",
        "data_goods": "25|Payot Masque Radiance Mask|1400|-|http://raro.prowebmarket.ru/ptoduct/25-shorty-bolero-black.html|"

    },
    {
        "link_detail": "24-shorty-robins.html",
        "image": "../uploads/posts/2021-05/1621439399_product-946023-0-productpagedesktop.jpg",
        "title": "Gel Effect Nail",
        "price": random.randint(600, 2710),
        "label": random.choice(["new", "", ""]),
        "num_goods": "goods_24",
        "data_goods": "24|Gel Effect Nail|250|-|http://raro.prowebmarket.ru/ptoduct/24-shorty-robins.html|"
    },
    {
        "link_detail": "22-futbolka-eazyway-sports.html",
        "image": "../uploads/posts/2021-05/1621440271_product-959928-0-productpagedesktop.jpg",
        "title": "Ultra Wear Stick",
        "price": random.randint(600, 2710),
        "label": random.choice(["new", "", ""]),
        "num_goods": "goods_22",
        "data_goods": "22| Ultra Wear Stick |3430|-|http://raro.prowebmarket.ru/ptoduct/22-futbolka-eazyway-sports.html|"
    },
    {
        "link_detail": "23-futbolka-fitness-purple.html",
        "image": "../uploads/posts/2021-05/1621440923_product-941847-0-productpagedesktop.jpg",
        "title": "Essence Blush Lighter",
        "price": random.randint(600, 2710),
        "label": random.choice(["new", "", ""]),
        "num_goods": "goods_23",
        "data_goods": "23|Essence Blush Lighter |300|-|http://raro.prowebmarket.ru/ptoduct/23-futbolka-fitness-purple.html|"
    },
    {
        "link_detail": "21-futbolka-basic-pro.html",
        "image": "../uploads/posts/2021-05/1621441502_product-937989-0-productpagedesktop.jpg",
        "title": "Note Luminous Silk",
        "price": random.randint(600, 2710),
        "label": random.choice(["new", ""]),
        "num_goods": "goods_21",
        "data_goods": "21|Note Luminous Silk|600|-|http://raro.prowebmarket.ru/ptoduct/21-futbolka-basic-pro.html|"
    },
    {
        "title": "Dolce &amp; Gabbana Light Blue",
        "price": random.randint(600, 2710),
        "image": "../uploads/posts/2021-05/1621438635_product-961805-0-productpagedesktop.jpg",
        "label": random.choice(["new", "", ""]),
        "link_detail": "26-shorty-triplex-red.html",
        "num_goods": "goods_26",
        "data_goods": "26|Dolce & Gabbana Light Blue|1772,25|-|http://raro.prowebmarket.ru/ptoduct/26-shorty-triplex-red.html|"
    },
    {
        "image": "../uploads/posts/2021-05/1621240233_1.jpg",
        "link_detail": "25-shorty-bolero-black.html",
        "title": "Payot Masque Radiance Mask",
        "price": random.randint(600, 2710),
        "label": random.choice(["new", "", ""]),
        "num_goods": "goods_25",
        "data_goods": "25|Payot Masque Radiance Mask|1400|-|http://raro.prowebmarket.ru/ptoduct/25-shorty-bolero-black.html|"

    },
    {
        "link_detail": "24-shorty-robins.html",
        "image": "../uploads/posts/2021-05/1621439399_product-946023-0-productpagedesktop.jpg",
        "title": "Gel Effect Nail",
        "price": random.randint(600, 2710),
        "label": random.choice(["new", "", ""]),
        "num_goods": "goods_24",
        "data_goods": "24|Gel Effect Nail|250|-|http://raro.prowebmarket.ru/ptoduct/24-shorty-robins.html|"
    },
    {
        "link_detail": "22-futbolka-eazyway-sports.html",
        "image": "../uploads/posts/2021-05/1621440271_product-959928-0-productpagedesktop.jpg",
        "title": "Ultra Wear Stick",
        "price": random.randint(600, 2710),
        "label": random.choice(["new", "", ""]),
        "num_goods": "goods_22",
        "data_goods": "22| Ultra Wear Stick |3430|-|http://raro.prowebmarket.ru/ptoduct/22-futbolka-eazyway-sports.html|"
    },
    {
        "link_detail": "23-futbolka-fitness-purple.html",
        "image": "../uploads/posts/2021-05/1621440923_product-941847-0-productpagedesktop.jpg",
        "title": "Essence Blush Lighter",
        "price": random.randint(600, 2710),
        "label": random.choice(["new", "", ""]),
        "num_goods": "goods_23",
        "data_goods": "23|Essence Blush Lighter |300|-|http://raro.prowebmarket.ru/ptoduct/23-futbolka-fitness-purple.html|"
    },
    {
        "link_detail": "21-futbolka-basic-pro.html",
        "image": "../uploads/posts/2021-05/1621441502_product-937989-0-productpagedesktop.jpg",
        "title": "Note Luminous Silk",
        "price": random.randint(600, 2710),
        "label": random.choice(["new", ""]),
        "num_goods": "goods_21",
        "data_goods": "21|Note Luminous Silk|600|-|http://raro.prowebmarket.ru/ptoduct/21-futbolka-basic-pro.html|"
    },
    {
        "link_detail": "20-leggins-correct.html",
        "image": "../uploads/posts/2021-05/1621442542_-normal-960132-big-8809500811015_jpg-productpagedesktop.jpg",
        "title": "La&#039;dor Keratin LPP Shampoo",
        "price": random.randint(600, 2710),
        "label": random.choice(["new", ""]),
        "num_goods": "goods_20",
        "data_goods": "20||270|-|http://raro.prowebmarket.ru/ptoduct/20-leggins-correct.html|"
    },
    {
        "link_detail": "19-top-bra-eazyway.html",
        "image": "../uploads/posts/2021-05/1621442996_product-917382-1-productpagedesktop.jpg",
        "title": "Bourjois Volume Glamour",
        "price": random.randint(600, 2710),
        "label": random.choice(["new", ""]),
        "num_goods": "goods_19",
        "data_goods": "19|Bourjois Volume Glamour|300|-|http://raro.prowebmarket.ru/ptoduct/19-top-bra-eazyway.html|"
    },
    {
        "link_detail": "17-kombinezon-bona-fide.html",
        "image": "../uploads/posts/2021-05/1621247418_2.jpg",
        "title": "Ginseng Milk and Tonic Duo",
        "price": random.randint(600, 2710),
        "label": random.choice(["new", ""]),
        "num_goods": "goods_17",
        "data_goods": "17|Ginseng Milk and Tonic Duo|2400|-|http://raro.prowebmarket.ru/ptoduct/17-kombinezon-bona-fide.html|"
    },
]
