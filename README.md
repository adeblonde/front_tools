# Front Tools

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