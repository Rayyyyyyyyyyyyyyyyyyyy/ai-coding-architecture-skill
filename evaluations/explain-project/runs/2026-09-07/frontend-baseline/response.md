這是一個很小的原生 JavaScript 待辦清單，目前能在畫面上新增項目，但資料只存在這次開啟頁面的記憶體中，重新整理就會消失。專案筆記寫的是「預計透過 API 儲存」，實際程式還沒接上。

架構可以看成三塊：

- [index.html](/private/tmp/explain-project-work-pf2duh5z/runs/frontend-baseline/repo/index.html:6)：提供輸入表單、清單容器，並載入 `app.js`。
- [app.js](/private/tmp/explain-project-work-pf2duh5z/runs/frontend-baseline/repo/app.js:1)：負責畫面事件、暫存資料及重畫清單。沒有前端框架，直接操作瀏覽器的 DOM。
- [task-client.js](/private/tmp/explain-project-work-pf2duh5z/runs/frontend-baseline/repo/task-client.js:1)：已寫好 `createTask(title)`，可將 `{ title }` 以 JSON POST 到 `/api/tasks`，但目前沒有被畫面程式匯入或呼叫。

目前資料實際這樣走：

1. 開啟頁面 → 建立內含「試著新增一筆待辦」的 `tasks` 陣列 → 畫出清單。
2. 使用者按新增 → 攔下表單原本的送出行為 → 讀取文字、去掉頭尾空白；空白內容不新增。
3. 產生隨機 ID → 加進 `tasks` 陣列 → 重新畫出整份清單 → 清空表單。

這條流程沒有發出網路請求。畫面顯示新增成功，只代表本地陣列已更新，並不代表已儲存到伺服器。

還沒接好的地方主要有三個：

- **新增尚未串 API。** 表單直接更新陣列，沒有呼叫現有的 `createTask()`，也沒有等待儲存結果、顯示儲存中狀態或處理失敗。
- **後端與持久化在這份 repo 中看不到。** 沒有 `/api/tasks` 的伺服器實作或資料庫程式，因此不能根據筆記認定資料已能永久儲存；也無法從這份 repo 確認外部是否另有服務。
- **重新載入資料的流程尚未實作。** 每次開頁都從寫死的範例開始，沒有向伺服器讀取待辦的程式，也沒有使用瀏覽器本地儲存。即使接好新增 API，還需要補上讀取，重新整理後才會看到之前的資料。

[CLAUDE.md](/private/tmp/explain-project-work-pf2duh5z/runs/frontend-baseline/repo/CLAUDE.md:5) 的架構描述應視為初始計畫：預期是「表單 → API client → 伺服器儲存」，現況則是「表單 → 記憶體陣列 → 畫面」。接手時最先要確認的是後端服務在哪裡，以及新增、讀取 API 的資料格式，再把畫面串起來。

以上依完整閱讀這份 repo 的四個檔案判斷；沒有修改程式，也沒有啟動瀏覽器或驗證外部 API。
