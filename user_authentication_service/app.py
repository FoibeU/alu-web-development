from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Assuming AUTH is an instance of the Auth class which handles user authentication
AUTH = Auth()

@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ GET /profile
      Return:
        - message
    """
    session_id = request.cookies.get('session_id')  # Get the session ID from cookies
    user = AUTH.get_user_from_session_id(session_id)  # Validate the session ID
    
    if user:
        # If the user is found, respond with their email
        return jsonify({"email": user.email}), 200
    else:
        # If the session ID is invalid or user does not exist, respond with 403
        abort(403)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

