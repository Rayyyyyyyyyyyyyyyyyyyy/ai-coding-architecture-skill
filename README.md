<div align="center">

# Vibe Coding Engineering Guardrails

**看懂專案、找到問題，再把修改做好。**

[![Install with skills.sh](https://skills.sh/b/Rayyyyyyyyyyyyyyyyyyyy/ai-coding-architecture-skill)](https://skills.sh/Rayyyyyyyyyyyyyyyyyyyy/ai-coding-architecture-skill)

[安裝](#安裝) · [8-個好記的入口](#8-個好記的入口) · [怎麼使用](#怎麼使用) · [維護與評估](#維護與評估)

</div>

用 AI 做出第一版很快，後續修改卻可能越來越難。這套 8 個 skills 幫你看懂
現況、檢查架構、補齊操作流程，並讓 AI 拿出與修改範圍相稱的驗證證據。

統一使用 `vibe-` 前綴，讓這組 skills 在清單中容易辨認；後面的短名稱負責好記。
自然語言指定這次要做什麼。你也可以直接描述需求，
由支援 skill discovery 的工具選擇適用能力。

## 安裝

安裝到 Claude Code 和 Codex：

```sh
npx skills@latest add Rayyyyyyyyyyyyyyyyyyyy/ai-coding-architecture-skill --skill '*' --global --agent claude-code --agent codex
```

只安裝到目前專案時，拿掉 `--global`。裝好後開新對話；若沒有出現，再重新啟動工具。
不同工具的自動選擇與 Agent 交接能力仍以該工具實際支援為準。

## 8 個好記的入口

<table>
  <thead>
    <tr>
      <th width="240" align="left">想做什麼</th>
      <th width="240" align="left">Skill</th>
      <th align="left">它負責什麼</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="240">看專案</td>
      <td width="240"><a href="skills/vibe-project/"><code>vibe-project</code></a></td>
      <td>解釋架構與資料流、評估全 repo 或跨單元的架構問題，也可以一次做兩者。</td>
    </tr>
    <tr>
      <td width="240">看前端</td>
      <td width="240"><a href="skills/vibe-frontend/"><code>vibe-frontend</code></a></td>
      <td>檢查前端責任、狀態、副作用、資料契約、型別保障與測試邊界；也指導前端實作與重構。</td>
    </tr>
    <tr>
      <td width="240">找設計原因</td>
      <td width="240"><a href="skills/vibe-design-context/"><code>vibe-design-context</code></a></td>
      <td>找回非顯而易見的設計理由；已授權的修改改變長期設計意圖時，同步最近的紀錄。</td>
    </tr>
    <tr>
      <td width="240">查操作流程</td>
      <td width="240"><a href="skills/vibe-ux/"><code>vibe-ux</code></a></td>
      <td>檢查或補齊相關的處理中、空結果、失敗重試、成功、重複操作、鍵盤與版面狀態。</td>
    </tr>
    <tr>
      <td width="240">找 bug</td>
      <td width="240"><a href="skills/vibe-debug/"><code>vibe-debug</code></a></td>
      <td>用可重現的證據找出故障原因；要求修復後才修改。</td>
    </tr>
    <tr>
      <td width="240">安全修改</td>
      <td width="240"><a href="skills/vibe-safe-change/"><code>vibe-safe-change</code></a></td>
      <td>處理依賴、金鑰、權限、持久資料、執行環境與恢復等具體風險。</td>
    </tr>
    <tr>
      <td width="240">驗證結果</td>
      <td width="240"><a href="skills/vibe-verify/"><code>vibe-verify</code></a></td>
      <td>執行與風險相稱的檢查，區分程式已改、局部驗證與正式環境實際驗證。</td>
    </tr>
    <tr>
      <td width="240">交接工作</td>
      <td width="240"><a href="skills/vibe-handoff/"><code>vibe-handoff</code></a></td>
      <td>真的交給另一個 Agent 時，傳遞任務狀態、產物、證據與未完成事項。</td>
    </tr>
  </tbody>
</table>

架構審查會說明程式證據、具體後果與最小改善範圍。長檔案、JavaScript、
目錄形狀或缺少測試是調查線索，不能單獨證明架構有問題。
`vibe-frontend` 可以在架構評估時提出有依據的 TypeScript 或資料驗證建議；
一般 JS 功能開發仍沿用既有語言。

`vibe-ux` 關心使用者能不能完成操作；`vibe-frontend` 關心實作這些操作的責任怎麼組織。
例如刪除圖片，前者檢查失敗時有沒有恢復與提示，後者檢查請求、狀態和撤銷由誰管理。

## 怎麼使用

```text
用 $vibe-project 帶我看懂這個 repo。
用 $vibe-project 檢查整個專案有哪些架構問題，先不要改。
用 $vibe-project 帶我看懂資料流，順便指出架構問題。

用 $vibe-frontend 看看這個 App 該怎麼拆，先提供建議。
用 $vibe-frontend 實作剛才確認的重構範圍。
用 $vibe-design-context 找出這個模組為什麼這樣設計。

用 $vibe-ux 檢查刪除流程有沒有漏掉的情況。
用 $vibe-debug 查明儲存失敗的原因。
用 $vibe-safe-change 檢查這次權限修改的風險。
用 $vibe-verify 確認剛才的修改。
用 $vibe-handoff 把目前工作交給下一個 Agent。
```

`vibe-project` 依請求選擇解說、評估或兩者，共用已追查的程式證據。
只問「怎麼運作」時，會說明未接通與未驗證處；要求「找架構問題」時，
才進一步做架構判斷。兩種模式都保持唯讀；要求儲存報告時，只寫指定的報告。

| 需求 | 工作範圍 |
| :--- | :--- |
| 看懂、評估、提供建議 | 讀取證據並回答，不修改應用程式。 |
| 診斷故障 | 查明原因；明確要求修復後才修。 |
| 實作已選項目 | 在授權範圍內完成與驗證，一般工程選擇不必反覆確認。 |
| 接手做到一半的 repo | 先用 `vibe-project` 理解或評估，再依需求繼續開發。 |
| 接手已經故障的 repo | 參考[接手故障專案流程](docs/workflows/recovery.md)，確認修復範圍，再組合相關 skills。 |

救援是一套組合流程，沒有額外的 skill 入口。它不會因為 repo 尚未完成就自動啟動，
也不會因修好一條核心流程便宣稱整個 repo 已經健康。

## 舊名稱對照

| 舊名稱 | 現在使用 |
| :--- | :--- |
| `project`、`explain-project`、`assess-project-architecture` | `vibe-project`：解說／評估／兩者 |
| `frontend`、`coding-architecture` | `vibe-frontend` |
| `design-context`、`architecture-context` | `vibe-design-context` |
| `ux`、`experience-completeness` | `vibe-ux` |
| `debug`、`debug-with-evidence` | `vibe-debug` |
| `verify`、`verify-before-done` | `vibe-verify` |
| `handoff`、`a2a-handoff` | `vibe-handoff` |
| `rescue-vibe-project` | [接手故障專案流程](docs/workflows/recovery.md) |
| `safe-change` | `vibe-safe-change` |

這些是重新命名，沒有另外保留舊名稱的可呼叫別名。先前安裝的舊目錄可能仍存在；
更新時請確認安裝工具的結果，避免同時留下兩套入口。修改本 repo 不會自動更新全域安裝副本。

## 維護與評估

每個 skill 的核心規則在 `SKILL.md`；`agents/openai.yaml` 提供 Codex 的顯示名稱與呼叫提示。
[路由分工](docs/skill-routing.md)與[組合規則](docs/skill-composition.md)說明能力如何配合。

本 repo 的工作追蹤放在 `.scratch/<feature>/`，遵循 [AGENTS.md](AGENTS.md)
指向的 [issue tracker](docs/agents/issue-tracker.md) 與 [triage 慣例](docs/agents/triage-labels.md)。

行為案例與實際執行紀錄分開保存，方法見 [evaluations](evaluations/README.md)。
[早期專案解說評估](evaluations/explain-project/runs/2026-09-07/README.md)保留當時的名稱、
skill 快照與結果，不能當成合併後 `vibe-project` 已通過評估的證明。
新增或更新案例本身也不代表已經執行通過。

`vibe-handoff` 在支援原生 A2A 的環境使用 host schema；其他環境使用精簡文字交接，
不宣稱具備原生協定互通能力。

## License

[MIT](LICENSE)
