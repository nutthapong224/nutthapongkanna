## หลักการทำงานของ Project
# จากภาพ การทำงานของ workflow  หลักๆ  มีการเทสที่ก่อนการ buildimage ด้วย github action ขึ้น github container  registry เมื่อ ทำ ci เสร็จจะ  trigger webhook ไปยัง jebkins ให้ดึง  image จากตัว  ginhub container registry มา deploy ลงใน jenkins vm ในส่วนของ cd 
![alt text](image.png)

1.การทำงานใส่ส่วนของ ci  อย่างแรกของ โจทย์ข้อ 2  นั้นต้องมีการ setup เพื่อให้ github action ดังภาพ 
![alt text](image-1.png)

2.

![alt text](image-2.png)

3.
![alt text](image-3.png)

4.
![alt text](image-4.png)

5. ดังในข้อกำหนด ข้อสอง มีการ install package ผ่าน requirements.txt แล้ว เมื่อเทสผ่าน แสดง สถานะ
✅ success
![alt text](image.png)

6. ในเคสที่เทสไม่ผ่านจะแสดง สถานะ ❌ failed” และ merge ไม่ได้ ไม่ได้ ดังภาพ

![alt text](image-5.png)
ส่วน แสดงผล “ Passed” ในหน้ํา PR/MR ไม่สามารถทำได้ใน github action ไม่สามารถแก้ข้อความที่ขึ้น  fail หรือ success ได้ เพราะมีคำ defualt ของ github action

