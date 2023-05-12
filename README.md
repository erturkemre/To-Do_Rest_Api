# To-Do_Rest_Api
TO-DO App

Bu uygulama, kullanıcıların kendilerine "yapılacaklar" listesi oluşturabileceği ve bu listeye adımlar ekleyebileceği bir to-do uygulamasıdır. Kullanıcılar, adımları tamamlayarak listelerini tamamlamaya çalışır.
Kullanıcılar

Uygulamada iki tür kullanıcı vardır. Kullanıcılar ön tanımlıdır ve kullanıcı oluşturma özelliği yoktur. Birinci tip kullanıcılar sadece kendi verileri üzerinde işlem yapabilirken, ikinci tip kullanıcılar tüm kullanıcıların listelerini görebilir.
Veri Saklama

Projenin dış bir veritabanına bağlanması gerekmemektedir. Veri saklama ve değiştirme işlemleri için Mock Servisler kullanılması önerilmektedir.
Entityler

Uygulamada iki tane entity (varlık) bulunmaktadır:

    TO-DO Listesi:
        ID
        İsim
        Oluşturma tarihi
        Güncellenme tarihi
        Silinme tarihi
        Listenin tamamlanma yüzdesi

    TO-DO Adımı:
        ID
        TO-DO Listesi ID
        Oluşturma tarihi
        Güncellenme tarihi
        Silinme tarihi
        İçerik
        Bitirilme durumu

API Endpointleri

Uygulamanın API endpointleri şu şekildedir:

    Login:
        Kullanıcı bir kullanıcı adı ve parola yollar eğer bilgiler doğru ise bir JWT oturum anahtarı alır.

    CRUD:
        Kullanıcı kendine bir TO-DO listesi oluşturabilir ve silebilir. Bu listeye maddeler ekleyebilir, çıkarabilir ve maddeleri değiştirebilir.
        Birinci tip kullanıcılar sadece kendi verileri üzerinde işlem yapabilir.
        İkinci tip kullanıcılar tüm kullanıcıların listelerini görebilir.
        
        
