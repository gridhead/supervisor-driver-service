
import docker
client = docker.DockerClient(base_url="unix://var/run/docker.sock")

# Printing client information
print(client.info())

# SAMPLE OUTPUT
'''
{
    "ID": "NRDM:32DL:WQOD:IQYR:JKZK:NC62:O3NW:SYNN:YLVM:QANM:7MSW:F4F3",
    "Containers": 6,
    "ContainersRunning": 6,
    "ContainersPaused": 0,
    "ContainersStopped": 0,
    "Images": 23,
    "Driver": "devicemapper",
    "DriverStatus": [
        [
            "Pool Name",
            "docker-179:2-1049372-pool"
        ],
        [
            "Pool Blocksize",
            "65.54kB"
        ],
        [
            "Base Device Size",
            "10.74GB"
        ],
        [
            "Backing Filesystem",
            "ext4"
        ],
        [
            "Udev Sync Supported",
            "true"
        ],
        [
            "Data file",
            "/dev/loop0"
        ],
        [
            "Metadata file",
            "/dev/loop1"
        ],
        [
            "Data loop file",
            "/var/lib/docker/devicemapper/devicemapper/data"
        ],
        [
            "Metadata loop file",
            "/var/lib/docker/devicemapper/devicemapper/metadata"
        ],
        [
            "Data Space Used",
            "9.043GB"
        ],
        [
            "Data Space Total",
            "107.4GB"
        ],
        [
            "Data Space Available",
            "13.74GB"
        ],
        [
            "Metadata Space Used",
            "25.44MB"
        ],
        [
            "Metadata Space Total",
            "2.147GB"
        ],
        [
            "Metadata Space Available",
            "2.122GB"
        ],
        [
            "Thin Pool Minimum Free Space",
            "10.74GB"
        ],
        [
            "Deferred Removal Enabled",
            "true"
        ],
        [
            "Deferred Deletion Enabled",
            "true"
        ],
        [
            "Deferred Deleted Device Count",
            "0"
        ],
        [
            "Library Version",
            "1.02.170 (2020-03-24)"
        ]
    ],
    "Plugins": {
        "Volume": [
            "local"
        ],
        "Network": [
            "bridge",
            "host",
            "ipvlan",
            "macvlan",
            "null",
            "overlay"
        ],
        "Authorization": null,
        "Log": [
            "awslogs",
            "fluentd",
            "gcplogs",
            "gelf",
            "journald",
            "json-file",
            "local",
            "logentries",
            "splunk",
            "syslog"
        ]
    },
    "MemoryLimit": true,
    "SwapLimit": true,
    "KernelMemory": true,
    "KernelMemoryTCP": true,
    "CpuCfsPeriod": true,
    "CpuCfsQuota": true,
    "CPUShares": true,
    "CPUSet": true,
    "PidsLimit": true,
    "IPv4Forwarding": true,
    "BridgeNfIptables": true,
    "BridgeNfIp6tables": true,
    "Debug": false,
    "NFd": 112,
    "OomKillDisable": true,
    "NGoroutines": 132,
    "SystemTime": "2021-01-28T16:40:53.758454556Z",
    "LoggingDriver": "json-file",
    "CgroupDriver": "cgroupfs",
    "CgroupVersion": "1",
    "NEventsListener": 0,
    "KernelVersion": "5.10.10-1-ARCH",
    "OperatingSystem": "Arch Linux ARM",
    "OSVersion": "",
    "OSType": "linux",
    "Architecture": "aarch64",
    "IndexServerAddress": "https://index.docker.io/v1/",
    "RegistryConfig": {
        "AllowNondistributableArtifactsCIDRs": [],
        "AllowNondistributableArtifactsHostnames": [],
        "InsecureRegistryCIDRs": [
            "127.0.0.0/8"
        ],
        "IndexConfigs": {
            "docker.io": {
                "Name": "docker.io",
                "Mirrors": [],
                "Secure": true,
                "Official": true
            }
        },
        "Mirrors": []
    },
    "NCPU": 4,
    "MemTotal": 4017565696,
    "GenericResources": null,
    "DockerRootDir": "/var/lib/docker",
    "HttpProxy": "",
    "HttpsProxy": "",
    "NoProxy": "",
    "Name": "alarm",
    "Labels": [],
    "ExperimentalBuild": false,
    "ServerVersion": "20.10.2",
    "Runtimes": {
        "io.containerd.runc.v2": {
            "path": "runc"
        },
        "io.containerd.runtime.v1.linux": {
            "path": "runc"
        },
        "runc": {
            "path": "runc"
        }
    },
    "DefaultRuntime": "runc",
    "Swarm": {
        "NodeID": "",
        "NodeAddr": "",
        "LocalNodeState": "inactive",
        "ControlAvailable": false,
        "Error": "",
        "RemoteManagers": null
    },
    "LiveRestoreEnabled": false,
    "Isolation": "",
    "InitBinary": "docker-init",
    "ContainerdCommit": {
        "ID": "269548fa27e0089a8b8278fc4fc781d7f65a939b.m",
        "Expected": "269548fa27e0089a8b8278fc4fc781d7f65a939b.m"
    },
    "RuncCommit": {
        "ID": "ff819c7e9184c13b7c2607fe6c30ae19403a7aff",
        "Expected": "ff819c7e9184c13b7c2607fe6c30ae19403a7aff"
    },
    "InitCommit": {
        "ID": "de40ad0",
        "Expected": "de40ad0"
    },
    "SecurityOptions": [
        "name=seccomp,profile=default"
    ],
    "Warnings": [
        "WARNING: No blkio weight support",
        "WARNING: No blkio weight_device support",
        "WARNING: the devicemapper storage-driver is deprecated, and will be removed in a future release.",
        "WARNING: devicemapper: usage of loopback devices is strongly discouraged for production use.\n         Use `--storage-opt dm.thinpooldev` to specify a custom block storage device."
    ]
}
'''

