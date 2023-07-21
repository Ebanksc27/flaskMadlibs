from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

#Routes
@app.route('/')
def home():
    # List of words required by the story
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)

# Route to display resulting story
@app.route('/story', methods=['POST'])
def generate_story():
    # user submitted answers from form
    answers = {}
    for prompt in story.prompts:
        # Use prompt as key to access users answer 
        user_answer = request.form.get(prompt)
        # Add users answer to asnwers dict
        answers[prompt] = user_answer

    # Generate story 
    generated_story = story.generate(answers)

    # Display resulting story
    return render_template('story.html', story=generated_story)

if __name__ == '__main__':
    app.run(debug=True)