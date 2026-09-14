<div dir="rtl">

# درس ۱ — برنامه‌نویسی چیست؟

## مقدمه

قبل از اینکه Python یاد بگیریم، باید یک سؤال ساده اما بسیار مهم را جواب بدهیم:

**برنامه‌نویسی چیست؟**

اگر این مفهوم را درست متوجه نشویم، ممکن است بتوانیم کدهای Python را حفظ کنیم، اما وقتی با یک مسئله جدید روبه‌رو شویم ندانیم از کجا باید شروع کنیم.

هدف این دوره حفظ کردن کد نیست.

هدف این است که یاد بگیریم:

> یک مسئله را به مراحل کوچک تبدیل کنیم، آن مراحل را به زبان قابل فهم برای کامپیوتر بیان کنیم و در نهایت یک برنامه قابل اجرا بسازیم.

در پروژه‌ی ما نیز دقیقاً همین اتفاق خواهد افتاد.

در نهایت می‌خواهیم از یک مسئله‌ی ساده شروع کنیم:

> «چطور بفهمیم یک TCP port روی یک سیستم باز است؟»

و مرحله‌به‌مرحله آن را به یک Port Scanner واقعی تبدیل کنیم.

---

# 1. کامپیوتر چیست؟

قبل از برنامه‌نویسی باید بدانیم با چه چیزی صحبت می‌کنیم.

کامپیوتر دستگاهی است که می‌تواند:

<p dir='rtl'>
• اطلاعات دریافت کند <br>
• اطلاعات را پردازش کند <br>
• اطلاعات را ذخیره کند <br>
• نتیجه تولید کند
</p>

اما کامپیوتر برخلاف انسان، به شکل طبیعی مفهوم جمله‌های انسانی را درک نمی‌کند.

مثلاً اگر به یک کامپیوتر بگوییم:

> «برو ببین آیا port شماره 80 باز است یا نه.»

این جمله برای انسان قابل فهم است، اما کامپیوتر برای انجام آن به دستورهای دقیق نیاز دارد.

ما باید دقیقاً مشخص کنیم:

<p dir='rtl'>
1. به کدام IP متصل شود؟ <br>
2. از چه protocol استفاده کند؟ <br>
3. به کدام port متصل شود؟ <br>
4. چقدر برای پاسخ منتظر بماند؟ <br>
5. اگر اتصال موفق شد چه کاری انجام دهد؟ <br>
6. اگر اتصال شکست خورد چه کاری انجام دهد؟
</p>

این همان جایی است که **برنامه‌نویسی** وارد می‌شود.

---

# 2. برنامه‌نویسی چیست؟

<p dir='rtl'>
<strong>Programming</strong> یعنی نوشتن مجموعه‌ای از دستورها برای اینکه کامپیوتر یک کار مشخص را انجام دهد.
</p>

به زبان ساده:

<p dir='rtl' style='background-color: #2f302f;padding-right:14px;border-left:4px solid #8e918f'>
 Programming = تبدیل یک مسئله به دستورهای دقیق و قابل اجرا برای کامپیوتر
</p>

مثلاً فرض کنیم می‌خواهیم برنامه‌ای بنویسیم که دو عدد را جمع کند.

مسئله:

```text
عدد اول = 10
عدد دوم = 20
```

کاری که می‌خواهیم:

```text
10 + 20
```

نتیجه:

```text
30
```

برای انسان بسیار ساده است.

اما برنامه باید این کار را به شکلی بیان کند که زبان برنامه‌نویسی آن را بفهمد.

مثلاً در Python:

```python
print(10 + 20)
```

خروجی:

```text
30
```

ما یک مسئله‌ی انسانی را به یک دستور قابل اجرا تبدیل کردیم.

---

<p dir='rtl' style='font-size:32px;font-wight:bold;'>
3. Program چیست؟
</p>

<p dir='rtl'>
<strong>Program</strong> یا برنامه، مجموعه‌ای از دستورهاست که برای انجام یک کار مشخص نوشته شده است.
</p>

