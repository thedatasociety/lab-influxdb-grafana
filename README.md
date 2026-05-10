<!-- ds header -->
<div align="center">
  <img src="https://avatars3.githubusercontent.com/u/47368510?s=200&v=4" width="100px">
  <h3>The Data Science and Engineering Society</h3>
  <hr/>
</div>
<br/>
<!-- /ds header -->

# Time Series Data Lab — InfluxDB, MongoDB & Grafana

A hands-on sandbox for learning time series data collection, storage, and visualization. This lab covers **two complementary approaches** to storing time series data:

- **InfluxDB 3** — a purpose-built time series database, used together with Telegraf and Grafana (the TIG stack)
- **MongoDB Time Series Collections** — time series support built into a general-purpose document database (MongoDB 5.0+)

Understanding both gives you the flexibility to choose the right tool for each use case. This repository is [BinderHub](https://github.com/jupyterhub/binderhub)-ready, meaning you can launch a fully configured environment in your browser with a single click — no local installation required.

---

## What's Inside

### Time Series Databases

| Component | Version | Role |
|---|---|---|
| [InfluxDB 3 Core](https://www.influxdata.com/products/influxdb/) | 3.9.2 | Purpose-built time series database |
| [MongoDB](https://www.mongodb.com/) | 8.3.1 | General-purpose database with native Time Series Collections |

### Supporting Stack

| Component | Version | Role |
|---|---|---|
| [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) | 1.11.2 | Metrics collection and ingestion agent |
| [Grafana](https://grafana.com/) | 6.2.5 | Metrics visualization and dashboards |
| [VS Code Server](https://github.com/cdr/code-server) | 3.4.1 | Browser-based IDE |

### Notebooks

| Notebook | Description |
|---|---|
| `1.influxdb.ipynb` | Introduction to InfluxDB — writing and querying time series data |
| `2.telegraf.ipynb` | Collecting system and application metrics with Telegraf |
| `3.grafana.ipynb` | Building dashboards and visualizing metrics in Grafana |
| `4.mongodb-timeseries.ipynb` | Time series with MongoDB — from basic inserts to advanced window functions |
| `1.Case IoT.ipynb` | End-to-end IoT use case using the full TIG stack |

---

## Option 1 — Launch in the Cloud (no installation needed)

[MyBinder.org](https://mybinder.org) is a free public service that builds and serves reproducible computational environments from Git repositories. Click any badge below to launch this lab directly in your browser.

> **Note:** The environment may take a few minutes to build on the first launch. Subsequent launches are faster due to caching.

### JupyterLab

<a href="https://mybinder.org/v2/gh/thedatasociety/lab-timeseries-dbs/master?urlpath=lab" target="_blank">
  <img src="https://img.shields.io/badge/_launch_JupyterLab-@_mybinder.org-blue?logo=jupyter" alt="Launch JupyterLab on mybinder.org">
</a><br/><br/>

<a href="https://2i2c.mybinder.org/v2/gh/thedatasociety/lab-timeseries-dbs/master?urlpath=lab" target="_blank">
  <img src="https://img.shields.io/badge/_launch_JupyterLab-@_2i2c.mybinder.org-blue?logo=jupyter" alt="Launch JupyterLab on 2i2c.mybinder.org">
</a><br/><br/>

<a href="https://bids.mybinder.org/v2/gh/thedatasociety/lab-timeseries-dbs/master?urlpath=lab" target="_blank">
  <img src="https://img.shields.io/badge/_launch_JupyterLab-@_bids.mybinder.org-blue?logo=jupyter" alt="Launch JupyterLab on bids.mybinder.org">
</a><br/><br/>

<a href="https://gesis.mybinder.org/v2/gh/thedatasociety/lab-timeseries-dbs/master?urlpath=lab" target="_blank">
  <img src="https://img.shields.io/badge/_launch_JupyterLab-@_gesis.mybinder.org-blue?logo=jupyter" alt="Launch JupyterLab on gesis.mybinder.org">
</a><br/><br/>

### VS Code

<a href="https://mybinder.org/v2/gh/thedatasociety/lab-timeseries-dbs/master?urlpath=vscode/" target="_blank">
  <img src="https://img.shields.io/badge/_launch_VSCode-@_mybinder.org-blue?logo=vscodium" alt="Launch VSCode on mybinder.org">
</a><br/><br/>

<a href="https://2i2c.mybinder.org/v2/gh/thedatasociety/lab-timeseries-dbs/master?urlpath=vscode/" target="_blank">
  <img src="https://img.shields.io/badge/_launch_VSCode-@_2i2c.mybinder.org-blue?logo=vscodium" alt="Launch VSCode on 2i2c.mybinder.org">
</a><br/><br/>

<a href="https://bids.mybinder.org/v2/gh/thedatasociety/lab-timeseries-dbs/master?urlpath=vscode/" target="_blank">
  <img src="https://img.shields.io/badge/_launch_VSCode-@_bids.mybinder.org-blue?logo=vscodium" alt="Launch VSCode on bids.mybinder.org">
</a><br/><br/>

<a href="https://gesis.mybinder.org/v2/gh/thedatasociety/lab-timeseries-dbs/master?urlpath=vscode/" target="_blank">
  <img src="https://img.shields.io/badge/_launch_VSCode-@_gesis.mybinder.org-blue?logo=vscodium" alt="Launch VSCode on gesis.mybinder.org">
</a><br/><br/>

---

## Option 2 — Run Locally with repo2docker

[repo2docker](https://github.com/jupyter/repo2docker) builds and runs the same environment as Binder, but on your local machine inside a Docker container. This is the recommended approach if you want to persist your work or work offline.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed and running
- Your local user added to the `docker` group (see [post-install steps](https://docs.docker.com/engine/install/linux-postinstall/))
- Python 3.6+ and `pip`

> **Security note:** The commands below use `--ip 0.0.0.0`, which accepts connections from any network interface. The `--NotebookApp.token` flag enforces token-based authentication. Replace `mytoken` with a strong, unique token in shared or remote environments. **Do not run the container as root.**

---

### Option 2a — From the remote repository (no local repo clone needed)

**1.** Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

**2.** Install `jupyter-repo2docker`:

```bash
pip install jupyter-repo2docker --upgrade
```

**3.** Launch the container directly from GitHub:

```bash
jupyter-repo2docker -p 8888:8888 \
    https://github.com/thedatasociety/lab-timeseries-dbs \
    jupyter lab --ip 0.0.0.0 --NotebookApp.token='mytoken'
```

---

### Option 2b — From a local clone

**1.** Clone the repository and enter the folder:

```bash
git clone https://github.com/thedatasociety/lab-timeseries-dbs.git
cd lab-timeseries-dbs
```

**2.** Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

**3.** Install `jupyter-repo2docker`:

```bash
pip install jupyter-repo2docker --upgrade
```

**4.** Launch the container:

```bash
jupyter-repo2docker -p 8888:8888 ./ \
    jupyter lab --ip 0.0.0.0 --NotebookApp.token='mytoken'
```

**4b.** To also mount your local folder inside the container (so changes persist on disk):

```bash
jupyter-repo2docker -p 8888:8888 \
    -v $(pwd):$(echo ~)/host-folder \
    ./ jupyter lab --ip 0.0.0.0 --NotebookApp.token='mytoken'
```

The mounted folder will appear as `host-folder` inside JupyterLab and VS Code.

---

### Accessing the interfaces

Once the container is running, open your browser and navigate to:

| Interface | URL |
|---|---|
| JupyterLab | http://127.0.0.1:8888/lab?token=mytoken |
| Jupyter Notebook | http://127.0.0.1:8888/tree?token=mytoken |
| VS Code | http://127.0.0.1:8888/vscode?token=mytoken |

---

## Further Reading

- [repo2docker documentation](https://repo2docker.readthedocs.io/)
- [MyBinder user documentation](https://mybinder.readthedocs.io/)
- [InfluxDB 3 Core documentation](https://docs.influxdata.com/influxdb3/core/)
- [Telegraf documentation](https://docs.influxdata.com/telegraf/)
- [Grafana documentation](https://grafana.com/docs/)
- [MyBinder Federation](https://binderhub.readthedocs.io/en/latest/federation/federation.html)