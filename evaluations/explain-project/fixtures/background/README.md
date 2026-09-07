# 訂單通知

此專案讓使用者建立訂單並查看通知處理狀態。

本機入口：`python3 api.py` 提供頁面與 API；另以 `python3 worker.py`
啟動背景工作。兩者使用 `ORDER_DB` 指定的同一個 SQLite 檔案，預設為
`orders.sqlite3`。執行 API 會建立資料表。

通知服務由 `NOTIFY_URL` 及 `NOTIFY_TOKEN` 設定。本 repo 不包含憑證或部署紀錄。
