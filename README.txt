Yangın tespit drone um için geliştirmiş olduğum yangın tespit programı.

Eğer kod çalışmıyorsa:
 Önce VS Code IDE ortamını kurunuz ( https://code.visualstudio.com/download )
 Ardından kodun çalışmasını sağlayan kütüphaneleri indirin. Bunun için terminal ekranı açmalısınız
 OpenCv için ( pip install opencv-python)
 Numpy için ( pip install numpy )
 Smtplib için ( pip install secure-smtplib )
 kütüphaneleri için verilen pip komutlarını terminal ekranında sırası ile çalıştırınız

 Ayrıca program mail gönderebildiği için koddaki mail gönderme ( send_mail())
fonksiyonundaki alanlara mail adreslerini girmeniz gerekmektedir.

Mail gönderme işleminde hata alıyorsanız kişisel mail adresinizden erişime 
izin vermeniz gerkmektedir.

Videodan yangın tespit etmek istiyorsanız kodun 22. satırında;
    cap = cv.VideoCapture(0) 0 yazan yere  
    cap = cv.VideoCapture("kullanılacak video adı")  nı yazarak videodan da 
    yangın tespiti yapabilirsiniz.
    video ve program kodunun aynı dosyada olmasına dikkat ediniz.


The fire detection program I developed for my fire detection drone.

If the code is not working:
 First install the VS Code IDE environment ( https://code.visualstudio.com/download )
 Then download the libraries that make the code work. For this you have to open a terminal screen
 For OpenCv ( pip install opencv-python)
 For numpy ( pip install numpy )
 For smtplib ( pip install secure-smtplib )
 Run the pip commands given for the libraries on the terminal screen in order

 Also, since the program can send mail, sending mail in the code ( send_mail())
You must enter your e-mail addresses in the fields in the function.

If you are getting an error while sending an e-mail, you can access it from your personal e-mail address.
You need your permission.

If you want to detect fire from video, on line 22 of the code;
    where cap = cv.VideoCapture(0) 0
    Cap = cv.VideoCapture("name of video to use") from the video as well
    You can detect fire.
    Make sure that the video and program code are in the same file.