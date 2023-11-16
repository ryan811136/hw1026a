import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
  "title": "小王子【70周年精裝紀念版】",
  "author": "安東尼‧聖修伯里",
  "cover": "https://www.books.com.tw/img/001/066/04/0010660414.jpg",
  "url": "https://www.books.com.tw/products/0010660414",
  "anniversary": 70
},

{
  "title": "最後14堂星期二的課【20週年紀念版】",
  "author": "米奇‧艾爾邦",
  "cover": "https://www.books.com.tw/img/001/079/06/0010790676.jpg",
  "url": "https://www.books.com.tw/products/0010790676",
  "anniversary": 20
},

{
  "title": "撒哈拉歲月【三毛逝世30週年紀念版】",
  "author": "三毛",
  "cover": "https://www.books.com.tw/img/001/089/77/0010897794.jpg",
  "url": "https://www.books.com.tw/products/0010897794",
  "anniversary": 30
},

{
  "title": "靜宜求學趣",
  "author": "(黃于倫)",
  "cover": "(https://media.istockphoto.com/id/1257951336/zh/%E7%85%A7%E7%89%87/%E9%80%8F%E6%98%8E%E5%82%98%E4%B8%8B%E9%9B%A8%E5%B0%8D%E6%B0%B4%E6%BB%B4%E9%A3%9B%E6%BF%BA%E8%83%8C%E6%99%AF%E9%9B%A8%E5%A4%A9%E6%A6%82%E5%BF%B5.jpg?s=612x612&w=0&k=20&c=iYfREWUx74x1kWNTmpxRhcZakDJN8jXCHNWQ_VR2arE=)",
  "url": "(https://hw-seven.vercel.app/)",
  "anniversary": 19
}

]

collection_ref = db.collection("圖書精選")
for doc in docs:
  collection_ref.add(doc)