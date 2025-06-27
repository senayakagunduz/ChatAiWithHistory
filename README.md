# ChatAiWithHistory
 ## true olduğu sürece cevap verecek, 
## düşünecek kısa bir süre sonra tüm cevabı yazdıracak
   
    if __name__ == '__main__':
    while True:
        user_input = input("> ")
        if user_input.lower() in {"exit", "quit"}:
            break
        response = with_message_history.invoke(
            input=[HumanMessage(content=user_input)],
            config=config
        )
        print(response.content)
### Eğer chatGpt gibi cümle cümle yazsın , hepsini aynı anda yazmasın istersen aşağıdaki gibi yazmalısın
### stream kullandığımda bu sorunu aşabiliyorum
    while True:
        user_input = input(">")
        for r in with_message_history.stream(
                input=[
                    HumanMessage(content=user_input)
                ],
                config=config
        ): print(r.content, end=" ")