مثلاً یک برنامه می‌تواند:

<p dir='rtl'>
• ماشین حساب باشد <br>
• مرورگر وب باشد <br>
• بازی باشد <br>
• سیستم مدیریت فایل باشد <br>
• Web Server باشد <br>
• Port Scanner باشد
</p>

برنامه‌ای که در پروژه‌ی ما می‌سازیم نیز مجموعه‌ای از دستورهاست که وظیفه‌ی آن بررسی وضعیت portهای TCP است.

---

<p dir='rtl' style='font-size:32px;font-wight:bold;'>
4. Code چیست؟
</p>

<p dir='rtl'>
<strong>Code</strong> به دستورهایی گفته می‌شود که ما با استفاده از یک زبان برنامه‌نویسی می‌نویسیم.
</p>

مثلاً:

```python
print("Hello")
```

این یک قطعه **Python code** است.

در اینجا:

```python
print
```

یک function داخلی Python است که برای نمایش مقدار استفاده می‌شود.

و:

```python
"Hello"
```

متنی است که می‌خواهیم نمایش داده شود.

وقتی این دو را کنار هم قرار می‌دهیم:

```python
print("Hello")
```

<p dir='rtl'>
Python آن را اجرا می‌کند و نتیجه می‌شود:
</p>

```text
Hello
```

---

<p dir='rtl' style='font-size:32px;font-wight:bold;'>
5. Programming Language چیست؟
</p>

کامپیوتر برای اجرای برنامه‌ها به دستورهای دقیق نیاز دارد.

برای نوشتن این دستورها از **Programming Language** یا زبان برنامه‌نویسی استفاده می‌کنیم.

زبان‌های برنامه‌نویسی مختلفی وجود دارند، مانند:

<p dir='rtl'>
• Python <br>
• C <br>
• C++ <br>
• Java <br>
• JavaScript <br>
• Go <br>
• Rust
</p>

هر زبان syntax و قوانین خودش را دارد.

مثلاً در Python:

```python
print("Hello")
```

اما در زبان‌های دیگر ممکن است روش نوشتن همین مفهوم متفاوت باشد.

بنابراین:

<p dir='rtl' style='background-color: #2f302f;padding-right:14px;border-left:4px solid #8e918f'>
Programming Language ابزاری است که به ما اجازه می‌دهد دستورهای قابل فهم برای ماشین را به شکل ساختاریافته بنویسیم.
</p>

---

# 6. چرا Python؟

در این پروژه از Python استفاده می‌کنیم.

<p dir='rtl'>
Python به دلایل مختلف برای این پروژه مناسب است:
</p>

### خوانایی

<p dir='rtl'>
Syntax آن نسبتاً ساده و خواناست.
</p>

مثلاً:

```python
print("Hello")
```

برای یک انسان بسیار قابل فهم است.

### کتابخانه‌های استاندارد

<p dir='rtl'>
Python امکاناتی برای کارهایی مانند:
</p>

<p dir='rtl'>
• networking <br>
• sockets <br>
• فایل‌ها <br>
• JSON <br>
• concurrency <br>
• testing <br>
• command-line applications
</p>

در اختیار ما قرار می‌دهد.

در پروژه‌ی فعلی نیز از بخش‌هایی از کتابخانه استاندارد Python مانند:

```python
socket
```

و:

```python
concurrent.futures
```

استفاده می‌کنیم.

### مناسب برای یادگیری

<p dir='rtl'>
Python اجازه می‌دهد بیشتر روی **حل مسئله** تمرکز کنیم و کمتر درگیر syntax پیچیده شویم.
</p>

---

<p dir='rtl' style='font-size:32px;font-wight:bold;'>
7. Python خودش چیست؟
</p>

<p dir='rtl'>
Python یک <strong>programming language</strong> است.
</p>

اما یک سؤال مهم‌تر وجود دارد:

اگر Python فقط یک زبان است، کامپیوتر چگونه کد Python ما را اجرا می‌کند؟

