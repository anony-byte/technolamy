from flask import Flask, render_template, request, url_for, redirect
import sys
sys.path.append('/Users/bhargavd/Desktop/project/technolamy/hashtag_maker')
sys.path.append('/Users/bhargavd/Desktop/project/technolamy')
sys.path.append('/Users/bhargavd/Desktop/project/technolamy/image_filter')

from hashtag_maker import hashtag


app = Flask(__name__, template_folder='templates')

details = {'phone_name': 'MOTO G42',
           'price': '12999INR',
           'pros': ['120Hz Amoled Display', '120Hz Amoled Display Super Clarity'
                    , 'Snapdragon 8GEN1 Processor', '5000mAh battery, 80W fast charge',
                    '120Hz Amoled Display', '120Hz Amoled Display'],
           'cons': ['120Hz Amoled Display', 'Bloatware', 'Snapdragon 8GEN1 processor'],
           'recommended': 'HIGHLY RECOMMENDED',
           'verdict': 'This is the best phone ever made. Can be recommended to everyone'
           }


def make_list(points):
    return points.split("\n")


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        global details
        details = {'phone_name': request.form.get("phone_name"),
                   'price': request.form.get("price"),
                   'pros': make_list(request.form.get('pros')),
                   'cons': make_list(request.form.get('cons')),
                   'recommended': request.form.get("recommended"),
                   'verdict': request.form.get("verdict")
                   }
        return redirect(url_for('home'))
    return render_template('form.html')


@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        all_hashtags = hashtag.HashTagMaking.str_to_list(request.form.get("hashtags"))
        print(all_hashtags)
        return redirect(url_for('done'))
    hashtags = hashtag.HashTagMaking(details).all_hashtags()
    return render_template('final.html', details=details, hashtags=hashtags)


@app.route('/done')
def done():
    return 'Thankyou! your form has been submitted'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
