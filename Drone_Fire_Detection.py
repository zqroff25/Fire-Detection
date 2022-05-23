
# UNMANNED FIRE DETECTION DRONE (UFDD) IMAGE PROCESSING CODES 

#  Gereken Kütüphaneler
import cv2 as cv # Görüntü işleme fonksiyonları için
import numpy as np # renk aralıklarındaki değerli tutmak için
import smtplib # mail gönderme işlemi yapabilmek için
import time # zaman ile ilgili işlemler yapabilmek için
 
kontrol=0 # yangının kaç kere tespit edildiğini saklar
kisi="gönderen mail adresi"

def send_mail(): # mail gönderme fonksiyonu // cihaz yangını gerekli miktarda tespit ettiğinde ilgili birime mail atacak
    content = " Flame Detected 100 Times ! " # mailin içeriği
    mail = smtplib.SMTP("smtp.gmail.com",587) # smtp protokolü
    mail.ehlo()
    mail.starttls()
    mail.login("gönderen mail adresi","gönderilen mail adresi") # maili gönderen kişinin mail bilgileri (gmail üzerinden gizlilik izin vermek gerekebilir)
    mail.sendmail("gönderen mail adresi", "gönderilen mail adresi", content) # kimin kime ne göndereceği bu fonksiyon ile gerçekleştirilir
    # denemek için mail adresleri // yildizzakir0@gmail.com   // onurboztas99@gmail.com  // uvurdemiral@gmail.com

cap = cv.VideoCapture(0) # kameradan görüntü almak için "0" parametresi verilir istenirse videonun yolu belirtilerek kullanılır
 
fgbg = cv.createBackgroundSubtractorMOG2()# pikselin iyi tanımlanıp tanımlanmadığını kontrol eder
kernel = np.ones((2,2),np.uint8) # 2 ye 2 lik 8 bitlik unsignedint değerler saklayabilen bir array

# alınan görüntüler burada işleniyor

while(True):
    ret, frame = cap.read() 
    if (ret):
        frame1 = cv.pyrDown(frame) 
        fgmask = fgbg.apply(frame) 
        
        vid = cv.medianBlur(fgmask,11) # görüntüyü yumuşatır
        prdown = cv.pyrDown(vid) # görüntüyü bulanıklaştırır

        vid1 = cv.bitwise_and(frame1,frame1,mask=prdown) 

        hsv = cv.cvtColor(vid1,cv.COLOR_BGR2HSV) # rgb renk gamutu bgr a çevrilir

        # ateşin renginin bulunduğu aralık
        lower = [18, 50, 50]
        upper = [35, 255, 255]

        lower = np.array(lower, dtype="uint8") # lower en düşük kırmızı renk aralığındaki değerleri dizide tutar
        upper = np.array(upper, dtype="uint8") # upper en yüksek kırmızı renk aralığındaki değerleri dizide tutar

        mask = cv.inRange(hsv, lower, upper) # işlemlerin hangi aralıkta yapılacağını kontrol eder
    
        output = cv.bitwise_and(vid1, hsv, mask=mask)
        no_red = cv.countNonZero(mask) # lower ve upper aralığındaki değerlerin sayısını geri verir
    
        imgray = cv.cvtColor(output,cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(imgray,127,255,0) #  çok küçük veya çok büyük değerlere sahip pikselleri filtrelemek için kullanılır.
        result = cv.dilate(thresh,kernel,iterations = 3)  #  kaynak görüntüyü genişletir
        
        nlabels, labels, stats, centroids = cv.connectedComponentsWithStats(result) # 8 bitlik görüntü haline getirir

        for index, centroid in enumerate(centroids):
            if stats[index][0] == 0 and stats[index][1] == 0:
                continue
            if np.any(np.isnan(centroid)):
                continue

        x, y, width, height, area = stats[index]
        centerX, centerY = int(centroid[0]), int(centroid[1])

        if area >50:
            cv.rectangle(frame1, (x, y), (x + width, y + height), (255, 0, 0),3)

        cv.imshow('frame', frame1)

        if int(no_red) > 1050: # eğer kırmızı miktarı 1050 den büyükse
            kontrol+=1 # tespit sayısını 1 artır
            print(" Warning Flame detected ! : Control : ",kontrol) #ateş tespit edildi yaz
            time.sleep(0.1) # 0.1 sn sonra görüntü al
            if kontrol==20: # eğer program 100 kez ateşi tespit ettiyse bu işlemleri yap // 100 olmasının sebebi daha kesin sonuçlar elde etmek için
                #cv.imwrite("Yangin Resmi.jpg",frame)
                print(" UFDD is Sending a Mail To ",kisi," !")
                send_mail() # ilgili birime mail gönderir
                print(" UFDD Sent a Mail ! ------>> Check Mail Box or Spam Box ! \n \n") # gönderilen mailler spam kutusuna düşebiliyor.Bu durumu göstermek için uyarı
                break # maili gönderdikten sonra programı kapat
        else: # eğer kırmızı miktarı daha azsa kontrol değişkenini sıfırlar
            print(' No Flame Detected !')
            kontrol=0 # kontrol sıfırlanır
            time.sleep(0.08) # 0.08 sn sonra görüntü alır

        if cv.waitKey(1) & 0xFF == ord('q'): # q ya basıldığında program tamamen sonlanır
            break

cap.release() #görüntüleri yayımla
cv.destroyAllWindows() # program bitince tüm pencereleri kapar

#--------------------------------------------------------------------------------------------------------------------------------------------------------#
#    Program genel olarak görüntü üzerinde bulanıklaştırma, maskeleme ve ölçeklendirme işlemlerini yapar.                                                #
#    Daha sonra oluşan yeni görüntü,ilgili renk değer aralığında incelenir ve işlemler yapılır.                                                          #
#    Görüntüde maskeleme ve renk işlemlerinin ardından aranan renk oranı bulunduysa program bunu terminal ekranına basar.                                #
#    Eğer program istenilen sayıda görüntüyü tespit edebildiyse ilgili birime durumu mail olarak gönderir.                                               #
#---------------------------------------------------------------------FINISH ----------------------------------------------------------------------------#