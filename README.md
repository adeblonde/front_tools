# Front Tools

## Swagger REST API

The swagger of the API is defined in `swagger/swagger.yml`.
To generate the code of the associated server in Python-Flask, go to the folder `swagger`, then run :

```bash
./prepare_api.sh
```

It will create a folder of code in `server_swagger`

## Electron template

This template is based on the project [Electron boilerplate](https://github.com/electron-react-boilerplate/electron-react-boilerplate)

You need to have `yarn` installed :

```bash
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update
sudo apt install yarn
```

After cloning the boilerplate, be sure to set the ownership of the repo to your user :

```bash
sudo chown -R YOUR_USERNAME YOUR_TEMPLATE_FOLDER
```

Build :

```
cd your-project-name
yarn
```

Run :

```bash
yarn dev
```

## Running both front and back

In a first console, run

```bash
cd electron-template
yarn dev
```

In another console, run

```bash
cd server_swagger/api
pip3 install -r requirements.txt
python3 -m swagger_server
```

Then use the Electron app
