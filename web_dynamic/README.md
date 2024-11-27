# AirBnB clone v4 - Web dynamic

## resources

- [jquery tutorial](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
- [$(document).ready()](https://learn.jquery.com/using-jquery-core/document-ready/)
- [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

## objectives

- how to request your own api
- how to modify an html element style and content
- how to modify the dom
- hot to make `GET` and `POST` request with jquery ajax
- how to to listen and bind to dom and user events

## requirements

- javascript should be semistandard compliant
	- `semistandard *.qs --global`
- all `*.js` files should be in `scripts`
- use jquery v3.x
- `var` is not allowed
- html should not reload for each action

## info

```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

### Flasgger

install [flasgger](https://pypi.org/project/flasgger/) before starting the REST
API

[flasgger github](https://github.com/flasgger/flasgger)

```sh
$ sudo apt-get install -y python3-lxml
$ sudo pip3 install flask_cors # if it was not installed yet
$ sudo pip3 install flasgger
```

#### troubleshooting

##### `jsonschema` exception

```sh
$ sudo pip3 uninstall -y jsonschema
$ sudo pip3 install jsonschema==3.0.1
```

##### `No module named 'pathlib2'` exception

```sh
$ sudo pip3 install pathlib2
```

### Vagrant

in the `Vagrantfile` add this line for each port forwarded

```
# I expose the port 5001 of my vm to the port 5001 on my computer
config.vm.network :forwarded_port, guest: 5001, host: 5001
```

to expose other ports use the same line but replace the 'guest port' and your
'host port'

use the AirBnB API with the port `5001`

## Manual Review

project may require manual review
