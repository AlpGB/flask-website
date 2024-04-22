from flask import Flask,redirect
import random

app = Flask(__name__)

facts_list = [
    'Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.',
    '2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.',
    'Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.',
    '2019 da yapılan bir araştırmaya göre, insanların %60 ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.',
    'Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.',
    'Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.',
    'Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.',
    'Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız.'
]

@app.route("/")#ana sayfa
def sayfa1():
    return '<h1>Random Facts:</h1>' \
           f'<p>{random.choice(facts_list)}</p>' \
           '<a href="/2">2. sayfa    </a>' \
           '<a href="/3">3. sayfa    </a>'

@app.route("/2")#taş kağıt makas
def sayfa2():
    return '<h1>Taş kağıt makas oyna!</h1>' \
           '<a href="/tas">TAŞ    </a>' \
           '<a href="/kagıt">KAĞIT    </a>' \
           '<a href="/makas">MAKAS    </a>' \
           '<a href="/">1. sayfa    </a>' \
           '<a href="/3">3. sayfa</a>'

click_count = 0

@app.route("/3")
def sayfa3():
    global click_count
    return f'''
        <h1>Clicker Simulator</h1>
        <p>Click Count: {click_count}</p>
        <form action="/click" method="post">
            <button type="submit">Click Me!</button>
        </form>
        <a href="/">Sayfa 1    </a>
        <a href="/2">Sayfa 2    </a>
    '''

@app.route("/click", methods=["POST"])
def click():
    global click_count
    click_count += 1
    return redirect("/3")

@app.route("/tas")
def tas():
    bot = random.randint(1,3)
    if bot == 1:
        botunsectigi = 'taş'
    elif bot == 2:
        botunsectigi = 'kağıt'
    elif bot == 3:
        botunsectigi = 'makas'
        
    if botunsectigi == 'taş':
        return '<h1>Berabere</h1>'\
               '<a href="/2">2. sayfa    </a>'
    elif botunsectigi == 'kağıt':
        return '<h1>Kaybettin</h1>'\
               '<a href="/2">2. sayfa    </a>'
    elif botunsectigi == 'makas':
        return '<h1>Kazandın</h1>' \
               '<a href="/2">2. sayfa    </a>'

@app.route("/kagıt")
def kagıt():
    bot = random.randint(1,3)
    if bot == 1:
        botunsectigi = 'taş'
    elif bot == 2:
        botunsectigi = 'kağıt'
    elif bot == 3:
        botunsectigi = 'makas'
        
    if botunsectigi == 'taş':
        return '<h1>Kazandın</h1>'\
               '<a href="/2">2. sayfa    </a>'
    elif botunsectigi == 'kağıt':
        return '<h1>Berabere</h1>'\
               '<a href="/2">2. sayfa    </a>'
    elif botunsectigi == 'makas':
        return '<h1>Kaybettin</h1>' \
               '<a href="/2">2. sayfa    </a>'

@app.route("/makas")
def makas():
    bot = random.randint(1,3)
    if bot == 1:
        botunsectigi = 'taş'
    elif bot == 2:
        botunsectigi = 'kağıt'
    elif bot == 3:
        botunsectigi = 'makas'
        
    if botunsectigi == 'taş':
        return '<h1>Kaybettin</h1>'\
               '<a href="/2">2. sayfa    </a>'
    elif botunsectigi == 'kağıt':
        return '<h1>Kazandın</h1>'\
               '<a href="/2">2. sayfa    </a>'
    elif botunsectigi == 'makas':
        return '<h1>Berabere</h1>' \
               '<a href="/2">2. sayfa    </a>'

    

app.run(debug=True)
