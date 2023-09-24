import openai

prompt = open("prompt.txt").read()

class Compiler(object):
    api_key = ""
    API_Base = "https://api.openai.com/v1/chat/completions"
    
    def __init__(key=None, base=None, model=None):
        if key:
            self.api_key = key
            openai.api_key = key
        elif os.getenv("OPENAI_API_KEY"):
            key = os.getenv("OPENAI_API_KEY")
            self.api_key = key
            openai.api_key = key
        else:
            raise RuntimeError("No api_key")
        
        self.availableModels = []
        if base:
            openai.api_base = base
        
        try:
            rst = openai.Moedel.list()
            for m in rst["data"]: self.availableModels.append(m["id"])
        except Exception as e:
            print("OPENAI API rerurned a error. Please check your api_key or api_base") 
            raise e
        
        if len(self.availableModels) == 0:
            raise RuntimeError("No available model")
        
        while True:
            if model and not model in self.availableModels:
                raise RuntimeError(f"No access to model \"{model}\"")
            
            if not model:
                print("No model was selected, please choose one")
                print("===========> Available Models:")
                print([x+"\n" for x in self.availableModels])
                model = input("You choose(input full name):")
                continue
            break
    
    def compile(code):
        response = openai.ChatCompletion.create(
        model=self.model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content":code}
        ]
        )