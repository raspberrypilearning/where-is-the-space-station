## المقدمة

في هذا المشروع، ستستخدم خدمة ويب لمعرفة الموقع الحالي لمحطة الفضاء الدولية (ISS) وتحدِّد موقعها على الخريطة. 

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/b95851338c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/iss-final.png">
</div>

### معلومات إضافية لقادة النادي

إذا كنت بحاجة إلى طباعة هذا المشروع، فيُرجى استخدام [نسخة سهلة الطباعة](https://projects.raspberrypi.org/ar-SA/projects/where-is-the-space-station/print).


--- collapse ---
---
title: ملاحظات قادة النادي
---


## المقدمة:
يتناول هذا المشروع استخدام خدمات الويب لمعرفة الموقع الحالي لمحطة الفضاء الدولية وتفاصيل رواد الفضاء الموجودين في الفضاء حاليًا. وسيعمل الأطفال باستخدام JSON وبُنى بيانات وPython. 

## الموارد المتوفرة على الإنترنت

يستخدم هذا المشروع مجموعة من خدمات الويب. يرجى التأكد من إمكانية وصولكم إليها عن طريق أجهزة الكمبيوتر التي ستستخدمونها لمشاريع Code Club. 

+ [افتح واجهات برمجة تطبيقات Notify -- api.open-notify.org/](http://api.open-notify.org/)

__يستخدم هذا المشروع Python 3.__ نوصي باستخدام [trinket](https://trinket.io/) لكتابة Python على الإنترنت. يحتوي هذا المشروع على Trinket التالية:

+ ['أين توجد محطة الفضاء الدولية؟' مشروع البدء -- jumpto.cc/iss-go](http://jumpto.cc/iss-go)

كما يوجد مشروع trinket يحتوي على نموذج حل للتحديات:

+ [مشروع 'أين توجد محطة الفضاء الدولية؟ مُكتمل' -- trinket.io/python/9ccc368bd5](https://trinket.io/python/b95851338c)

## الموارد المتوفرة دون اتصال بالإنترنت
يمكن أن يكون هذا المشروع [مكتمل دون اتصال بالإنترنت] (https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) إذا كنت تفضل ذلك. يمكنك الوصول إلى موارد المشروع من خلال النقر فوق رابط "مواد المشروع" الخاص بهذا المشروع. يحتوي هذا الرابط على قسم "موارد المشروع"، الذي يتضمن الموارد التي يحتاج إليها الأطفال لإكمال هذا المشروع دون الاتصال بالإنترنت. تأكد من أن كل طفل لديه حق الوصول إلى نسخة من هذه الموارد. يتضمن هذا القسم الملفات التالية:

+ iss/iss.py
+ iss/map.gif
+ iss/iss.gif
+ iss/iss2.gif

يمكنك أيضًا العثور على نسخة كاملة من تحديات هذا المشروع في قسم "موارد المتطوعين" الذي يحتوي على:

+ iss-finished/iss.py
+ iss-finished/map.gif
+ iss-finished/iss.gif
+ iss-finished/iss2.gif

(جميع الموارد المذكورة أعلاه قابلة للتنزيل أيضًا كملفات `.zip` للمشاريع والمتطوعين).

## أهداف التعلم
+ استخدام خدمات الويب للحصول على بيانات حية؛
+ الدمج: استخدام بُنى بيانات Python وجرافيكيات السلحفاة. 

يتناول هذا المشروع عناصر من الصفوف التالية من [المناهج الرقمية الخاصة بـ Raspberry Pi](http://rpf.io/curriculum):

+ [دمج الإنشاءات البرمجية لحل مشكلة](https://www.raspberrypi.org/curriculum/programming/builder)

## التحديات:
+ اعرض المركبة الفضائية - قراءة البيانات من بنية بيانات مُرجعة؛
+ ابحث عن أوقات أخرى لمرور المحطة فوق موقع معين مباشرة - إرسال الإدخالات إلى خدمة ويب؛

## الأسئلة الشائعة
+ __لا تعمل صور png مع Python في حالة عدم الاتصال. لذا تم توفير صور بصيغة gif لاستخدامها في حالة عدم الاتصال.__
+ لاحظ أن هذا المشروع يستخدم الإدخالات النصية وجرافيكيات السلحفاة، ويمكنك تعديل المساحة المتوفرة لكل منهما في trinket. 




--- /collapse ---


--- collapse ---
---
title: مواد المشروع
---
## موارد المشروع
* [ملف .zip يحتوي على كل موارد المشروع](resources/iss-project-resources.zip)
* [Trinket عبر الإنترنت يحتوي على موارد مشروع البدء 'أين محطة الفضاء الدولية؟'](http://jumpto.cc/iss-go)
* [iss/iss.py](resources/iss-iss.py)
* [iss/map.gif](resources/iss-map.gif)
* [iss/iss.gif](resources/iss-iss.gif)
* [iss/iss2.gif](resources/iss-iss2.gif)

## موارد قادة النادي
* [ملف .zip يحتوي على كل موارد المشاريع المكتملة](resources/iss-volunteer-resources.zip)
* [مشروع Trinket المكتمل على الإنترنت](https://trinket.io/python/b95851338c)
* [iss-finished/iss.py](resources/iss-finished-iss.py)
* [iss-finished/map.gif](resources/iss-finished-map.gif)
* [iss-finished/iss.gif](resources/iss-finished-iss.gif)
* [iss-finished/iss2.gif](resources/iss-finished-iss2.gif)

--- /collapse ---
