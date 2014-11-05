#!/usr/bin/env python
from ngptf import app

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')