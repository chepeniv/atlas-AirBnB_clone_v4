# UNITTESTING

running all `unittest` in discover mode
```bash
python3 -m unittest discover tests
```

running `unittest` file-by-file
```bash
python3 -m unittest path/to/file/test_file.py
```

running `unittest` with environment variable set-up
```bash
HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd\
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db\
python3 -m unittest discover tests 2> /dev/null
```

running `unittest` from a script
```bash
sudo sh run_unittest.sh
```

