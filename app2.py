from flask import Flask

app = Flask(__name__)

# صفحه اصلی
@app.route('/')
def home():
    return '''
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        a { text-decoration: none; color: pink; margin: 10px; }
        a:hover { color: purple; }
    </style>
    <h1>خوش اومدی عسلچه ی بابا</h1>
    <p>زیباترین زیباها دوستت دارم</p>
    <a href="/my_apologies">my apologies</a><br>
    <a href="/you_may_not_believe_me_but..">you may not believe me but..</a>
    '''

# صفحه عذرخواهی
@app.route('/my_apologies')
def my_apologies():
    return '''
    <h1>my apologies</h1>
    <p>نمیدونم از کجا شروع کنم..فقط میتونم بگم عاشقتم... اون پنج ماهی که باهات گذروندم بهترین قسمت زندگیم و نعمتی از طرف خدا به من بودن..میدونم آدم افتضاحیم.. میدونم کارم قابل بخشش نیست..و اشکال نداره اگه دیگه دوستم نداشته باشی..من بازم عاشقت میمونم:) تنها چیزی که میخوام بخششه..و البته نبودن نفرتی از طرف تو نسبت به من..میتونم تحمل کنم عاشقم نباشی اما نمیتونم نفرتت رو تحمل کنم..واقعا معذرت میخوام بابت همه چیز..
ای کاش میتونستم به گذشته برگردم و همه چیز رو درست کنم اما غیر ممکنه..متاسفم‌ و عاشقتم</p>
    <a href="/">بازگشت به صفحه اصلی</a>
    '''

# صفحه دیگری
@app.route('/you_may_not_believe_me_but..')
def you_may_not_believe_me_but():
    return '''
    <h1>you may not believe me but..</h1>
    <p>i love you till the day that i die...i can breath when you're not here but i can't live! your my first love, the love of my life, my girl.. my only one:) please stay with me..</p>
    <a href="/">بازگشت به صفحه اصلی</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)