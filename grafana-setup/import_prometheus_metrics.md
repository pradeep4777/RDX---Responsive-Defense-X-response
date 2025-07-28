# How to Import Prometheus Metrics into Grafana

## ✅ Prerequisites
- Prometheus is installed and running at `http://localhost:9090`
- Grafana is installed and running at `http://localhost:3000`

---

## 📊 Step-by-Step to Add Prometheus as Data Source

1. Open Grafana: [http://localhost:3000](http://localhost:3000)
2. Login using default credentials:
   - Username: `admin`
   - Password: `admin`
3. Navigate to:
   - ⚙️ **Gear icon** → **Data Sources**
   - Click **Add data source**
   - Select **Prometheus**
4. Configure the Prometheus Data Source:
   - URL: `http://localhost:9090`
   - Leave other settings as default
   - Click **Save & Test**

---

## 📈 Import Dashboard using Prometheus Metrics

1. Click the **+ (Plus)** icon on left → **Import**
2. You have two options:
   - Paste Dashboard ID from [Grafana.com](https://grafana.com/grafana/dashboards/)
     - For example: `1860` (Node Exporter Full Dashboard)
   - Or Upload a `.json` file if you have exported one earlier
3. Select the Prometheus data source you added
4. Click **Import**

---

## 🔍 Popular Dashboard IDs

| Dashboard | Description                     | ID    |
|----------|---------------------------------|--------|
| Node Exporter Full | Linux system metrics | 1860 |
| Prometheus Stats | Prometheus internal metrics | 2 |
| Docker Monitoring | Monitor Docker containers | 179 |

---

## 🧪 Try Sample Prometheus Queries

- CPU Usage:
  ```promql
  rate(node_cpu_seconds_total{mode!="idle"}[1m])
