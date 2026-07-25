# 📦 Xitoydan Zakaz Qilish Kurslari Bot

Aiogram v3 + PostgreSQL asosida qurilgan to'liq avtomatlashtirilgan kurs sotish bot tizimi.

---

## 🚀 Railway ga Deploy qilish

### 1. GitHub ga push qiling
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/SIZNING_USERNAME/SIZNING_REPO.git
git push -u origin main
```

### 2. Railway da yangi loyiha yarating
1. [railway.app](https://railway.app) ga kiring
2. **New Project** → **Deploy from GitHub repo** → repo ni tanlang

### 3. ⚠️ MUHIM: PostgreSQL qo'shing
**Bu qadamni o'tkazib yubormang!**

1. Railway dashboard da proyektingizni oching
2. **New** tugmasini bosing
3. **Database** → **Add PostgreSQL** ni tanlang
4. Railway avtomatik ravishda PostgreSQL yaratadi va `DATABASE_URL` ni qo'shadi

**❌ Agar bu qadamni bajarmassangiz, bot ishlamaydi va quyidagi xato chiqadi:**
```
socket.gaierror: [Errno -2] Name or service not known
```

### 4. Environment Variables qo'shing
Railway dashboard → **Variables** bo'limiga quyidagilarni kiriting:

| Kalit | Qiymat | Majburiy |
|-------|--------|----------|
| `BOT_TOKEN` | Botning token raqami | ✅ Ha |
| `SUPER_ADMIN_IDS` | Admin Telegram IDlari (vergul bilan) | ✅ Ha |
| `DATABASE_URL` | **QO'SHMANG** - PostgreSQL avtomatik qo'shadi | ⚠️ Avtomatik |
| `REFERRAL_BONUS` | Referal bonus (masalan: 20000) | ❌ Ixtiyoriy |
| `MIN_WITHDRAWAL` | Minimal yechish (masalan: 50000) | ❌ Ixtiyoriy |
| `RECEIPTS_CHANNEL_ID` | Cheklar yuboriladigan kanal ID | ❌ Ixtiyoriy |
| `WEBHOOK_URL` | Bo'sh qoldirilsa avtomatik aniqlanadi | ❌ Ixtiyoriy |

> **⚠️ ESLATMA:** `DATABASE_URL` ni qo'lda yozMANG! Railway PostgreSQL qo'shganda avtomatik to'ldiriladi!

### 5. Deploy va Tekshirish
Variables kiritilgandan keyin Railway avtomatik deploy qiladi. 

**Deploy Logs ni tekshiring:**
- ✅ Muvaffaqiyatli: `✅ Jadvallar tekshirildi / yaratildi.`
- ❌ Xato: `socket.gaierror` - PostgreSQL qo'shilmaganligini bildiradi (3-qadamga qayting)

---

## 💻 Lokal ishga tushirish

```bash
pip install -r requirements.txt
cp .env.example .env
# .env faylni to'ldiring
python main.py
```

---

## 📱 Bot funksionalligi

### Foydalanuvchi uchun:
- 📚 Bir yoki bir nechta kurs tanlash (chegirma tizimi bilan)
- 💳 To'lov kartalari orqali to'lash
- 🎓 Mening kurslarim — tasdiqlangan kurslar + kanal havolasi
- 👥 Referal tizim — do'st taklif qilish va bonus yig'ish

### Admin uchun:
- 📊 Statistika (foydalanuvchilar, sotuvlar, daromad)
- ✅ To'lovlarni tasdiqlash/rad etish
- 💸 Pul yechish so'rovlari (chek rasm bilan)
- 📚 Kurslar CRUD
- 💳 To'lov kartalari boshqaruvi
- 🎁 Chegirma qoidalari (bundle)
- 📢 Homiy kanallar
- 📣 Broadcast xabar yuborish
- 👮 Admin qo'shish/o'chirish
- ⚙️ Sozlamalar (bonus, yechish, FAQ, kurs sahifasi matni)

---

## ⚙️ Sozlamalar (.env)

```env
BOT_TOKEN=bot_token
DATABASE_URL=postgresql+asyncpg://...   # Railway avtomatik beradi
SUPER_ADMIN_IDS=123456789,987654321      # Vergul bilan ajrating
REFERRAL_BONUS=20000                     # So'mda
MIN_WITHDRAWAL=50000                     # So'mda
```
