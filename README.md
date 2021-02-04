<p align="center">
  <img width="15%" src="https://raw.githubusercontent.com/t0xic0der/supervisor-driver-service/a720542ac78d51a3c7426b7f41e6798202c931c3/pictures/mainicon.svg" />
</p>

<h1 align="center">SuperVisor</h1>
<h3 align="center">Driver Service</h3>
<p align="center">Reference driver endpoint service written in Falcon, Werkzeug, Psutil and Docker</p>

<p align="center">
    <img src="https://img.shields.io/github/issues/t0xic0der/supervisor-driver-service?style=flat-square&logo=appveyor&color=teal">
    <img src="https://img.shields.io/github/forks/t0xic0der/supervisor-driver-service?style=flat-square&logo=appveyor&color=teal">
    <img src="https://img.shields.io/github/stars/t0xic0der/supervisor-driver-service?style=flat-square&logo=appveyor&color=teal">
    <img src="https://img.shields.io/github/license/t0xic0der/supervisor-driver-service?style=flat-square&logo=appveyor&color=teal">
    <img src="https://img.shields.io/github/watchers/t0xic0der/supervisor-driver-service?style=flat-square&color=teal&logo=appveyor">
</p>

## Note
This project works as an intuitive remotely accessible system performance monitoring and task management service for 
container station servers and headless Raspberry Pi setups where multiple containers are concurrently running and 
require observation, with secure passcode-protected endpoints so that clients can connect via the [SuperVisor Frontend 
Service](https://github.com/t0xic0der/supervisor-frontend-service/) and manage their devices.

## Features
- Zero dependence on pre-rendered template with the use of **DeadSync** to render DOM elements on connection
- Efficient JSON data structure for 100% faster updating with the use of **LiveSync** to refresh DOM contents
- Intuitive endpoints for fetching preliminaries, statistics, logs and process listing for containers
- Intuitive endpoints for fetching preliminaries and revision histories for images
- Intuitive endpoints for fetching preliminaries for both networks and volumes
- Relatively low overhead from the server during live stat (approx. 2MB over Python 3 runtime usage)
- Live polling time period is left at client-side decision to stick to a simple client-server model
- Monitoring station information is provided by the awesome **`psutil`** library
- Monitoring and management Docker information is provided by the effective **`docker-py`** library
- Added protection using passcode verification parameter check and server-side authentication of data requests
- Decoupled structure allows for connection to frontend service ([Check here](https://github.com/t0xic0der/supervisor-frontend-service))
- Authenticated process management endpoints - **`TERMINATE`**, **`KILL`**, **`SUSPEND`** and **`RESUME`** ops
- Rewritten entirely in Falcon WSGI and Werkzeug HTTP server to emphasise on speed, efficiency and cleaner code

## Table of contents
1. [Home](https://github.com/t0xic0der/supervisor-driver-service/wiki)
2. [Installation](https://github.com/t0xic0der/supervisor-driver-service/wiki/Installation)
3. [Download releases](https://github.com/t0xic0der/supervisor-driver-service/releases)
4. [SuperVisor Frontend Service](https://github.com/t0xic0der/supervisor-frontend-service)

## Contribute
You may request for the addition of new features in the [issues](https://github.com/t0xic0der/supervisor-driver-service/issues) 
page but as the project is singlehandedly maintained - it might take time to develop on them. Please consider forking 
the repository and contributing to its development. :heart:
