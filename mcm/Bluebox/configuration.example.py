# -*- coding: utf-8 -*-
""" 
	Project Bluebox 
	
	Copyright (C) <2015> <University of Stuttgart>
	
	This software may be modified and distributed under the terms
	of the MIT license.  See the LICENSE file for details.
"""
import logging, os

"""
###############################################################################
	Log level setting
###############################################################################
"""
# log_level = logging.CRITICAL
# log_level = logging.ERROR
log_level = logging.WARNING
# log_level = logging.INFO
# log_level = logging.DEBUG

"""
################################################################################
You can set the "default tenant" of the login page here:
Bluebox/angular/modules/login/loginController.js
it's hardcoded as a default there
################################################################################
"""

"""
################################################################################
Server / runtime config
################################################################################
"""

"""
this is the socket that the "dev" runner will listen on.
VCAP_APP_* variables are used in cloudfoundry environments; the second parameter is the fallback which will be used normally
note that with this config, the DEV runner is only locally visible. Only the PROD runner listening on 0.0.0.0 will be accessible form th eoutside
"""
netPortDev = 8000
netHostDev = "127.0.0.1"

netPortProd = 8000
netHostProd = "0.0.0.0"

"""
################################################################################
define the Swift server connection below:
localhost:3000 is the default for the SDOS API proxy.
here we assume that auth/store run on the same host/port. this is true with SDOS
 as well as swift-all-in-one setups.
 If bluebox is directly connected to Swift (without SDOS proxy) then you may need
 to configure two different endpoints below
################################################################################
"""

swift_host = os.getenv("SWIFT_HOST", "localhost")
swift_port = os.getenv("SWIFT_PORT", 3000)

swift_auth_url = "http://{}:{}/auth/1.0".format(swift_host, swift_port)
swift_store_url_valid_prefix = "http://{}:{}/v1/AUTH_".format(swift_host, swift_port)
swift_auth_version = "1.0"

# SDOS on localhost example
# swift_auth_url = "http://localhost:3000/v2.0"
# swift_store_url_valid_prefix = "http://localhost:3000/v1/AUTH_"
# swift_auth_version = "2.0"

# local docker CEPH
# swift_auth_url = "http://172.18.0.22/auth/1.0"
# swift_store_url_valid_prefix = "http://172.18.0.22/swift/v1"
# swift_auth_version = "1.0"

"""
################################################################################
Kafka bootstrap broker for messaging / Task setup
################################################################################
"""
kafka_host = os.getenv("KAFKA_HOST", "localhost")
kafka_port = os.getenv("KAFKA_PORT", 9092)

kafka_broker_endpoint = "{}:{}".format(kafka_host, kafka_port)

"""
################################################################################
used by Analytics. Endpoint of the metadata warehouse PostgreSQL db
################################################################################
"""
postgres_host = os.getenv("POSTGRES_HOST", "localhost")
postgres_port = os.getenv("POSTGRES_PORT", 5432)

metadata_warehouse_endpoint = {
    "database": "mcm_metadata_{}",
    "user": "postgres",
    "password": "passw0rd",
    "host": postgres_host,
    "port": postgres_port
}

"""
################################################################################
used by Analytics. Please provide the URL that points to the Node-RED root.
################################################################################
"""
nodered_host = os.getenv("NODERED_HOST", "localhost")
nodered_port = os.getenv("NODERED_PORT", 1880)

nodered_url = "http://{}:{}".format(nodered_host, nodered_port)
