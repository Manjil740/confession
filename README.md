
# Its just a little webpage i made to show someone to show something

## how to use it? heres step by step guide on how i use it

## Download ngrok from its official site and follow instructions
### for windows:
```bash
https://dashboard.ngrok.com/get-started/setup/windows
```

## for linux 

```bash
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
  && echo "deb https://ngrok-agent.s3.amazonaws.com bookworm main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list \
  && sudo apt update \
  && sudo apt install ngrok
```
authenticate it via 
```bash
ngrok config add-authtoken $YOUR_AUTHTOKEN
```

after these step 

## how to setup 
### for linux
```bash
git clone https://github.com/Manjil740/confession.git
cd confession
python3 -m venv venv
source venv/bin/activate
pip3 install flask
python3 main.py
```

### for windows
#### download the zip file by clicking code or use the clone command
```bash
git clone https://github.com/Manjil740/confession.git
```
#### after that
```bash
cd confession #or open the terminal in same directory as the confession folder is located
pip install flask
python main.py
```

## Then in a different terminal

```bash
ngrok http 5000
```

# Thanks for checking my repo please star it if you like it
