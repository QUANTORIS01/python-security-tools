<div align='right'>

[🇬🇧 English](./CHANGELOG.md)

</div>

# تاریخچهٔ تغییرات

تمام تغییرات مهم این پروژه در این فایل مستند می‌شوند.

## [1.0.0] - انتشار اولیه

### قابلیت‌های اضافه‌شده

<div align='right' dir="rtl">

<span dir='rtl'>• افزودن قابلیت جست‌وجوی رکوردهای DNS.</span> <br>
<span dir='rtl'>• پشتیبانی از انواع رکوردهای DNS زیر:</span> <br>
  <span style='margin-right:30px' dir='rtl'>⁌ `A`</span> <br>
  <span style='margin-right:30px' dir='rtl'>⁌ `AAAA`</span> <br>
  <span style='margin-right:30px' dir='rtl'>⁌ `MX`</span> <br>
  <span style='margin-right:30px' dir='rtl'>⁌ `NS`</span> <br>
  <span style='margin-right:30px' dir='rtl'>⁌ `TXT`</span> <br>
  <span style='margin-right:30px' dir='rtl'>⁌ `CNAME`</span> <br>
<span dir='rtl'>• افزودن اعتبارسنجی دامنه.</span> <br>
<span dir='rtl'>• افزودن اعتبارسنجی نوع رکورد DNS.</span> <br>
<span dir='rtl'>• افزودن مدل ساختاریافتهٔ نتایج DNS با استفاده از `dataclass` به نام `DNSRecord`.</span> <br>
<span dir='rtl'>• افزودن نمایش خوانا در ترمینال.</span> <br>
<span dir='rtl'>• افزودن قابلیت خروجی‌گرفتن در قالب JSON.</span> <br>
<span dir='rtl'>• افزودن قابلیت خروجی‌گرفتن در قالب CSV.</span> <br>
<span dir='rtl'>• افزودن ثبت گزارش در فایل.</span> <br>
<span dir='rtl'>• افزودن رابط خط فرمان (CLI).</span> <br>
<span dir='rtl'>• افزودن مجموعهٔ تست خودکار با استفاده از `pytest`.</span>

</div>

### بهبودها

<p dir='rtl'>
• جداسازی مسئولیت‌های اعتبارسنجی، حل درخواست DNS، قالب‌بندی، خروجی‌گرفتن و ثبت گزارش. <br>
• ایجاد ساختار خروجی یکپارچه میان ترمینال و قالب‌های خروجی. <br>
• بهبود معماری پروژه برای نگهداری و تست آسان‌تر.
</p>

### مدیریت خطا

مدیریت مناسب وضعیت‌های زیر:

<div align='right' dir="rtl">

<span dir='rtl'>• دامنه‌های ناموجود (`NXDOMAIN`)</span> <br>
<span dir='rtl'>• نبود رکورد DNS در پاسخ (`NoAnswer`)</span> <br>
<span dir='rtl'>• شرایط پایان مهلت درخواست DNS (Timeout)</span> <br>
<span dir='rtl'>• در دسترس نبودن سرورهای DNS</span>

</div>

### تست‌ها

افزودن تست‌های واحد برای بخش‌های زیر:

<p dir='rtl'>
• اعتبارسنجی <br>
• Resolver <br>
• مدل‌ها <br>
• نتایج <br>
• قالب‌بندی خروجی <br>
• صادرکننده‌ها <br>
• ثبت گزارش <br>
• رابط خط فرمان (CLI)
</p>

### مستندات

<p dir='rtl'>
• افزودن مستندات کامل پروژه. <br>
• ایجاد ساختار مستندات دوزبانه (انگلیسی و فارسی). <br>
• مستندسازی معماری، نحوهٔ استفاده، محدودیت‌ها و بهبودهای آینده.
</p>
