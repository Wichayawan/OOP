from friend import Friend
from emailcontract import EmailableContract

# ข้อมูลเพื่อน
f1 = Friend("บ๊อบ", "bob@ksu.ac.th", "123-456-7890", 
            "เกษตรสมบูรณ์", "กาฬสินธุ์", "กาฬสินธุ์", "46000")
f2 = Friend("อลิซ", "alice@ksu.ac.th", "987-654-3210", 
            "ถนนไม่มี", "คำม่วง", "กาฬสินธุ์", "46000")

# สัญญา
s = EmailableContract("พิซซ่าฮัท", "pizza@ksu.ac.th")
s.send_mail("สวัสดี คุณเป็นอย่างไรบ้าง?")

# แสดงข้อมูลสัญญาทั้งหมด
for p in s.all_contracts:
    print("------------------------------")
    print(p)
    print()