# Printing version information
print(client.version())

# SAMPLE OUTPUT

'''
{
    "Platform": {
        "Name": ""
    },
    "Components": [
        {
            "Name": "Engine",
            "Version": "20.10.2",
            "Details": {
                "ApiVersion": "1.41",
                "Arch": "arm64",
                "BuildTime": "2021-01-19T19:14:01.000000000+00:00",
                "Experimental": "false",
                "GitCommit": "8891c58a43",
                "GoVersion": "go1.15.6",
                "KernelVersion": "5.10.10-1-ARCH",
                "MinAPIVersion": "1.12",
                "Os": "linux"
            }
        },
        {
            "Name": "containerd",
            "Version": "v1.4.3",
            "Details": {
                "GitCommit": "269548fa27e0089a8b8278fc4fc781d7f65a939b.m"
            }
        },
        {
            "Name": "runc",
            "Version": "1.0.0-rc92",
            "Details": {
                "GitCommit": "ff819c7e9184c13b7c2607fe6c30ae19403a7aff"
            }
        },
        {
            "Name": "docker-init",
            "Version": "0.19.0",
            "Details": {
                "GitCommit": "de40ad0"
            }
        }
    ],
    "Version": "20.10.2",
    "ApiVersion": "1.41",
    "MinAPIVersion": "1.12",
    "GitCommit": "8891c58a43",
    "GoVersion": "go1.15.6",
    "Os": "linux",
    "Arch": "arm64",
    "KernelVersion": "5.10.10-1-ARCH",
    "BuildTime": "2021-01-19T19:14:01.000000000+00:00"
}
'''

# Listing running containers
print(client.containers.list())

# Per-container information
j = client.containers.list()[0]
j.id                            # <str>
j.image                         # <image-object>
j.labels                        # <dict>
j.name                          # <str>
j.short_id                      # <str>
j.status                        # <str>
j.logs(stream=False)            # <bytes>
j.logs(stream=False).decode()   # <str>

# SAMPLE OUTPUT

