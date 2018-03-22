## amps-blog-easy-http-auth

This repository contains artifacts for the 2018 blog article on easy HTTP authentication and entitlements.

This is a simple project that demonstrates how to use AMPS with
the `libamps_http_entitlement` module in order to provide authentication
and/or entitlements via web service.

A detailed description of the `libamps_http_entitlement` module is available here: http://devnull.crankuptheamps.com/documentation/html/5.2.0.0/user-guide/html/chapters/auxiliary_modules.html#configuring-amps-to-use-web-service-authentication-and-entitlements


### Requirements

- AMPS Server 5.2 or higher
- Python 2.7 or higher


### Quick Start

- Start the AMPS Server using the configuration file:

    ```bash
    <PATH_TO_AMPS_BINARY>/ampServer config.xml
    ```

- Start the Python Flask application (in the `auth` directory):

    ```
    python main.py
    ```

- Open the Galvanometer Web interface with your favorite browser. It's available at this URL: `http://localhost:8085`
  In the login/password window enter: `mylogin` and `mypass`

- Try to subscribe to a topic using `Spark`:

    ```bash
    <PATH_TO_AMPS_BINARY>/spark subscribe -server mylogin:mypass@localhost:9007 -topic foo -type json
    ```


### Miscellaneous

Want to know more about how AMPS can help you build great applications? Still having trouble getting AMPS to play your tune? For help or questions, send us a note at support@crankuptheamps.com.
