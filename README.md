<div align="center">

# Vibe Coding Engineering Guardrails

**先看懂專案，再放心修改。這套 skills 幫 AI 別把專案越寫越難改。**

[![Install with skills.sh](https://skills.sh/b/Rayyyyyyyyyyyyyyyyyyyy/ai-coding-architecture-skill)](https://skills.sh/Rayyyyyyyyyyyyyyyyyyyy/ai-coding-architecture-skill)

[直接安裝](#直接安裝) · [看看有哪些-skills](#這-9-個-skills-各自管什麼) · [怎麼使用](#基本上不用特別做什麼) · [維護這個-repo](#維護這個-repo)

</div>

---

用 AI 做產品很快。你說一句「幫我加個登入」，沒多久畫面就出來了。

麻煩通常不是第一版做不出來，而是改到第十次之後，專案開始出現一些很難解釋的小毛病：

- 明明有現成的按鈕，AI 又做了一個幾乎一樣的
- 換個 AI 或開新對話，就得重新解釋整個專案
- 登入畫面做好了，真正的權限檢查卻沒做
- 私密金鑰不小心被包進前端，任何人都能看到
- 只想改一個小地方，結果半個專案一起被翻修
- AI 說「完成了」，但重要的測試根本沒跑

這個 repo 收了 9 個 skills，幫你看懂專案，也替 AI 補上這些容易被忽略的工程習慣。

它們不是要把每個需求變成一場架構會議，也不是要 AI 回答得更像教科書。它們只希望 AI 在動手之前多看一眼、做完之後多確認一步，讓今天省下來的時間，不會變成下個月要還的技術債。

> 其中 6 個會在平常寫程式時派上用場；1 個用白話帶你看懂現有專案；1 個只管 Agent 之間的交接；1 個是專案已經亂掉時才會主動叫來的救援隊。

## 直接安裝

下面這行會把全部 skills 安裝到 Claude Code 和 Codex：

```sh
npx skills@latest add Rayyyyyyyyyyyyyyyyyyyy/ai-coding-architecture-skill --skill '*' --global --agent claude-code --agent codex
```

裝好後開一個新對話就能使用。如果沒看到 skills，重新啟動工具一次。

<details>
<summary>只想裝在目前這個專案裡</summary>

把 `--global` 拿掉：

```sh
npx skills@latest add Rayyyyyyyyyyyyyyyyyyyy/ai-coding-architecture-skill --skill '*' --agent claude-code --agent codex
```

</details>

不熟終端機也沒關係，把上面的指令丟給幫你設定開發環境的人就好。

## 這 9 個 skills 各自管什麼

### 先看懂做到一半的專案

[`explain-project`](skills/explain-project/) 從目前的程式追查，用白話說明產品在做什麼、各部分負責什麼、資料從哪裡來、送出後存去哪裡，以及哪些地方還是假資料或尚未接通。

```text
請使用 $explain-project，帶我看懂這個專案的架構與資料流，先不要改程式。
```

你不需要自己讀給 Agent 的指令文件。它會直接解說具體操作背後的流程，附少量程式連結供追問；沒有實際執行驗證的部分，也會說清楚。第一輪先建立主要架構與代表流程的全貌，再依你的問題深入。

### 平常寫程式時

<table>
  <thead>
    <tr>
      <th width="240" align="left">Skill</th>
      <th align="left">它會提醒 AI 什麼</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="240"><a href="skills/coding-architecture/"><code>coding-architecture</code></a></td>
      <td>寫新功能前，先看看專案原本怎麼做。能沿用就沿用，能組合就組合。只問重構建議時，先列出問題、影響與建議範圍；要求實作後才修改。</td>
    </tr>
    <tr>
      <td width="240"><a href="skills/architecture-context/"><code>architecture-context</code></a></td>
      <td>找回光看程式猜不出的架構決定。只問現有設計時，說明原因與文件衝突；已授權的修改改變設計意圖時，再同步最近的架構紀錄。</td>
    </tr>
    <tr>
      <td width="240"><a href="skills/safe-change/"><code>safe-change</code></a></td>
      <td>動到套件、金鑰、登入權限、資料庫或環境設定時，先確認這個改動會不會留下安全問題，或造成難以復原的損失。</td>
    </tr>
    <tr>
      <td width="240"><a href="skills/verify-before-done/"><code>verify-before-done</code></a></td>
      <td>說「完成」以前先拿證據。測到哪裡就說到哪裡，還沒驗證的部分不要假裝已經沒問題。</td>
    </tr>
    <tr>
      <td width="240"><a href="skills/experience-completeness/"><code>experience-completeness</code></a></td>
      <td>盤點流程真正需要的載入、空資料、錯誤、重複操作及無障礙等狀態。只問缺什麼時先交清單；要求補齊後才實作，需要新增產品行為時先確認。</td>
    </tr>
    <tr>
      <td width="240"><a href="skills/debug-with-evidence/"><code>debug-with-evidence</code></a></td>
      <td>遇到 bug 或效能問題，先讓問題穩定地出現、留下看得見的證據，再判斷原因。同一條路連續失敗三次，就停下來重看目標、假設和其他解法。除非你叫它修，否則它只負責查清楚。</td>
    </tr>
  </tbody>
</table>

這六個 skills 各管一件事。需要一起工作時會互相配合，不需要時也不會硬湊成一張超長檢查表。

### 特殊情況才用

<table>
  <thead>
    <tr>
      <th width="240" align="left">Skill</th>
      <th align="left">什麼時候叫它</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="240"><a href="skills/a2a-handoff/"><code>a2a-handoff</code></a></td>
      <td>真的要把工作交給另一個 Agent 時，才用它整理「做到哪裡、留下什麼、接下來要做什麼」。一般寫功能時不需要多跑這一套。</td>
    </tr>
    <tr>
      <td width="240"><a href="skills/rescue-vibe-project/"><code>rescue-vibe-project</code></a></td>
      <td>專案還能跑，但每改一次就壞別的地方，甚至已經沒人敢再碰時，用它先列出問題 checklist，與你確認要修的項目和驗證方式後，再救回一條可以驗證的核心流程。它不會一上來就全面重寫，也不會因為救活一頁就宣布整個專案都健康了。</td>
    </tr>
  </tbody>
</table>

`rescue-vibe-project` 不會由 AI 自己決定啟用。你真的需要時，請直接說：

```text
請使用 $rescue-vibe-project，先列出找到的問題 checklist，與我確認修復範圍後，再實作修復，讓專案恢復到能安全繼續修改的狀態。
```

<details>
<summary>a2a-handoff 的相容方式</summary>

如果執行環境原生支援 A2A，這個 skill 會使用該環境提供的 A2A object 和 task-state schema。沒有原生支援時，就改用一份精簡、容易讀的文字交接。

後者只是借用 A2A 的交接概念，不是假裝自己是能與其他系統互通的標準 A2A payload。

</details>

## 基本上，不用特別做什麼

你還是照平常的方式跟 AI 說話：

```text
幫我加上 Google 登入。
```

如果你使用的工具支援 skill discovery，AI 會依照這個需求，自己注意幾件事：

1. 專案原本怎麼處理登入和權限
2. 金鑰有沒有放在不該出現的地方
3. 新畫面能不能沿用現成的元件和結構
4. 做完後可以跑哪些檢查，還有哪些外部設定要由人完成

一般、可復原的工程判斷，它應該安靜地處理掉。真的可能刪掉資料、洩漏秘密、破壞相容性、增加基礎設施成本，或需要你決定產品行為時，它才應該停下來找你確認。

不同 AI 工具對自動載入 skills、限制使用者專用流程，以及 Agent 交接格式的支援程度不太一樣，實際行為仍以你使用的工具為準。

### 先說明，還是開始修改？

| 你提出的需求 | AI 應該做到哪裡 |
| :--- | :--- |
| 「帶我看懂架構和資料流」 | 用 `explain-project` 解說目前怎麼運作，指出未完成與未驗證處，保持唯讀。 |
| 「看看哪裡能重構／這個流程缺什麼」 | 先提供有證據的建議或狀態清單，等你要求實作。 |
| 「把剛才選的項目做好」 | 在已同意的範圍內實作與驗證，一般選擇不必反覆確認。 |
| 「救回這個專案」 | 用 `rescue-vibe-project` 先列問題 checklist，等你確認修復範圍後才動手；擴大範圍時再確認。 |

### 想點名也可以

如果這次特別在意某個面向，可以直接講：

```text
請使用 $explain-project，說明新增一筆資料後會經過哪些地方、最後存在哪裡。

請使用 $coding-architecture，照專案原本的做法完成這個頁面。

請使用 $architecture-context，確認這次修改沒有弄壞原本的架構決定。

請使用 $safe-change，檢查這次登入和資料庫修改有沒有隱藏風險。

請使用 $verify-before-done，實際確認這次修改能不能用，再告訴我哪些部分真的驗證過了。

請使用 $a2a-handoff，把目前任務完整交給下一個 Agent。
```

## 這套東西刻意不做什麼

- **不逼 AI 背術語給你聽。** 工程判斷有做到，比回答看起來很專業重要。
- **不把每次修改都當成大工程。** 小改動就用小改動該有的力氣處理。
- **不把一句「測試通過」當萬靈丹。** 改動風險不同，需要的證據也不同。
- **不亂保證。** 程式碼寫完，不代表正式環境、資料移轉、金鑰或外部服務都已經設定完成。
- **不宣稱能讓專案永遠不出錯。** 它能做的是讓錯誤少一點、出事時比較容易查，也比較容易救回來。

## Claude Code 和 Codex 都能用

每個 skill 的核心規則只寫在一份標準的 `SKILL.md` 裡，不需要為不同 AI 維護兩套內容。

| 工具 | 怎麼接上 |
| :--- | :--- |
| Claude Code | 讀取它支援的 `SKILL.md` frontmatter |
| Codex | 另外透過 `agents/openai.yaml` 補上介面資訊和呼叫規則 |

兩邊讀到的是同一套行為。不過哪些 skills 會自動出現、哪些只能由使用者呼叫，以及 Agent 之間能不能直接交換結構化資料，仍由各自的工具決定。

## 維護這個 repo

本 repo 採用 Matt 工作流的分工：先確認範圍、依 Markdown 規格實作，再用行為評估與 Standards／Spec 雙軸 review 檢查結果。工作追蹤放在本地 Markdown，設定由 [AGENTS.md](AGENTS.md) 與 [CLAUDE.md](CLAUDE.md) 共同指向 [docs/agents/](docs/agents/)。

| 想查看什麼 | 位置 |
| :--- | :--- |
| 工作追蹤與狀態慣例 | [Issue tracker](docs/agents/issue-tracker.md)、[triage 狀態](docs/agents/triage-labels.md) |
| 功能規格與進度 | `.scratch/<feature>/`；例如 `explain-project` 的[規格](.scratch/explain-project/spec.md)與[進度](.scratch/explain-project/progress.md) |
| 行為評估方式 | [evaluations/README.md](evaluations/README.md) |
| `explain-project` 已執行的評估 | [情境、結果與限制](evaluations/explain-project/runs/2026-09-07/README.md) |

評估案例與實際執行紀錄分開保存。`explain-project` 的兩個隔離情境與一個對照組已通過；對照組同樣能完成解說，因此目前不能宣稱新 skill 帶來多少改善，也尚未驗證真人理解成效。

這些是維護本集合的設定；安裝及使用各個 skill 不需要另外安裝 Matt 的技能套件。

## License

[MIT](LICENSE)
