import layoutparser as lp 
import cv2
import pytesseract
import functions

def ocrtext(image):
    Result=[]
    img = cv2.imread("static/uploads/"+image)
    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    img = cv2.bilateralFilter(img,9,75,75)
    cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    ocr_agent = lp.TesseractAgent(languages='fra')
    res = ocr_agent.detect(img, return_response=True )

    text=res['text']
    text = res['text'].split("\n")  
    
    dict={}
    dict['Dénimination']=functions.extractnom(text)
    dict['Date immatriculation']=functions.date(text)
    dict['Forme Juridique']=functions.form(text)
    dict['Activité']=functions.extractActivité(text)
    dict['Capital']=functions.Capital(text)
    dict['Siége Social']=functions.siege(text)


    return dict