اینجا مفهوم **Python Interpreter** مطرح می‌شود.

---

<p dir='rtl' style='font-size:32px;font-wight:bold;'>
8. Interpreter چیست؟
</p>

وقتی ما می‌نویسیم:

```python
print("Hello")
```

پردازنده‌ی کامپیوتر مستقیماً این عبارت را به عنوان یک دستور Python اجرا نمی‌کند.

یک پیاده‌سازی از Python، مانند **CPython**، کد Python را دریافت و آن را برای اجرا پردازش می‌کند.

به طور ساده می‌توانیم این مسیر را این‌طور تصور کنیم:

```text
Python Code
     ↓
Python Interpreter
     ↓
Execution
     ↓
Output
```

مثلاً:

```text
print("Hello")
```

↓

```text
Python
```

↓

```text
Hello
```

این مدل ذهنی برای شروع کافی است.

جزئیات داخلی اجرای Python را بعداً در درس‌های مربوط به interpreter و runtime بررسی خواهیم کرد.

---

# 9. اولین برنامه Python

حالا اولین برنامه‌ی خودمان را می‌نویسیم:

```python
print("Hello, World!")
```

اگر آن را اجرا کنیم:

```text
Hello, World!
```

خواهیم دید.

---

<p dir='rtl' style='font-size:32px;font-wight:bold;'>
10. <mark style='background-color: #525352; color: #ffffffcd'>print()</mark> چیست؟
</p>

در Python، `print()` برای نوشتن اطلاعات روی **standard output** استفاده می‌شود.

در ساده‌ترین حالت، این یعنی اطلاعاتی را در terminal مشاهده می‌کنیم.

مثلاً:

```python
print("Hello")
```

خروجی:

```text
Hello
```

بیایید این دستور را قسمت‌بندی کنیم.

```python
print("Hello")
```

<p dir='rtl'>
<mark style='background-color: #525352; color: #ffffffcd; font-size:24px;'>print</mark>
</p>

نام تابع است.

### `(` و `)`

این پرانتزها برای فراخوانی function و قرار دادن argumentهای آن استفاده می‌شوند.

<p dir='rtl'>
<mark style='background-color: #525352; color: #ffffffcd; font-size:24px;'>"Hello"</mark>
</p>

یک **string** است.

### کل دستور

```python
print("Hello")
```

یعنی:

> مقدار `"Hello"` را برای نمایش روی standard output ارسال کن.

---

<p dir='rtl' style='font-size:32px;font-wight:bold;'>
11. Function چیست؟
</p>

<p dir='rtl'>
Function یکی از مهم‌ترین مفاهیم Python است.
</p>

<p dir='rtl'>
Function را فعلاً می‌توانیم این‌طور تصور کنیم:
</p>

> یک بخش از برنامه که یک کار مشخص انجام می‌دهد.

مثلاً:

```python
print()
```

وظیفه‌اش نمایش اطلاعات است.

بعداً خودمان نیز function خواهیم ساخت.

مثلاً:

```python
def say_hello():
    print("Hello")
```

در اینجا:

```python
def
```

برای تعریف function استفاده می‌شود.

و:

```python
say_hello
```

نام function است.

بعداً به طور کامل درباره‌ی:

<p dir='rtl'>
• function <br>
• parameter <br>
• argument <br>
• return <br>
• scope
</p>

صحبت خواهیم کرد.

فعلاً فقط این مفهوم را به خاطر داشته باش:

<p dir='rtl' style='background-color: #2f302f;padding-right:14px;border-left:4px solid #8e918f'>
Function یعنی یک بخش قابل استفاده از برنامه که مسئول انجام یک کار مشخص است.
</p>

---

<p dir='rtl' style='font-size:32px;font-wight:bold;'>
12. String چیست؟
</p>

در مثال:

```python
print("Hello")
```

عبارت:

```python
"Hello"
```

یک **string** است.

