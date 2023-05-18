from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from flask_cors  import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/',methods=['GET'])
def get():
    return jsonify({'msg':'hello world'})

@app.route('/saveProbability',methods=['POST'])
def getProbability():
    cold_count_s = request.json["cold_count_s"];
    flu_count_s =  request.json["flu_count_s"];
    cold_count_ns = request.json["cold_count_ns"];
    flu_count_ns =  request.json["flu_count_ns"];

    total_s = cold_count_s + flu_count_s
    total_ns = cold_count_ns + flu_count_ns
    total_cold =  cold_count_s + cold_count_ns
    total_flu = flu_count_s + flu_count_ns
    
    total_cases = total_cold + total_flu

    cold_joint_mp_s = cold_count_s / total_cases
    flu_joint_mp_s = flu_count_s / total_cases

    cold_joint_mp_ns = cold_count_ns / total_cases
    flu_joint_mp_ns = flu_count_ns / total_cases

    total_joint_mp_s =  cold_joint_mp_s + flu_joint_mp_s
    total_joint_mp_ns = cold_joint_mp_ns + flu_joint_mp_ns

    total_joint_mp_cold = cold_joint_mp_s + cold_joint_mp_ns
    total_joint_mp_flu =  flu_joint_mp_s + flu_joint_mp_ns

    total_joint_mp = total_joint_mp_cold + total_joint_mp_flu

    p_s_con_cold = cold_joint_mp_s / total_joint_mp_cold

    p_cold_con_s = cold_joint_mp_s / total_joint_mp_s

    P_ns_con_cold = cold_joint_mp_ns / total_joint_mp_cold

    p_cold_con_ns = cold_joint_mp_ns / total_joint_mp_ns


    # flu.

    p_s_con_flu = flu_joint_mp_s / total_joint_mp_flu

    p_flu_con_s = flu_joint_mp_s / total_joint_mp_s

    P_ns_con_flu = flu_joint_mp_ns / total_joint_mp_flu

    p_flu_con_ns = flu_joint_mp_ns / total_joint_mp_ns

    
    return jsonify({'total_s':total_s, 'total_ns' : total_ns,'total_cold': total_cold,
                    'total_flu' :total_flu, 'total_cases' : total_cases, 'cold_joint_mp_s': round(cold_joint_mp_s, 4),
                     'flu_joint_mp_s' : round(flu_joint_mp_s, 4), 'cold_joint_mp_ns' : round(cold_joint_mp_ns, 4),
                     'flu_joint_mp_ns' : round(flu_joint_mp_ns, 4), 'total_joint_mp_s' : round(total_joint_mp_s, 4),
                     'cold_joint_mp_ns' : round(cold_joint_mp_ns, 4), 'flu_joint_mp_ns' : round(flu_joint_mp_ns, 4),
                     'total_joint_mp_s' : round(total_joint_mp_s, 4) , 'total_joint_mp_ns': round(total_joint_mp_ns,4),
                     'total_joint_mp_cold' : round(total_joint_mp_cold, 4), 'total_joint_mp_flu' : round(total_joint_mp_flu, 4),
                     'p_s_con_cold': round(p_s_con_cold, 4), 'p_cold_con_s' : round(p_cold_con_s, 4), 'P_ns_con_cold' : round(P_ns_con_cold, 4),
                     'p_cold_con_ns': round(p_cold_con_ns, 4),  'p_s_con_flu' : round(p_s_con_flu, 4), 
                     'p_flu_con_s' : round(p_flu_con_s, 4), 'P_ns_con_flu' : round(P_ns_con_flu, 4) , 'p_flu_con_ns' : round(p_flu_con_ns, 4), 'total_joint_mp': round(total_joint_mp,4)});


if __name__ == "__main__":
    app.run()    
