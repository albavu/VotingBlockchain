from app import app
import sys

if __name__ == "__main__":

    """
    se ejecuta como python run.py localhost 5000 192.168.1.67 5000 True
    """
    app.run(host=sys.argv[1],port=sys.argv[2])