'''
[s6-init] making user provided files available at /var/run/s6/etc...exited 0.
[s6-init] ensuring user provided files have correct perms...exited 0.
[fix-attrs.d] applying ownership & permissions fixes...
[fix-attrs.d] done.
[cont-init.d] executing container initialization scripts...
[cont-init.d] 01-envfile: executing... 
[cont-init.d] 01-envfile: exited 0.
[cont-init.d] 10-adduser: executing... 

-------------------------------------
          _         ()
         | |  ___   _    __
         | | / __| | |  /  \ 
         | | \__ \ | | | () |
         |_| |___/ |_|  \__/


Brought to you by linuxserver.io
-------------------------------------

To support LSIO projects visit:
https://www.linuxserver.io/donate/
-------------------------------------
GID/UID
-------------------------------------

User uid:    1000
User gid:    1000
-------------------------------------

[cont-init.d] 10-adduser: exited 0.
[cont-init.d] 20-config: executing... 
[cont-init.d] 20-config: exited 0.
[cont-init.d] 30-keygen: executing... 
using keys found in /config/keys
[cont-init.d] 30-keygen: exited 0.
[cont-init.d] 50-config: executing... 
New container detected, installing Heimdall
Setting permissions
[cont-init.d] 50-config: exited 0.
[cont-init.d] 99-custom-files: executing... 
[custom-init] no custom files found exiting...
[cont-init.d] 99-custom-files: exited 0.
[cont-init.d] done.
[services.d] starting services
[services.d] done.
[cont-finish.d] executing container finish scripts...
[s6-init] making user provided files available at /var/run/s6/etc...exited 0.
[s6-init] ensuring user provided files have correct perms...exited 0.
[fix-attrs.d] applying ownership & permissions fixes...
[fix-attrs.d] done.
[cont-init.d] executing container initialization scripts...
[cont-init.d] 01-envfile: executing... 
[cont-init.d] 01-envfile: exited 0.
[cont-init.d] 10-adduser: executing... 
usermod: no changes

-------------------------------------
          _         ()
         | |  ___   _    __
         | | / __| | |  /  \ 
         | | \__ \ | | | () |
         |_| |___/ |_|  \__/


Brought to you by linuxserver.io
-------------------------------------

To support LSIO projects visit:
https://www.linuxserver.io/donate/
-------------------------------------
GID/UID
-------------------------------------

User uid:    1000
User gid:    1000
-------------------------------------

[cont-init.d] 10-adduser: exited 0.
[cont-init.d] 20-config: executing... 
[cont-init.d] 20-config: exited 0.
[cont-init.d] 30-keygen: executing... 
using keys found in /config/keys
[cont-init.d] 30-keygen: exited 0.
[cont-init.d] 50-config: executing... 
Setting permissions
[cont-init.d] 50-config: exited 0.
[cont-init.d] 99-custom-files: executing... 
[custom-init] no custom files found exiting...
[cont-init.d] 99-custom-files: exited 0.
[cont-init.d] done.
[services.d] starting services
[services.d] done.
[s6-init] making user provided files available at /var/run/s6/etc...exited 0.
[s6-init] ensuring user provided files have correct perms...exited 0.
[fix-attrs.d] applying ownership & permissions fixes...
[fix-attrs.d] done.
[cont-init.d] executing container initialization scripts...
[cont-init.d] 01-envfile: executing... 
[cont-init.d] 01-envfile: exited 0.
[cont-init.d] 10-adduser: executing... 
usermod: no changes

-------------------------------------
          _         ()
         | |  ___   _    __
         | | / __| | |  /  \ 
         | | \__ \ | | | () |
         |_| |___/ |_|  \__/


Brought to you by linuxserver.io
-------------------------------------

To support LSIO projects visit:
https://www.linuxserver.io/donate/
-------------------------------------
GID/UID
-------------------------------------

User uid:    1000
User gid:    1000
-------------------------------------

[cont-init.d] 10-adduser: exited 0.
[cont-init.d] 20-config: executing... 
[cont-init.d] 20-config: exited 0.
[cont-init.d] 30-keygen: executing... 
using keys found in /config/keys
[cont-init.d] 30-keygen: exited 0.
[cont-init.d] 50-config: executing... 
Setting permissions
[cont-init.d] 50-config: exited 0.
[cont-init.d] 99-custom-files: executing... 
[custom-init] no custom files found exiting...
[cont-init.d] 99-custom-files: exited 0.
[cont-init.d] done.
[services.d] starting services
[services.d] done.
[s6-init] making user provided files available at /var/run/s6/etc...exited 0.
[s6-init] ensuring user provided files have correct perms...exited 0.
[fix-attrs.d] applying ownership & permissions fixes...
[fix-attrs.d] done.
[cont-init.d] executing container initialization scripts...
[cont-init.d] 01-envfile: executing... 
[cont-init.d] 01-envfile: exited 0.
[cont-init.d] 10-adduser: executing... 
usermod: no changes

-------------------------------------
          _         ()
         | |  ___   _    __
         | | / __| | |  /  \ 
         | | \__ \ | | | () |
         |_| |___/ |_|  \__/


Brought to you by linuxserver.io
-------------------------------------

To support LSIO projects visit:
https://www.linuxserver.io/donate/
-------------------------------------
GID/UID
-------------------------------------

User uid:    1000
User gid:    1000
-------------------------------------

[cont-init.d] 10-adduser: exited 0.
[cont-init.d] 20-config: executing... 
[cont-init.d] 20-config: exited 0.
[cont-init.d] 30-keygen: executing... 
using keys found in /config/keys
[cont-init.d] 30-keygen: exited 0.
[cont-init.d] 50-config: executing... 
Setting permissions
[cont-init.d] 50-config: exited 0.
[cont-init.d] 99-custom-files: executing... 
[custom-init] no custom files found exiting...
[cont-init.d] 99-custom-files: exited 0.
[cont-init.d] done.
[services.d] starting services
[services.d] done.
[cont-finish.d] executing container finish scripts...
[cont-finish.d] done.
[s6-finish] waiting for services.
[s6-finish] sending all processes the TERM signal.
[s6-finish] sending all processes the KILL signal and exiting.
[s6-init] making user provided files available at /var/run/s6/etc...exited 0.
[s6-init] ensuring user provided files have correct perms...exited 0.
[fix-attrs.d] applying ownership & permissions fixes...
[fix-attrs.d] done.
[cont-init.d] executing container initialization scripts...
[cont-init.d] 01-envfile: executing... 
[cont-init.d] 01-envfile: exited 0.
[cont-init.d] 10-adduser: executing... 
usermod: no changes

-------------------------------------
          _         ()
         | |  ___   _    __
         | | / __| | |  /  \ 
         | | \__ \ | | | () |
         |_| |___/ |_|  \__/


Brought to you by linuxserver.io
-------------------------------------

To support LSIO projects visit:
https://www.linuxserver.io/donate/
-------------------------------------
GID/UID
-------------------------------------

User uid:    1000
User gid:    1000
-------------------------------------

[cont-init.d] 10-adduser: exited 0.
[cont-init.d] 20-config: executing... 
[cont-init.d] 20-config: exited 0.
[cont-init.d] 30-keygen: executing... 
using keys found in /config/keys
[cont-init.d] 30-keygen: exited 0.
[cont-init.d] 50-config: executing... 
Setting permissions
[cont-init.d] 50-config: exited 0.
[cont-init.d] 99-custom-files: executing... 
[custom-init] no custom files found exiting...
[cont-init.d] 99-custom-files: exited 0.
[cont-init.d] done.
[services.d] starting services
[services.d] done.
'''

