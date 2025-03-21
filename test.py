from langchain_mistralai import ChatMistralAI



model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0
)


print (model.predict("Hello what's up the sky ?"))