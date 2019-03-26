# Front Tools

## Swagger REST API

The swagger of the API is defined in `swagger/swagger.yml`.
To generate the code of the associated server in Python-Flask, go to the folder `swagger`, then run :

```bash
./prepare_api.sh
```

It will create a folder of code in `server_swagger`

You can run locally the Flask REST API using the following command :

```bash
cd PATH_TO_SERVER_FOLDER
python3 -m swagger_server
```

You can then test you server from another console :

```bash
curl -X GET http://localhost:8080/v1/answers
curl -H "Content-Type: application/json" -X POST -d '{"id":1,"name":"test_name","content":"test_content"}' http://localhost:8080/v1/answers
```

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

## Adding new pages to the app

add the new route in `app/constants/routes.json` :

```json
{
	"NEWPAGE" : "/newpage"
}
```

add the new container in `app/containers/NewPage.js`

add the new route to the Router in `Routes.js` :

```js
import NewPage from './container/NewPage';

export default () => (
  <App>
    <Switch>
      <Route path={routes.NEWPAGE} component={NewPage} />
      <Route path={routes.HOME} component={HomePage} />
    </Switch>
  </App>
);
```