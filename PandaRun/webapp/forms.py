from django import forms
from webapp.models import full_runner
from webapp.models import half_runner
from webapp.models import contact

class full_runner_form(forms.ModelForm):
    class Meta():
        model = full_runner
        fields = ('first_name',
                    'last_name',
                    'age',
                    'gender',
                    'shirt_size',
                    'team',
                    'send',
                    'address',
                    'mobile',
                    'capture'
                    )

        labels = {
        "first_name": "ชื่อ (ไม่ต้องใส่คำนำหน้า)",
        "last_name": "นามสกุล",
        "age":"อายุ (นับตามปีเกิด)",
        "gender":"เพศ",
        "shirt_size":"ขนาดเสื้อ",
        "team":"ชื่อทีม/ชมรม",
        "send":"วิธีการรับเสื้อ+BIB",
        "address":"ที่อยู่ ถนน ตำบล/แขวง อำเภอ/เขต จังหวัด รหัสไปรษณีย์",
        "mobile":"เบอร์โทรศัพท์มือถือ (ไม่ต้องใส่ขีด)",
        "capture":"หลักฐานการโอนเงิน"
                    }

class half_runner_form(forms.ModelForm):
    class Meta():
        model = half_runner
        fields = ('first_name',
                    'last_name',
                    'age',
                    'gender',
                    'shirt_size',
                    'team',
                    'send',
                    'address',
                    'mobile',
                    'capture'
                    )

        labels = {
        "first_name": "ชื่อ (ไม่ต้องใส่คำนำหน้า)",
        "last_name": "นามสกุล",
        "age":"อายุ (นับตามปีเกิด)",
        "gender":"เพศ",
        "shirt_size":"ขนาดเสื้อ",
        "team":"ชื่อทีม/ชมรม",
        "send":"วิธีการรับเสื้อ+BIB",
        "address":"ที่อยู่ ถนน ตำบล/แขวง อำเภอ/เขต จังหวัด รหัสไปรษณีย์",
        "mobile":"เบอร์โทรศัพท์มือถือ (ไม่ต้องใส่ขีด)",
        "capture":"หลักฐานการโอนเงิน"
                    }

class contact_form(forms.ModelForm):
    class Meta():
        model = contact
        fields = ('first_name',
                    'email',
                    'mobile',
                    'comment',
                    )

        labels = {
        "first_name": "ผู้ติดต่อ",
        "email": "email",
        "mobile":"เบอร์ติดต่อ",
        "comment":"ข้อความที่ต้องการติดต่อ"
                    }
