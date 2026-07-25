# 🚂 Railway Setup - Bosqichma-bosqich qo'llanma

## ❌ Sizda chiqayotgan xato

```
socket.gaierror: [Errno -2] Name or service not known
```

**Bu xato nimani anglatadi?**
- Bot ma'lumotlar bazasiga ulanolmayapti
- `DATABASE_URL` o'zgaruvchisi yo'q yoki noto'g'ri
- PostgreSQL Railway da qo'shilmagan

---

## ✅ Tuzatish qadamlari

### 1️⃣ Railway Dashboard ga kiring
- [railway.app](https://railway.app) ga o'ting
- Proyektingizni oching

### 2️⃣ PostgreSQL qo'shing (ENG MUHIM QADAM!)

1. **Dashboard da proyektingiz ochiq bo'lsin**
2. **"New" tugmasini toping va bosing** (yuqori o'ng burchakda)
3. **"Database" ni tanlang**
4. **"Add PostgreSQL" ni bosing**
5. Biroz kutasiz - PostgreSQL yaratilmoqda...
6. ✅ PostgreSQL container paydo bo'ladi

### 3️⃣ DATABASE_URL avtomatik qo'shilganligini tekshiring

1. Proyektingizda **asosiy service** (bot) ni oching
2. **"Variables"** bo'limiga o'ting
3. `DATABASE_URL` ni qidiring
4. **Agar `DATABASE_URL` YO'Q bo'lsa:**
   - PostgreSQL container ga o'ting
   - "Variables" bo'limidan `DATABASE_URL` ni ko'chirib oling
   - Bot service ga qo'lda qo'shing

### 4️⃣ Majburiy o'zgaruvchilarni qo'shing

**Variables** bo'limiga quyidagilarni kiriting:

```
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
SUPER_ADMIN_IDS=123456789,987654321
```

**Qo'shimcha o'zgaruvchilar (ixtiyoriy):**
```
REFERRAL_BONUS=20000
MIN_WITHDRAWAL=50000
RECEIPTS_CHANNEL_ID=-1001234567890
```

### 5️⃣ Qayta deploy qiling

Variables qo'shilgandan keyin Railway avtomatik deploy qiladi.

**Deploy Logs ni kuzating:**
```
# ✅ MUVAFFAQIYATLI:
✅ Jadvallar tekshirildi / yaratildi.
✅ Bot: @your_bot (ID: 123456789)
✅ Super adminlar: [123456789]
✅ Scheduler ishga tushdi.
🚀 Polling rejimida ishga tushmoqda...
```

```
# ❌ XATO (PostgreSQL yo'q):
socket.gaierror: [Errno -2] Name or service not known
```

---

## 🔍 Xatolarni tekshirish

### Deploy Logs da xato ko'rsatilmasa:
1. Railway dashboard → Proyektingiz
2. Service ni tanlang
3. **"Deploy Logs"** yoki **"Deployments"** ga o'ting
4. Oxirgi deployment ni oching
5. Qizil xatolar borligini tekshiring

### Variables to'g'ri ekanligini tekshirish:
```
✅ BOT_TOKEN mavjud va to'g'ri
✅ DATABASE_URL mavjud (postgresql:// bilan boshlanadi)
✅ SUPER_ADMIN_IDS mavjud
```

---

## 📞 Yordam kerakmi?

Agar yuqoridagi qadamlar yordam bermasa:

1. **PostgreSQL container ishlaganligini tekshiring**
   - Dashboard → PostgreSQL → "Metrics" - status "Running" bo'lishi kerak

2. **DATABASE_URL formati to'g'ri ekanligini tekshiring**
   - Format: `postgresql://username:password@hostname:port/database`
   - Railway format: `postgresql://postgres:password@containers.railway.app:1234/railway`

3. **Bot service va PostgreSQL bir proyektda ekanligini tekshiring**
   - Ikkalasi ham bir proyektda bo'lishi kerak

---

## 💡 Muhim eslatmalar

- ⚠️ SQLite production uchun ishlamaydi (Railway da fayllar o'chmaydi)
- ⚠️ PostgreSQL qo'shmasdan turib bot ishlamaydi
- ⚠️ `DATABASE_URL` ni qo'lda yozMANG - Railway avtomatik beradi
- ✅ PostgreSQL qo'shilishi bepul (Hobby plan)
- ✅ Bitta proyektda bir nechta service bo'lishi mumkin
