from flask import Flask
app = Flask(__name__)

@app.route('/api')
def hello_world():
    return 'Hello,This FLask App!'

'''
data() {
    return {
      msg: ''
    };
  },
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:5000/';
      axios
        .get(path)
        .then(res => {
          this.msg = res.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  created() {
    this.getMessage();
  }
'''