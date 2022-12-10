from decouple import config
import openai

openai.api_key = config('OPENAI_API_KEY')


def getAnswer(question):
    startQuestion = "Q: "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=startQuestion+question,
        temperature=0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print('response:', response.choices[0].text)
    return response.choices[0].text


def handler(request, jsonify):
    # Get the request body
    body = request.get_json()
    print('body:', body)
    
    # Get the question
    try:
        question = body['question']
        print('question:', question)
    except:
        return jsonify({
            'message': 'Question is required'
        }), 422
    
    # Get the answer
    answer = getAnswer(question)
    
    # replace all \n with blank
    # answer = answer.replace('\n', '')

    # replace all A: with blank
    answer = answer.replace('A: ', '')
    
    print('answer:', answer)

    result = {
        'message': 'Success',
        'answer': answer
    }

    return jsonify(result), 200
