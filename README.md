# Nedir?
HX_Envoy, bir web sitesindeki RSS bilgilerinden yararlanarak içerik kontrolü sağlayan ve içerikteki güncellemeleri Telegram botu ile mesaj olarak gönderen cronejob ile uyumlu, küçük ve işlevsel bir programdır.

Program, İçerik kontrolünü `parse` edilmiş içeriğin(RSS Feed) `entry_id` değerinea göre yapar. Bu id adreslerini `last_entry_ids.txt` dosyasında saklar. Bu sayede cronjob ile program belirli bir süre sonra tekrar çaştırıldığında `last_entry_ids.txt` deki id değerleri ile web sitesine yeni eklenen içeriklerin id değerlerini karşılaştırmış olur. Karşılaştırma sonucunda `.txt` dosyasındaki id değeri ile web sitesindeki `feed_url` in `entry_id` değeri aynı olursa o `feed_url` i geçer , farklı olursa da telegram botu aracılığıyla yeni içeriğin eklendiğine dair bir mesaj gönderir.

