from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/smart_budget', methods=['GET'])
def expose_endpoint():
    return jsonify({
       "smart_budget": 40,
       "updated": False,
       "spending_status": 2
       })

@app.route('/ref_status', methods=['GET'])
def expose_ref_status():
   return jsonify({
      'first_ref_status': 'done',
      'second_ref_status': 'done'
   })

@app.route('/initial_status', methods=['GET'])
def expose_initial_status():
   return jsonify({
      'saving_predictions': 5250,
      'saving_rate_increase': 3
   })

@app.route('/referral_code', methods=['POST'])
def submit_code():
    try:
        # Ensure that the request contains JSON data
        if request.is_json:
            data = request.get_json()
            code = data.get('code')
            if not code:
                return jsonify({"error": "No code provided"}), 400
            print(f"Received code: {code}")
            return jsonify({"code_referral": 1}), 200
        else:
            return jsonify({"error": "Invalid content type, expecting application/json"}), 400
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/referral_code_confirmation', methods=["GET"])
def referral_code_confirmation():
   return jsonify({'confirmation': 1})

@app.route('/user_name', methods=['POST'])
def user_name():
    try:
        # Ensure that the request contains JSON data
        if request.is_json:
            data = request.get_json()
            code = data.get('user_name')
            if not code:
                return jsonify({"error": "No code provided"}), 400
            print(f"Received user_name: {code}")
            return jsonify({"message": "user_name received and printed to console"}), 200
        else:
            return jsonify({"error": "Invalid content type, expecting application/json"}), 400
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
    
@app.route('/saving_capacity', methods=['POST'])
def saving_capacity():
    try:
        # Ensure that the request contains JSON data
        if request.is_json:
            data = request.get_json()
            code = data.get('saving_capacity')
            if not code:
                return jsonify({"error": "No saving provided"}), 400
            print(f"Received user_name: {code}")
            return jsonify({"message": "saving capacity received and printed to console"}), 200
        else:
            return jsonify({"error": "Invalid content type, expecting application/json"}), 400
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/plaid_status', methods=["GET"])
def plaid_status():
   return jsonify({'ok': 1})

@app.route('/get_ref_code', methods=["GET"])
def get_ref_code():
   return jsonify({'code': 1717})

@app.route('/user_behavior', methods=["GET"])
def user_behavior():
   return jsonify({'value': 1})

@app.route('/thirty_saving_prog', methods=["GET"])
def thirty_saving_prog():
   return jsonify({'value': 0.56})

@app.route('/thirty_saving', methods=["GET"])
def thirty_saving():
   return jsonify({'value': 5600})

@app.route('/list_goals', methods=['GET'])
def list_goal():
    return jsonify({'goals': ['1', '2']})

@app.route('/new_goal', methods=['POST'])
def new_goal():
    try:
        # Ensure that the request contains JSON data
        if request.is_json:
            data = request.get_json()
            code = data.get('goal')
            if not code:
                return jsonify({"error": "No saving provided"}), 400
            print(f"Received user_name: {code}")
            return jsonify({"message": "goal received and printed to console"}), 200
        else:
            return jsonify({"error": "Invalid content type, expecting application/json"}), 400
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
    
@app.route('/check_eta', methods=['GET'])
def check_eta():
    return jsonify({'eta': 1})

@app.route('/check_goal', methods=['GET'])
def check_goal():
  try:
          # Ensure that the request contains JSON data
      if request.is_json:
          data = request.get_json()
          code = data.get('goal')
          if not code:
              return jsonify({"error": "No saving provided"}), 400
          print(f"Received user_name: {code}")
          return jsonify({"confirmation":1}), 200
      else:
          return jsonify({"error": "Invalid content type, expecting application/json"}), 400
  except Exception as e:
      print(f"Error: {e}")
      return jsonify({"error": str(e)}), 500
  
@app.route('/get_eta', methods=['GET'])
def get_eta():
  try:
          # Ensure that the request contains JSON data
      if request.is_json:
          data = request.get_json()
          code = data.get('goal')
          if not code:
              return jsonify({"error": "No goal provided"}), 400
          print(f"Received user_name: {code}")
          return jsonify({"eta":"2024-05-01"}), 200
      else:
          return jsonify({"error": "Invalid content type, expecting application/json"}), 400
  except Exception as e:
      print(f"Error: {e}")
      return jsonify({"error": str(e)}), 500
          
@app.route('/cancel_goal', methods=['POST'])
def cancel_goal():
  try:
          # Ensure that the request contains JSON data
      if request.is_json:
          data = request.get_json()
          code = data.get('goal')
          if not code:
              return jsonify({"error": "No goal provided"}), 400
          print(f"Received user_name: {code}")
          return jsonify({"confirmation": 1}), 200
      else:
          return jsonify({"error": "Invalid content type, expecting application/json"}), 400
  except Exception as e:
      print(f"Error: {e}")
      return jsonify({"error": str(e)}), 500
  

@app.route('/delete_account', methods=['POST'])
def delete_account():
  return jsonify({'confirmation': 1})

@app.route('/weekly_audit', methods=['GET'])
def weekly_audit():
    return jsonify({'data': 500})

if __name__ == '__main__':
  print("__main__")
  app.run(host='0.0.0.0', port=5002, debug=True)