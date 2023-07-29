<a href="https://www.buymeacoffee.com/metimol"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee :)&emoji=&slug=metimol&button_colour=FFDD00&font_colour=000000&font_family=Lato&outline_colour=000000&coffee_colour=ffffff" /></a>

### Hello everyone!

Specify what you want it to build, the AI asks for clarification, and then builds it.

#### Free-GPT-Engineer is made to be easy to adapt, extend, and make your agent learn how you want your code to look. It generates an entire codebase based on a prompt.
It **absolutely FREE.** You don't need to using Openai API Key.

This project based on the [GPT-Engineer repository](https://github.com/AntonOsika/gpt-engineer), version **0.0.7**

## Usage

For installing **Free-GPT-Engineer** run this commands:
- `git clone https://github.com/metim0l/free-gpt-engineer.git`
- `cd free-gpt-engineer`
- `pip install -r requirements.txt`
- Open [this website](https://api.chatanywhere.cn/v1/oauth/free/github/render) and login with your GitHub account.
- Open file `key.json` and paste API key from website to `api_key` variable.


**RUN WITH FRONTEND** (Tested on Ubuntu 22.04.2 LTS)
- Run command `python3 freegptmanager.py`
- Press Delete Files
- Press Create
- Edit Prompt
- And start script
- Export and renew 


**RUN WITHOUT FRONTEND**:
- Create an empty folder inside the repo, in **projects** folder.
- Fill in the `prompt` file in your new folder
- Run command `python main.py projects/new_folder`

**Results**
- Check the generated files in `projects/my-new-project/workspace`