j.stats(stream=False)           # <dict>

# SAMPLE OUTPUT

'''
{
    "read": "2021-01-28T16:47:14.57043359Z",
    "preread": "2021-01-28T16:47:13.564934527Z",
    "pids_stats": {
        "current": 16
    },
    "blkio_stats": {
        "io_service_bytes_recursive": [
            {
                "major": 7,
                "minor": 0,
                "op": "Read",
                "value": 47042560
            },
            {
                "major": 7,
                "minor": 0,
                "op": "Write",
                "value": 90112
            },
            {
                "major": 7,
                "minor": 0,
                "op": "Sync",
                "value": 47050752
            },
            {
                "major": 7,
                "minor": 0,
                "op": "Async",
                "value": 81920
            },
            {
                "major": 7,
                "minor": 0,
                "op": "Discard",
                "value": 0
            },
            {
                "major": 7,
                "minor": 0,
                "op": "Total",
                "value": 47132672
            },
            {
                "major": 253,
                "minor": 0,
                "op": "Read",
                "value": 47042560
            },
            {
                "major": 253,
                "minor": 0,
                "op": "Write",
                "value": 90112
            },
            {
                "major": 253,
                "minor": 0,
                "op": "Sync",
                "value": 47050752
            },
            {
                "major": 253,
                "minor": 0,
                "op": "Async",
                "value": 81920
            },
            {
                "major": 253,
                "minor": 0,
                "op": "Discard",
                "value": 0
            },
            {
                "major": 253,
                "minor": 0,
                "op": "Total",
                "value": 47132672
            },
            {
                "major": 253,
                "minor": 2,
                "op": "Read",
                "value": 47042560
            },
            {
                "major": 253,
                "minor": 2,
                "op": "Write",
                "value": 90112
            },
            {
                "major": 253,
                "minor": 2,
                "op": "Sync",
                "value": 47050752
            },
            {
                "major": 253,
                "minor": 2,
                "op": "Async",
                "value": 81920
            },
            {
                "major": 253,
                "minor": 2,
                "op": "Discard",
                "value": 0
            },
            {
                "major": 253,
                "minor": 2,
                "op": "Total",
                "value": 47132672
            },
            {
                "major": 179,
                "minor": 0,
                "op": "Read",
                "value": 2465792
            },
            {
                "major": 179,
                "minor": 0,
                "op": "Write",
                "value": 4096
            },
            {
                "major": 179,
                "minor": 0,
                "op": "Sync",
                "value": 2465792
            },
            {
                "major": 179,
                "minor": 0,
                "op": "Async",
                "value": 4096
            },
            {
                "major": 179,
                "minor": 0,
                "op": "Discard",
                "value": 0
            },
            {
                "major": 179,
                "minor": 0,
                "op": "Total",
                "value": 2469888
            }
        ],
        "io_serviced_recursive": [
            {
                "major": 7,
                "minor": 0,
                "op": "Read",
                "value": 3587
            },
            {
                "major": 7,
                "minor": 0,
                "op": "Write",
                "value": 13
            },
            {
                "major": 7,
                "minor": 0,
                "op": "Sync",
                "value": 3589
            },
            {
                "major": 7,
                "minor": 0,
                "op": "Async",
                "value": 11
            },
            {
                "major": 7,
                "minor": 0,
                "op": "Discard",
                "value": 0
            },
            {
                "major": 7,
                "minor": 0,
                "op": "Total",
                "value": 3600
            },
            {
                "major": 253,
                "minor": 0,
                "op": "Read",
                "value": 3587
            },
            {
                "major": 253,
                "minor": 0,
                "op": "Write",
                "value": 13
            },
            {
                "major": 253,
                "minor": 0,
                "op": "Sync",
                "value": 3589
            },
            {
                "major": 253,
                "minor": 0,
                "op": "Async",
                "value": 11
            },
            {
                "major": 253,
                "minor": 0,
                "op": "Discard",
                "value": 0
            },
            {
                "major": 253,
                "minor": 0,
                "op": "Total",
                "value": 3600
            },
            {
                "major": 253,
                "minor": 2,
                "op": "Read",
                "value": 3137
            },
            {
                "major": 253,
                "minor": 2,
                "op": "Write",
                "value": 13
            },
            {
                "major": 253,
                "minor": 2,
                "op": "Sync",
                "value": 3139
            },
            {
                "major": 253,
                "minor": 2,
                "op": "Async",
                "value": 11
            },
            {
                "major": 253,
                "minor": 2,
                "op": "Discard",
                "value": 0
            },
            {
                "major": 253,
                "minor": 2,
                "op": "Total",
                "value": 3150
            },
            {
                "major": 179,
                "minor": 0,
                "op": "Read",
                "value": 487
            },
            {
                "major": 179,
                "minor": 0,
                "op": "Write",
                "value": 1
            },
            {
                "major": 179,
                "minor": 0,
                "op": "Sync",
                "value": 487
            },
            {
                "major": 179,
                "minor": 0,
                "op": "Async",
                "value": 1
            },
            {
                "major": 179,
                "minor": 0,
                "op": "Discard",
                "value": 0
            },
            {
                "major": 179,
                "minor": 0,
                "op": "Total",
                "value": 488
            }
        ],
        "io_queue_recursive": [],
        "io_service_time_recursive": [],
        "io_wait_time_recursive": [],
        "io_merged_recursive": [],
        "io_time_recursive": [],
        "sectors_recursive": []
    },
    "num_procs": 0,
    "storage_stats": {},
    "cpu_stats": {
        "cpu_usage": {
            "total_usage": 23964363902,
            "percpu_usage": [
                4580207653,
                9390755702,
                4317221070,
                5676179477
            ],
            "usage_in_kernelmode": 3450000000,
            "usage_in_usermode": 20090000000
        },
        "system_cpu_usage": 197655370000000,
        "online_cpus": 4,
        "throttling_data": {
            "periods": 0,
            "throttled_periods": 0,
            "throttled_time": 0
        }
    },
    "precpu_stats": {
        "cpu_usage": {
            "total_usage": 23964330532,
            "percpu_usage": [
                4580207653,
                9390722332,
                4317221070,
                5676179477
            ],
            "usage_in_kernelmode": 3450000000,
            "usage_in_usermode": 20090000000
        },
        "system_cpu_usage": 197651360000000,
        "online_cpus": 4,
        "throttling_data": {
            "periods": 0,
            "throttled_periods": 0,
            "throttled_time": 0
        }
    },
    "memory_stats": {
        "usage": 55132160,
        "max_usage": 61685760,
        "stats": {
            "active_anon": 0,
            "active_file": 6733824,
            "cache": 19329024,
            "dirty": 135168,
            "hierarchical_memory_limit": 9223372036854771712,
            "hierarchical_memsw_limit": 9223372036854771712,
            "inactive_anon": 31764480,
            "inactive_file": 12406784,
            "mapped_file": 8515584,
            "pgfault": 35937,
            "pgmajfault": 1287,
            "pgpgin": 31977,
            "pgpgout": 19517,
            "rss": 31899648,
            "rss_huge": 0,
            "total_active_anon": 0,
            "total_active_file": 6733824,
            "total_cache": 19329024,
            "total_dirty": 135168,
            "total_inactive_anon": 31764480,
            "total_inactive_file": 12406784,
            "total_mapped_file": 8515584,
            "total_pgfault": 35937,
            "total_pgmajfault": 1287,
            "total_pgpgin": 31977,
            "total_pgpgout": 19517,
            "total_rss": 31899648,
            "total_rss_huge": 0,
            "total_unevictable": 0,
            "total_writeback": 135168,
            "unevictable": 0,
            "writeback": 135168
        },
        "limit": 4017565696
    },
    "name": "/heimdall",
    "id": "360340a08b7ab9c5b56788f91474e4b336d2863cd01c7175270e2ef66220f497",
    "networks": {
        "eth0": {
            "rx_bytes": 40111,
            "rx_packets": 426,
            "rx_errors": 0,
            "rx_dropped": 0,
            "tx_bytes": 1102841,
            "tx_packets": 375,
            "tx_errors": 0,
            "tx_dropped": 0
        }
    }
}
'''

