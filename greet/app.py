from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
  """ Welcome Message"""
  return "welcome"

@app.route('/welcome/home')
def welcome_home():
  """ Home Page """
  return "Welcome home"

@app.route('/welcome/back')
def welcome_back():
  """ Welcome Back Page """
  return "Welcome back"