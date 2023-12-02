import cv2
from pyzbar.pyzbar import decode
import pyzbar
pyzbar.pyzbar.DebugScanner = False

def main():
    kamera = cv2.VideoCapture(0)

    while True:
        ret, frame = kamera.read()
        
        if not ret:
            print("Gagal membaca frame dari kamera")
            break
        
        if frame is not None:
            decode_objek = decode(frame)
            for obj in decode_objek:
                data = obj.data.decode('utf-8')
                print("QR Code Data:", data)
            
                # Menampilkan kotak
                titik = obj.polygon
                if len(titik) == 4:
                    pts = []
                    for j in range(4):
                        pts.append((int(titik[j].x), int(titik[j].y)))
                    pts = tuple(pts)
                    cv2.polylines(frame,  pts, isClosed=True, color=(0, 255, 0), thickness=2)
                
            # Tampilan Frame
            cv2.imshow('QR Code Scanner', frame)

        key = cv2.waitKey(1)
        if key == 113:  # ASCII untuk 'q'
            break
    # Keluar dari kamera dan menutup jendela
    kamera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("")
        