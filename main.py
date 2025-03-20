from src.views import *
from src.models import *

def main():
    create_default_user()
    app = MainWindow()
    app.run()

if __name__ == '__main__':
    main()