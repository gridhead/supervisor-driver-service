<p align="center">
  <img width="15%" src="https://raw.githubusercontent.com/t0xic0der/supervisor-driver-service/a720542ac78d51a3c7426b7f41e6798202c931c3/pictures/mainicon.svg" />
</p>

<h1 align="center">SuperVisor</h1>
<h3 align="center">Driver Service</h3>
<p align="center">Reference driver endpoint service written in Falcon, Werkzeug, Psutil and Docker</p>

<p align="center">
    <img src="https://raw.githubusercontent.com/veggiemonk/awesome-docker/master/badge.svg">
    <img src="https://camo.githubusercontent.com/e5d3197f63169393ee5695f496402136b412d5e3b1d77dc5aa80805fdd5e7edb/68747470733a2f2f617765736f6d652e72652f6d656e74696f6e65642d62616467652e737667">
</p>

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

## In action

![](pictures/drivanim.gif)

**CORRECTION** - The TermSocket URI's protocol text must be `ws` (WebSocket) instead of `http` (HTTP), like it has been 
shown above. Please be sure to make that correction before entering those details in the frontend service.

## Table of contents
1. [Home](https://github.com/t0xic0der/supervisor-driver-service/wiki)
2. [Installation](https://github.com/t0xic0der/supervisor-driver-service/wiki/Installation)
3. [Obtain releases](https://github.com/t0xic0der/supervisor-driver-service/releases)
4. [SuperVisor Frontend Service](https://github.com/t0xic0der/supervisor-frontend-service)

## Contribute
You may request for the addition of new features in the 
[issues](https://github.com/t0xic0der/supervisor-driver-service/issues) page but as the project is singlehandedly 
maintained - it might take time to develop on them. Please consider forking the repository and contributing to its 
development.