j.top()                         # <dict>

'''
{
    "Processes": [
        [
            "root",
            "5463",
            "5445",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "s6-svscan -t0 /var/run/s6/services"
        ],
        [
            "root",
            "5531",
            "5463",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "s6-supervise s6-fdholderd"
        ],
        [
            "root",
            "5812",
            "5463",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "s6-supervise nginx"
        ],
        [
            "root",
            "5813",
            "5463",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "s6-supervise queue"
        ],
        [
            "root",
            "5815",
            "5463",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "s6-supervise php-fpm"
        ],
        [
            "root",
            "5816",
            "5463",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "s6-supervise cron"
        ],
        [
            "alarm",
            "5818",
            "5813",
            "0",
            "04:12",
            "?",
            "00:00:20",
            "php /var/www/localhost/heimdall/artisan queue:work database --sleep=3 --tries=3"
        ],
        [
            "root",
            "5819",
            "5812",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "nginx: master process /usr/sbin/nginx -c /config/nginx/nginx.conf"
        ],
        [
            "root",
            "5820",
            "5816",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "/usr/sbin/crond -f -S -l 5 -c /etc/crontabs"
        ],
        [
            "root",
            "5822",
            "5815",
            "0",
            "04:12",
            "?",
            "00:00:01",
            "php-fpm: master process (/etc/php7/php-fpm.conf)"
        ],
        [
            "alarm",
            "5842",
            "5819",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "nginx: worker process"
        ],
        [
            "alarm",
            "5843",
            "5819",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "nginx: worker process"
        ],
        [
            "alarm",
            "5844",
            "5819",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "nginx: worker process"
        ],
        [
            "alarm",
            "5845",
            "5819",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "nginx: worker process"
        ],
        [
            "alarm",
            "5846",
            "5822",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "php-fpm: pool www"
        ],
        [
            "alarm",
            "5847",
            "5822",
            "0",
            "04:12",
            "?",
            "00:00:00",
            "php-fpm: pool www"
        ]
    ],
    "Titles": [
        "UID",
        "PID",
        "PPID",
        "C",
        "STIME",
        "TTY",
        "TIME",
        "CMD"
    ]
}
'''

