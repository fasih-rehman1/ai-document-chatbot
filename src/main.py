from config import Config 

def main():
    print("=" * 50)
    print(Config.APP_NAME)
    print("=" * 50)
    print(f"Model : {Config.MODEL_NAME}")
    print(f"Debug : {Config.DEBUG}")
    print("=" * 50)


if __name__ == "__main__":
    main()