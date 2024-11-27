# Web Framework

## Resources

- [medium: what are web-frameworks](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb)
- [flask quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)
- [jinja template designer](https://jinja.palletsprojects.com/en/stable/templates/)
- [flask portal](https://palletsprojects.com/projects/flask/)

## Objectives

- what is a web framework
- how to build a web framework with flask
- how to define routes in flask
- what is a route
- how to handle variables in a route
- what is a template
- how to create an html response in flask with a template
- how to create a dynamic template
- how to display html data from an sql database

## Requirements

### html and css

- css files go in the `styles/` directory
- image files go in the `images/` directory
- neither the use of `!important` nor `id` are allowed (`#...` in css)
- all tags must be uppercase
- "no cross browsers"

## Issues

"If you get Flask errors after executing the curl ... commands, it might be because of the DEFAULT CHARSET. If it’s DEFAULT CHARSET=latam1, you might want to change it to DEFAULT CHARSET=utf8mb4, either on the server’s config file (/etc/mysql/my.cnf commonly) orm on the CREATE DATABASE statement."

## Flask

`$ pip3 install Flask`

if the following error is raised
```
 - [Got]
rpc error: code = 2 desc = oci runtime error: exec failed: container_linux.go:290: starting container process caused "process_linux.go:111: decoding init error from pipe caused \"read parent: connection reset by peer\""


(222 chars long)
```
then try setting the flask configuration `debug` to `False`

## Manual Review

request a peer review upon completion of this project (and before the deadline).
if no peers have been reviewed then request a review from a TA or staff instead.