# Per-image information
j.image.attrs                   # <dict>

# SAMPLE OUTPUT

'''
{
    "Id": "sha256:c05e909a5a07bf6743bda6406592f9e0d9e9a85a357b2ee32dea6788855e70fe",
    "RepoTags": [
        "linuxserver/heimdall:latest"
    ],
    "RepoDigests": [
        "linuxserver/heimdall@sha256:9cf0002855ab15758dfad10997efab0b388672490711664e5199ec5e5a8e8579"
    ],
    "Parent": "",
    "Comment": "",
    "Created": "2021-01-15T06:34:00.510644721Z",
    "Container": "",
    "ContainerConfig": {
        "Hostname": "",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "ExposedPorts": {
            "443/tcp": {},
            "80/tcp": {}
        },
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "PS1=$(whoami)@$(hostname):$(pwd)\\$ ",
            "HOME=/root",
            "TERM=xterm",
            "S6_BEHAVIOUR_IF_STAGE2_FAILS=2"
        ],
        "Cmd": [
            "/bin/sh",
            "-c",
            "#(nop) COPY dir:50d2f28c52d1224e0c176ad89512b9b0b7daf607120b0723506867dc3122e1fd in / "
        ],
        "Image": "sha256:7070a625aceeb2c60f59767ee415ad6259959b8cf189e62ab3e643cc2b2043c1",
        "Volumes": {
            "/config": {}
        },
        "WorkingDir": "",
        "Entrypoint": [
            "/init"
        ],
        "OnBuild": null,
        "Labels": {
            "build_version": "Linuxserver.io version:- 2.2.2-ls113 Build-date:- 2021-01-15T06:32:32+00:00",
            "maintainer": "aptalca"
        }
    },
    "DockerVersion": "20.10.2",
    "Author": "",
    "Config": {
        "Hostname": "",
        "Domainname": "",
        "User": "",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "ExposedPorts": {
            "443/tcp": {},
            "80/tcp": {}
        },
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "PS1=$(whoami)@$(hostname):$(pwd)\\$ ",
            "HOME=/root",
            "TERM=xterm",
            "S6_BEHAVIOUR_IF_STAGE2_FAILS=2"
        ],
        "Cmd": null,
        "Image": "sha256:7070a625aceeb2c60f59767ee415ad6259959b8cf189e62ab3e643cc2b2043c1",
        "Volumes": {
            "/config": {}
        },
        "WorkingDir": "",
        "Entrypoint": [
            "/init"
        ],
        "OnBuild": null,
        "Labels": {
            "build_version": "Linuxserver.io version:- 2.2.2-ls113 Build-date:- 2021-01-15T06:32:32+00:00",
            "maintainer": "aptalca"
        }
    },
    "Architecture": "arm64",
    "Variant": "v8",
    "Os": "linux",
    "Size": 91338738,
    "VirtualSize": 91338738,
    "GraphDriver": {
        "Data": {
            "DeviceId": "105",
            "DeviceName": "docker-179:2-1049372-f9c76abbb914d6b93d619aa18e24ae6c0a751923ea156fff417b318ff085e3f0",
            "DeviceSize": "10737418240"
        },
        "Name": "devicemapper"
    },
    "RootFS": {
        "Type": "layers",
        "Layers": [
            "sha256:fdf68b32143970fdfe941d96e18001467a4dd37d4411ac5308727bab14f7b03b",
            "sha256:279eb88f2fc871c145bed0f6e7cd6851a01e291906473ba217d98665203dcbb2",
            "sha256:29069ff6494bb13219ea10a6a2cdd19859d887823fbb452f682c9a513c8eb8c4",
            "sha256:127c9d166be9eefea4a3b6189b21d876120bd0ad63416f43c069f93f3ed5d9b4",
            "sha256:f5c574eb12d23251f1922ac794c60da31632a482c612146943b30aa94d4b1699",
            "sha256:2a35d0a1a39469ed203090d46fce3fdd0ebd6db6b7e412d8bea990ed20cd6b2d",
            "sha256:1587025e855779aee1b597ef8647a68549cbcc027cdecf21a1e427f0b029703a",
            "sha256:13a685f575cffbfe02fe9c7639685a87fe47830529c1be0655e516954bca6683",
            "sha256:daff46243e3b2ae85dca4c859a905443fed955c11cd2d5e020b479bd8612eb94"
        ]
    },
    "Metadata": {
        "LastTagTime": "0001-01-01T00:00:00Z"
    }
}
'''

j.image.id                      # <str>

j.image.labels                  # <dict>

# SAMPLE OUTPUT