<p dir='rtl'>
String یعنی داده‌ی متنی.
</p>

مثلاً:

```python
"Hello"
```

یا:

```python
"Python"
```

یا:

```python
"127.0.0.1"
```

همه string هستند.

حتی این:

```python
"80"
```

هم string است.

دقت کن:

```python
80
```

و:

```python
"80"
```

یکی نیستند.

اولی یک عدد است.

دومی یک متن است.

این تفاوت در برنامه‌نویسی بسیار مهم است و بعداً به طور کامل بررسی خواهد شد.

---

<p dir='rtl' style='font-size:32px;font-wight:bold;'>
13. Terminal چیست؟
</p>

در طول پروژه زیاد با **Terminal** کار خواهیم کرد.

<p dir='rtl'>
Terminal محیطی است که می‌توانیم در آن دستورهای متنی را اجرا کنیم.
</p>

مثلاً:

```powershell
python --version
```

یا:

```powershell
python
```

یا اجرای برنامه:

```powershell
python src/cli.py
```

در پروژه‌ی ما Terminal اهمیت زیادی دارد، چون Port Scanner یک **CLI application** است.

<p dir='rtl'>
CLI یعنی:
</p>

<p dir='rtl' style='background-color: #2f302f;padding-right:14px;border-left:4px solid #8e918f'>
Command-Line Interface
</p>

یعنی کاربر با برنامه از طریق command line تعامل می‌کند.

---

<p dir='rtl' style='font-size:32px;font-wight:bold;'>
14. Standard Output چیست؟
</p>

وقتی برنامه چیزی را با `print()` نمایش می‌دهد، این اطلاعات معمولاً به **stdout** یا **standard output** می‌رود.

مثلاً:

```python
print("Hello")
```

به صورت مفهومی:

```text
Python Program
      |
      v
    stdout
      |
      v
   Terminal
```

بعداً وقتی با:

<p dir='rtl'>
• logging <br>
• pipes <br>
• shell commands <br>
• redirection
</p>

کار کنیم، تفاوت stdout و سایر streamها اهمیت بیشتری پیدا می‌کند.

---

# 15. برنامه‌نویسی فقط نوشتن Code نیست

این یکی از مهم‌ترین قسمت‌های این درس است.

بسیاری از افراد تصور می‌کنند برنامه‌نویسی یعنی:

> «کد بنویس.»

اما برنامه‌نویسی واقعی قبل از نوشتن code شروع می‌شود.

فرض کنیم مسئله این است:

> یک Port Scanner بساز.

اگر فوراً شروع کنیم به نوشتن:

```python
socket.socket(...)
```

ممکن است برنامه‌ای بنویسیم که کار کند، اما احتمالاً مشکلات زیادی خواهد داشت.

اول باید مسئله را تحلیل کنیم.

مثلاً:

```text
Problem
  ↓
Requirements
  ↓
Design
  ↓
Implementation
  ↓
Testing
  ↓
Debugging
  ↓
Refactoring
```

این workflow یکی از مهم‌ترین چیزهایی است که در این پروژه یاد خواهیم گرفت.

---

# 16. مثال: طراحی Port Scanner

مسئله:

> می‌خواهیم بدانیم آیا یک TCP port باز است یا نه.

اول مسئله را به سؤال‌های کوچک‌تر تقسیم می‌کنیم.

### سؤال ۱

<p dir='rtl'>
Target چیست؟
</p>

مثلاً:

```text
127.0.0.1
```

### سؤال ۲

کدام port را بررسی کنیم؟

مثلاً:

```text
80
```

### سؤال ۳

چگونه بررسی کنیم؟

می‌توانیم تلاش کنیم یک TCP connection ایجاد کنیم.

### سؤال ۴

اگر connection موفق شد؟

احتمالاً port باز است.

### سؤال ۵

اگر connection شکست خورد؟

احتمالاً port قابل اتصال نیست.

### سؤال ۶

اگر connection خیلی طول کشید؟

باید timeout داشته باشیم.

