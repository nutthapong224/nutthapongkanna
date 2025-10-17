# Python Hello World CI/CD

โปรเจค Python แบบง่ายที่สาธิตการใช้งาน CI/CD Pipeline ด้วย GitHub Actions และ Jenkins

## 📋 สิ่งที่ต้องเตรียม

- Python 3.12 หรือสูงกว่า
- pip (Python package manager)
- Docker
- Jenkins (สำหรับ deployment)

## 🚀 การติดตั้ง


## โครงสร้างโปรเจคและการใช้งานแบบปกติ

1. **Clone repository**
   ```bash
   git clone https://github.com/nutthapong224/nutthapongkanna.git
   cd nutthapongkanna
   ```

2. **ติดตั้ง dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 การใช้งาน

### รันแอปพลิเคชัน

```bash
python app/hello.py
```

### รัน Unit Tests

```bash
pytest -v
```

## 🔄 CI/CD Pipeline

### GitHub Actions

โปรเจคนี้ใช้ GitHub Actions ทั้งหมด 2 workflows:

#### 1. CI Test (`ci.yml`)
- **Trigger:** เมื่อมีการสร้าง Pull Request ไปยัง branch `main`
- **การทำงาน:**
  - ติดตั้ง Python dependencies
  - รัน unit tests ด้วย pytest

#### 2. Build and Push Docker Image (`docker-build.yml`)
- **Trigger:** เมื่อมีการ push code ไปยัง branch `main`
- **การทำงาน:**
  - Build Docker image
  - Push image ไปยัง GitHub Container Registry (GHCR)

### Jenkins Pipeline

Jenkinsfile กำหนดขั้นตอนการ deploy ดังนี้:

1. ดึง Docker image จาก GHCR
2. หยุดและลบ container เก่า (ถ้ามี)
3. รอการอนุมัติจากผู้ดูแลระบบ
4. Deploy ไปยัง staging environment
5. ตรวจสอบสถานะการ deploy
6. รัน integration tests ภายใน container

```

## 📁 โครงสร้างโปรเจค

```
c:\testbdi\
├── Dockerfile                  # Docker image configuration
├── Jenkinsfile                 # Jenkins pipeline definition
├── readme.md                   # เอกสารโปรเจค
├── requirements.txt            # Python dependencies
├── app\
│   ├── hello.py               # Application code
│   └── __init__.py            # Package initializer
├── .github\
│   └── workflows\
│       ├── ci.yml             # CI workflow
│       └── docker-build.yml   # Docker build workflow
└── tests\
    └── test_hello.py          # Unit tests
```

### คำอธิบายไฟล์สำคัญ

| ไฟล์/โฟลเดอร์ | คำอธิบาย |
|--------------|---------|
| `Dockerfile` | กำหนดค่าสำหรับสร้าง Docker image |
| `Jenkinsfile` | กำหนด pipeline สำหรับ Jenkins |
| `requirements.txt` | รายการ Python packages ที่ใช้ในโปรเจค |
| `app/hello.py` | Source code หลักของแอปพลิเคชัน |
| `app/__init__.py` | ทำให้ Python รู้จัก app เป็น package |
| `.github/workflows/` | เก็บไฟล์ GitHub Actions workflows |
| `tests/test_hello.py` | Unit tests สำหรับทดสอบฟังก์ชัน |

## 📝 หมายเหตุ

- ตรวจสอบให้แน่ใจว่าได้ตั้งค่า GitHub Container Registry credentials ใน Jenkins
- ปรับแต่ง Jenkinsfile ตามความต้องการของ environment ของคุณ