'''
{
    "build_version": "Linuxserver.io version:- 2.2.2-ls113 Build-date:- 2021-01-15T06:32:32+00:00",
    "maintainer": "aptalca"
}
'''

'''
{
    "org.label-schema.build-date": "20201204",
    "org.label-schema.license": "GPLv2",
    "org.label-schema.name": "CentOS Base Image",
    "org.label-schema.schema-version": "1.0",
    "org.label-schema.vendor": "CentOS"
}
'''

j.image.short_id                # <str>
j.image.tags                    # <list>

# SAMPLE OUTPUT

'''
[
    "centos:code-server"
]
'''

j.image.history()               # <list>

# SAMPLE OUTPUT

'''
[
    {
        "Comment": "",
        "Created": 1611682947,
        "CreatedBy": "/bin/sh -c #(nop)  VOLUME [/config]",
        "Id": "sha256:c7be7c07415c5a1b4e24bf7b13cf0c40dbc9867256d3749c16dc28c3146fb0f3",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611682946,
        "CreatedBy": "/bin/sh -c #(nop)  EXPOSE 1900/udp 3005/tcp 32400/tcp 32410/udp 32412/udp 32413/udp 32414/udp 32469/tcp 5353/udp 8324/tcp",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611682944,
        "CreatedBy": "/bin/sh -c #(nop) COPY dir:54e6f0d31377700bd5ccb5b2a2412b03ca3f924ea0134f6a2098bdcfdbe2a49b in / ",
        "Id": "<missing>",
        "Size": 9922,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611682927,
        "CreatedBy": "|3 BUILD_DATE=2021-01-26T17:39:30+00:00 PLEX_RELEASE=1.21.2.3939-3945797bd VERSION=1.21.2.3939-3945797bd-ls20 /bin/sh -c echo \"**** install runtime packages ****\" &&  apt-get update &&  apt-get install -y \tjq \tudev \tunrar \twget &&  echo \"**** install plex ****\" &&  if [ -z ${PLEX_RELEASE+x} ]; then         PLEX_RELEASE=$(curl -sX GET 'https://plex.tv/api/downloads/5.json'         | jq -r '.computer.Linux.version');  fi &&  curl -o \t/tmp/plexmediaserver.deb -L \t\"${PLEX_DOWNLOAD}/${PLEX_RELEASE}/debian/plexmediaserver_${PLEX_RELEASE}_${PLEX_ARCH}.deb\" &&  dpkg -i /tmp/plexmediaserver.deb &&  echo \"**** ensure abc user's home folder is /app ****\" &&  usermod -d /app abc &&  echo \"**** cleanup ****\" &&  apt-get clean &&  rm -rf \t/etc/default/plexmediaserver \t/tmp/* \t/var/lib/apt/lists/* \t/var/tmp/*",
        "Id": "<missing>",
        "Size": 215721403,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611682852,
        "CreatedBy": "/bin/sh -c #(nop)  ENV DEBIAN_FRONTEND=noninteractive PLEX_DOWNLOAD=https://downloads.plex.tv/plex-media-server-new PLEX_ARCH=arm64 PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR=/config/Library/Application Support PLEX_MEDIA_SERVER_HOME=/usr/lib/plexmediaserver PLEX_MEDIA_SERVER_MAX_PLUGIN_PROCS=6 PLEX_MEDIA_SERVER_USER=abc PLEX_MEDIA_SERVER_INFO_VENDOR=Docker PLEX_MEDIA_SERVER_INFO_DEVICE=Docker Container (LinuxServer.io)",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611682851,
        "CreatedBy": "/bin/sh -c #(nop)  LABEL maintainer=thelamer",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611682849,
        "CreatedBy": "/bin/sh -c #(nop)  LABEL build_version=Linuxserver.io version:- 1.21.2.3939-3945797bd-ls20 Build-date:- 2021-01-26T17:39:30+00:00",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611682848,
        "CreatedBy": "/bin/sh -c #(nop)  ARG PLEX_RELEASE",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611682847,
        "CreatedBy": "/bin/sh -c #(nop)  ARG VERSION",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611682844,
        "CreatedBy": "/bin/sh -c #(nop)  ARG BUILD_DATE",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637837,
        "CreatedBy": "/bin/sh -c #(nop)  ENTRYPOINT [\"/init\"]",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637835,
        "CreatedBy": "/bin/sh -c #(nop) COPY dir:643a650c063c923b6bde607ed6d0259227130c48523761aade9a41628ded66d7 in / ",
        "Id": "<missing>",
        "Size": 14754,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637827,
        "CreatedBy": "|5 BUILD_DATE=2021-01-26T05:05:04+00:00 DEBIAN_FRONTEND=noninteractive OVERLAY_ARCH=aarch64 OVERLAY_VERSION=v2.1.0.2 VERSION=fd2376ac-ls25 /bin/sh -c echo \"**** Ripped from Ubuntu Docker Logic ****\" &&  set -xe &&  echo '#!/bin/sh' \t> /usr/sbin/policy-rc.d &&  echo 'exit 101' \t>> /usr/sbin/policy-rc.d &&  chmod +x \t/usr/sbin/policy-rc.d &&  dpkg-divert --local --rename --add /sbin/initctl &&  cp -a \t/usr/sbin/policy-rc.d \t/sbin/initctl &&  sed -i \t's/^exit.*/exit 0/' \t/sbin/initctl &&  echo 'force-unsafe-io' \t> /etc/dpkg/dpkg.cfg.d/docker-apt-speedup &&  echo 'DPkg::Post-Invoke { \"rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true\"; };' \t> /etc/apt/apt.conf.d/docker-clean &&  echo 'APT::Update::Post-Invoke { \"rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true\"; };' \t>> /etc/apt/apt.conf.d/docker-clean &&  echo 'Dir::Cache::pkgcache \"\"; Dir::Cache::srcpkgcache \"\";' \t>> /etc/apt/apt.conf.d/docker-clean &&  echo 'Acquire::Languages \"none\";' \t> /etc/apt/apt.conf.d/docker-no-languages &&  echo 'Acquire::GzipIndexes \"true\"; Acquire::CompressionTypes::Order:: \"gz\";' \t> /etc/apt/apt.conf.d/docker-gzip-indexes &&  echo 'Apt::AutoRemove::SuggestsImportant \"false\";' \t> /etc/apt/apt.conf.d/docker-autoremove-suggests &&  mkdir -p /run/systemd &&  echo 'docker' \t> /run/systemd/container &&  echo \"**** install apt-utils and locales ****\" &&  apt-get update &&  apt-get install -y \tapt-utils \tlocales &&  echo \"**** install packages ****\" &&  apt-get install -y \tcurl \tgnupg \ttzdata &&  echo \"**** generate locale ****\" &&  locale-gen en_US.UTF-8 &&  echo \"**** create abc user and make our folders ****\" &&  useradd -u 911 -U -d /config -s /bin/false abc &&  usermod -G users abc &&  mkdir -p \t/app \t/config \t/defaults &&  mv /usr/bin/with-contenv /usr/bin/with-contenvb &&  echo \"**** add qemu ****\" &&  curl -o  /usr/bin/qemu-aarch64-static -L \t\"https://lsio-ci.ams3.digitaloceanspaces.com/qemu-aarch64-static\" &&  chmod +x /usr/bin/qemu-aarch64-static &&  echo \"**** cleanup ****\" &&  apt-get clean &&  rm -rf \t/tmp/* \t/var/lib/apt/lists/* \t/var/tmp/*",
        "Id": "<missing>",
        "Size": 49712129,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637710,
        "CreatedBy": "/bin/sh -c #(nop) COPY file:7c0649cb600aa6c72cfc6188617e4e394e832e723897e1fcd0655af5f631ac68 in /etc/apt/ ",
        "Id": "<missing>",
        "Size": 884,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637709,
        "CreatedBy": "/bin/sh -c #(nop)  ENV HOME=/root LANGUAGE=en_US.UTF-8 LANG=en_US.UTF-8 TERM=xterm",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637706,
        "CreatedBy": "/bin/sh -c #(nop)  ARG DEBIAN_FRONTEND=noninteractive",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637704,
        "CreatedBy": "|4 BUILD_DATE=2021-01-26T05:05:04+00:00 OVERLAY_ARCH=aarch64 OVERLAY_VERSION=v2.1.0.2 VERSION=fd2376ac-ls25 /bin/sh -c chmod +x /tmp/s6-overlay-${OVERLAY_ARCH}-installer && /tmp/s6-overlay-${OVERLAY_ARCH}-installer / && rm /tmp/s6-overlay-${OVERLAY_ARCH}-installer",
        "Id": "<missing>",
        "Size": 5991535,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637688,
        "CreatedBy": "/bin/sh -c #(nop) ADD 4f58740c4ce0b21f8d45d774ff3cd81a980d7cabc9f47ef8e46a619ccc3f7559 in /tmp/ ",
        "Id": "<missing>",
        "Size": 6255344,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637684,
        "CreatedBy": "/bin/sh -c #(nop)  ARG OVERLAY_ARCH=aarch64",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637682,
        "CreatedBy": "/bin/sh -c #(nop)  ARG OVERLAY_VERSION=v2.1.0.2",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637681,
        "CreatedBy": "/bin/sh -c #(nop)  LABEL maintainer=TheLamer",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637679,
        "CreatedBy": "/bin/sh -c #(nop)  LABEL build_version=Linuxserver.io version:- fd2376ac-ls25 Build-date:- 2021-01-26T05:05:04+00:00",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637677,
        "CreatedBy": "/bin/sh -c #(nop)  ARG VERSION",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637676,
        "CreatedBy": "/bin/sh -c #(nop)  ARG BUILD_DATE",
        "Id": "<missing>",
        "Size": 0,
        "Tags": null
    },
    {
        "Comment": "",
        "Created": 1611637664,
        "CreatedBy": "/bin/sh -c #(nop) COPY dir:0376870dce13fe7fca7fb7b81e82ee89d85446f7738f6ee4f4a61e280cc627c2 in / ",
        "Id": "<missing>",
        "Size": 65677970,
        "Tags": null
    }
]
'''