حالا مسئله کم‌کم قابل پیاده‌سازی شده است.

---

<p dir='rtl' style='font-size:32px;font-wight:bold;'>
17. Algorithm چیست؟
</p>

قبل از نوشتن code می‌توانیم مراحل حل مسئله را به صورت یک **Algorithm** بیان کنیم.

برای یک port:

<p dir='rtl' style='background-color: #2f302f;padding-right:14px;border-left:4px solid #8e918f'>
1. Target IP را دریافت کن.<br>
2. Port را دریافت کن.<br>
3. یک TCP socket ایجاد کن.<br>
4. Timeout تنظیم کن.<br>
5. تلاش کن به target متصل شوی.<br>
6. اگر اتصال موفق شد:<br>
      <span style='padding-right:130px'> port = OPEN </span> <br>
7. اگر اتصال موفق نشد:<br>
      <span style='padding-right:110px'> port = NOT OPEN </span> <br>
8. socket را ببند.
</p>

این هنوز Python code نیست.

اما یک نقشه برای نوشتن Python code است.

این تفاوت بسیار مهم است:

<p dir='rtl' style='background-color: #2f302f;padding-right:14px;border-left:4px solid #8e918f'>
Algorithm = روش حل مسئله
</p>

<p dir='rtl' style='background-color: #2f302f;padding-right:14px;border-left:4px solid #8e918f'>
Code = پیاده‌سازی آن روش با یک زبان برنامه‌نویسی
</p>

---

# 18. چرا این موضوع برای Cybersecurity مهم است؟

در Cybersecurity دائماً با مسئله‌هایی روبه‌رو می‌شویم که باید آن‌ها را به مراحل کوچک‌تر تقسیم کنیم.

مثلاً:

```text
Reconnaissance
      ↓
Identify Host
      ↓
Identify Ports
      ↓
Identify Services
      ↓
Identify Versions
      ↓
Analyze Attack Surface
```

هر مرحله خودش یک مسئله است.

اگر Python را فقط به صورت syntax یاد بگیریم، ممکن است بتوانیم:

```python
for
if
def
import
```

بنویسیم.

اما نمی‌دانیم **چه زمانی و چرا** باید از آن‌ها استفاده کنیم.

هدف این دوره این است که علاوه بر syntax، توانایی حل مسئله را هم یاد بگیریم.

---

# 19. اشتباه رایج شماره ۱: حفظ کردن Code

فرض کن این کد را حفظ کرده‌ای:

```python
print("Hello")
```

اگر فردا از تو بپرسند:

> چگونه دو عدد را جمع کنیم؟

ممکن است فقط همان کد را بلد باشی و ندانستی چه کار کنی.

اما اگر مفهوم را فهمیده باشی، می‌توانی مسئله را تحلیل کنی:

```text
دو مقدار داریم
      ↓
آن‌ها را جمع می‌کنیم
      ↓
نتیجه را نمایش می‌دهیم
```

و به:

```python
print(10 + 20)
```

می‌رسی.

پس:

> هدف یادگیری Programming، حفظ کردن syntax نیست؛ توانایی ساختن راه‌حل است.

---

# 20. اشتباه رایج شماره ۲: شروع مستقیم از Code

وقتی مسئله‌ای دریافت می‌کنی، قبل از نوشتن code این سؤال‌ها را بپرس:

<p dir='rtl' style='background-color: #2f302f;padding:10px 14px 10px 0;border-left:4px solid #8e918f'>
Problem چیست؟ <br>
Input چیست؟ <br>
Output چیست؟ <br>
Rules چیست؟ <br>
Constraints چیست؟ <br>
Edge Cases چیست؟
</p>

مثلاً برای Port Scanner:

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
Input
</p>

```text
IP address
Start port
End port
Timeout
Workers
```

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
Output
</p>

مثلاً:

```text
80 OPEN
443 OPEN
```

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
Constraints
</p>

مثلاً:

