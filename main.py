from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from hijri_converter import Hijri, Gregorian
import arabic_reshaper
from bidi.algorithm import get_display

def reshape_text(text):
    if not text:
        return ""
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

class DateConverterApp(App):
    def build(self):
        self.title = reshape_text("محول التاريخ الهجري والميلادي")
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.label_title = Label(
            text=reshape_text("محول التواريخ الهجرية والميلادية"),
            font_size='22sp',
            bold=True
        )
        layout.add_widget(self.label_title)

        self.input_year = TextInput(
            hint_text=reshape_text("السنة (مثال: 1445 أو 2024)"),
            multiline=False,
            input_filter='int',
            font_size='18sp'
        )
        layout.add_widget(self.input_year)

        self.input_month = TextInput(
            hint_text=reshape_text("الشهر (1-12)"),
            multiline=False,
            input_filter='int',
            font_size='18sp'
        )
        layout.add_widget(self.input_month)

        self.input_day = TextInput(
            hint_text=reshape_text("اليوم (1-31)"),
            multiline=False,
            input_filter='int',
            font_size='18sp'
        )
        layout.add_widget(self.input_day)

        btn_layout = BoxLayout(orientation='horizontal', spacing=10)
        
        self.btn_to_gregorian = Button(
            text=reshape_text("تحويل من هجري إلى ميلادي"),
            font_size='16sp',
            on_press=self.convert_to_gregorian
        )
        btn_layout.add_widget(self.btn_to_gregorian)

        self.btn_to_hijri = Button(
            text=reshape_text("تحويل من ميلادي إلى هجري"),
            font_size='16sp',
            on_press=self.convert_to_hijri
        )
        btn_layout.add_widget(self.btn_to_hijri)

        layout.add_widget(btn_layout)

        self.result_label = Label(
            text=reshape_text("النتيجة ستظهر هنا"),
            font_size='18sp',
            bold=True
        )
        layout.add_widget(self.result_label)

        return layout

    def get_inputs(self):
        try:
            y = int(self.input_year.text)
            m = int(self.input_month.text)
            d = int(self.input_day.text)
            return y, m, d
        except ValueError:
            return None

    def convert_to_gregorian(self, instance):
        inputs = self.get_inputs()
        if not inputs:
            self.result_label.text = reshape_text("يرجى إدخال أرقام صحيحة")
            return
        try:
            h_year, h_month, h_day = inputs
            g_date = Hijri(h_year, h_month, h_day).to_gregorian()
            res_str = f"الميلادي: {g_date.year}-{g_date.month:02d}-{g_date.day:02d}"
            self.result_label.text = reshape_text(res_str)
        except Exception as e:
            self.result_label.text = reshape_text("تاريخ هجري غير صحيح")

    def convert_to_hijri(self, instance):
        inputs = self.get_inputs()
        if not inputs:
            self.result_label.text = reshape_text("يرجى إدخال أرقام صحيحة")
            return
        try:
            g_year, g_month, g_day = inputs
            h_date = Gregorian(g_year, g_month, g_day).to_hijri()
            res_str = f"الهجري: {h_date.year}-{h_date.month:02d}-{h_date.day:02d}"
            self.result_label.text = reshape_text(res_str)
        except Exception as e:
            self.result_label.text = reshape_text("تاريخ ميلادي غير صحيح")

if __name__ == '__main__':
    DateConverterApp().run()