<p dir='rtl' style='background-color: #2f302f;padding:10px 14px 10px 0;border-left:4px solid #8e918f'>
Port باید بین 0 و 65535 باشد. <br>
Timeout باید مثبت باشد.
</p>

این نوع تفکر بعداً در طراحی پروژه بسیار مهم خواهد بود.

---

# 21. ارتباط این درس با پروژه

در پروژه‌ی ما:

```text
Problem
   ↓
Network Concepts
   ↓
Python Concepts
   ↓
Algorithm
   ↓
Implementation
   ↓
Tests
   ↓
Working Tool
```

برای مثال:

<p dir='rtl' style='background-color: #2f302f;padding:10px 14px 10px 0;border-left:4px solid #8e918f'>
"Port Scanner بساز"
</p>

به:

```text
socket
```

منتهی می‌شود.

سپس:

```text
socket
+
timeout
+
connection
```

به:

```text
scan_port()
```

منتهی می‌شود.

بعد:

```text
scan_port()
+
multiple ports
+
concurrency
```

به:

```text
scan_range()
```

منتهی می‌شود.

و بعد:

```text
scanner
+
service detection
+
banner grabbing
+
results
+
formatting
+
export
```

به ابزار فعلی ما تبدیل می‌شود.

پس هر فایل پروژه نتیجه‌ی یک مفهوم و یک مسئله‌ی مشخص خواهد بود.

---

# 22. تمرین

## تمرین ۱

بدون اجرای Python، توضیح بده این کد چه کاری انجام می‌دهد:

```python
print("Python")
```

---

## تمرین ۲

تفاوت این دو را توضیح بده:

```python
print(80)
```

و:

```python
print("80")
```

---

## تمرین ۳

این مسئله را به مراحل کوچک تقسیم کن:

> برنامه‌ای بساز که نام کاربر را دریافت کند و سپس به او سلام کند.

فعلاً code ننویس.

فقط Algorithm را بنویس.

مثلاً:

```text
1. ...
2. ...
3. ...
```

---

## تمرین ۴ — Challenge

مسئله:

> برنامه‌ای می‌خواهیم که یک IP و یک port دریافت کند و بررسی کند آیا می‌تواند به آن port متصل شود یا نه.

فعلاً Python code ننویس.

فقط مشخص کن:

<p dir='rtl' style='font-size:20px; font-wight:bold;'>
Input چیست؟
</p>

<p dir='rtl' style='font-size:20px; font-wight:bold;'>
Output چیست؟
</p>

### مراحل Algorithm چیست؟

### چه چیزهایی ممکن است باعث شکست عملیات شوند؟

این تمرین مقدمه‌ی مستقیم ورود ما به بخش Networking و سپس `scanner.py` است.

---

# 23. جمع‌بندی

در این درس یاد گرفتیم:

<p dir='rtl'>
• Computer چیست. <br>
• Programming چیست. <br>
• Program چیست. <br>
• Code چیست. <br>
• Programming Language چیست. <br>
• Python چیست. <br>
• Interpreter چه نقشی دارد. <br>
• <mark style='background-color: #525352; color: #ffffffcd; padding:2px;' dir='ltr'>print()</mark> چیست. <br>
• Function چیست. <br>
• String چیست. <br>
• Terminal چیست. <br>
• stdout چیست. <br>
• Algorithm چیست. <br>
• چرا قبل از نوشتن code باید مسئله را تحلیل کنیم. <br>
• چرا حفظ کردن code با یادگیری Programming متفاوت است.
</p>

مهم‌ترین مفهوم این درس:

> **برنامه‌نویس کسی نیست که فقط syntax را بلد باشد؛ برنامه‌نویس کسی است که بتواند یک مسئله را تحلیل کند و برای آن راه‌حل قابل اجرا بسازد.**

در پروژه‌ی ما این مهارت را از ساده‌ترین مفاهیم شروع می‌کنیم و در نهایت از آن برای ساختن یک Network Reconnaissance Tool استفاده خواهیم کرد.

</div>
