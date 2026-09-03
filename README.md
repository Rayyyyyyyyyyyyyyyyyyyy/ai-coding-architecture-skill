# Vibe Coding Engineering Guardrails

[![skills.sh](https://skills.sh/b/Rayyyyyyyyyyyyyyyyyyyy/ai-coding-architecture-skill)](https://skills.sh/Rayyyyyyyyyyyyyyyyyyyy/ai-coding-architecture-skill)

> 你負責做產品，這套 skills 負責補上 AI coding 容易漏掉的工程護欄。

## 這套 skills 解決什麼問題？

Vibe Coding 讓你用日常語言告訴 AI 想做什麼，再一邊看結果、一邊調整。即使不熟悉程式，也能很快做出網站或 App。

但專案做久了，你可能開始遇到：

- 同一種按鈕或提示視窗，AI 每次都重新做一套；
- 換一個 AI 或開新對話，就要重新解釋專案怎麼運作；
- 登入畫面看似完成，真正的權限檢查卻漏了；
- 私密金鑰被放進使用者可以下載的網頁程式；
- 改一個小功能，AI 卻順手重寫大片程式；
- AI 說完成了，但重要測試或外部設定其實還沒做。

這套 collection 把不同問題交給不同 skill。你不需要先學會工程術語，也不必在每次需求中貼上一長串規則。

目前共八個 skills：六個日常工程護欄、一個只在 Agent 委派或交接事件使用的跨領域 contract，以及一個由使用者主動呼叫的救援流程。

## 目前包含六個日常工程護欄

| Skill | 它在背後處理的事 |
| --- | --- |
| `coding-architecture` | 讓新功能沿著專案原本的做法健康長進去，優先沿用、組合，再決定是否需要抽出共用做法。 |
| `architecture-context` | 把不容易從程式本身看懂的重要架構決定留在 repository 裡；它不是完整專案記憶或檔案百科。 |
| `safe-change` | 留意套件、私密資料、登入權限、資料庫、環境設定和破壞性修改等隱藏風險。 |
| `verify-before-done` | 根據修改的風險實際執行有意義的檢查，並讓 AI 只宣稱已被證據支持的完成程度。 |
| `experience-completeness` | 讓互動流程在真正相關的載入、空白、錯誤、重複操作、不同裝置與鍵盤操作情境下仍可完成。 |
| `debug-with-evidence` | 發生 bug、偶發錯誤或效能退化時，先建立可觀測的失敗證據再找原因；只有你要求修復時才修改程式。 |

它們各自保持小而專注，可以單獨使用，也可以一起工作。

## Agent 交接時使用的跨領域 contract

| Skill | 它在什麼事件中工作 |
| --- | --- |
| `a2a-handoff` | 只有在工作實際委派、轉交、續接或回傳給另一個 Agent 時，才用精確任務狀態與最小必要成果交接；它不是一般實作工作的額外 checklist。 |

有 native A2A runtime 時，這個 skill 遵守 host 支援的 A2A object 與 task-state schema。沒有 native runtime 時，使用 A2A-inspired 的精簡文字慣例；這個 fallback 不宣稱是可互通的 A2A protocol payload。

## 需要時主動使用的救援流程

| Skill | 適合什麼時候使用 |
| --- | --- |
| `rescue-vibe-project` | 專案已經能局部運作，但越改越容易壞、缺乏可信 baseline，或你已經不敢繼續修改時，先恢復一條可驗證的核心流程，不預設全面重寫，也不把一條流程通過說成整個 repository 已恢復健康。 |

`rescue-vibe-project` 的 `SKILL.md` 已宣告 `disable-model-invocation: true`，OpenAI/Codex 安裝 metadata 也另外設定 `allow_implicit_invocation: false`。支援其中相應欄位的 hosts 會機械限制隱式呼叫；不支援的環境仍必須遵守只由使用者明確呼叫的行為邊界：

```text
請使用 $rescue-vibe-project，先把這個專案恢復到能安全繼續修改的狀態。
```

## 使用時不必改變你的習慣

你仍然可以只對 AI 說：

```text
幫我加上 Google 登入。
```

支援 skill discovery 的 AI 程式助手，可以在需求符合各 skill 的 trigger 時分別處理：

1. 讀取專案原本的登入與架構規則；
2. 確認金鑰、登入和權限檢查放在安全的位置；
3. 沿用現有畫面和程式組織方式；
4. 執行目前能做的檢查，說清楚哪些外部設定仍待完成。

正常、可逆的工程判斷會安靜完成。只有可能造成資料遺失、洩漏私密資訊、破壞相容性、增加基礎設施成本，或需要你決定產品行為時，AI 才應該停下來說明影響。

`a2a-handoff` 只在真正發生 Agent 委派或交接事件時加入；`rescue-vibe-project` 則仍由你主動呼叫。自動 discovery 與 user-only metadata 的實際支援程度依 AI host 而異。

## 同時安裝到 Claude Code 與 Codex

若要把整套 collection 同時全域安裝到兩邊，執行：

```sh
npx skills@latest add Rayyyyyyyyyyyyyyyyyyyy/ai-coding-architecture-skill --skill '*' --global --agent claude-code --agent codex
```

這會把相同的八個 skills 安裝到 Claude Code 與 Codex；不需要選邊，也不維護兩套行為。若只想安裝到目前專案，移除 `--global`。安裝後開啟新的對話；如果 skills 沒有出現，請重新啟動工具。

如果你不熟悉終端機，可以把上面的指令交給負責設定開發工具的人。

## 也可以明確指定 skill

日常工程護欄通常可以讓相容的 AI 依 trigger 選擇；交接與救援則遵守上面的事件或明確呼叫邊界。需要時，也可以直接寫：

```text
請使用 $coding-architecture，依照專案原本的做法完成這個頁面。
```

```text
請使用 $architecture-context，確認這次修改沒有破壞原本的架構決定。
```

```text
請使用 $safe-change，檢查這次登入與資料庫修改的隱藏風險。
```

```text
請使用 $verify-before-done，實際確認這次修改可以使用，再告訴我哪些部分已被驗證。
```

```text
請使用 $a2a-handoff，把目前任務精準交給下一個 Agent。
```

## 安靜，但不是省略責任

這些 skills 不會要求 AI 每次向你背誦設計模式或安全名詞。重點是讓它做出比較健康的工程決定，而不是讓回答看起來很專業。

它們也不是保證書。重要功能仍然需要實際操作與測試；涉及正式環境、資料移轉、金鑰設定或外部服務時，完成程式碼不代表部署已經完成。

## 跨 AI 使用

每個 skill 的核心行為只維護在標準 `SKILL.md` 中。Claude Code 使用其支援的 frontmatter；Codex 使用 `agents/openai.yaml` 補充 UI 與 invocation policy。兩邊共用相同行為，但 discovery、user-only enforcement 與 native A2A capability 仍由各 host 負責。

## 評估與設計原則

- [Behavioral evaluation case specifications](evaluations/README.md)：定義要測哪些工程決定與執行紀錄；目前不是已通過的評估結果。
- [Collection philosophy](docs/philosophy.md)：說明為什麼 skills 要保持安靜、專注、可組合且不綁定模型。
- [Skill routing and ownership](docs/skill-routing.md)：區分六個工程護欄、delegation-event handoff 與主動 rescue workflow 的觸發及責任邊界。
- [Host-neutral skill composition](docs/skill-composition.md)：說明跨 host 如何依具體 signal 載入另一支 skill，避免在同一 active context 重複載入，也不假設 Skill 會跨 turn 或 Agent 永久存在。

### 驗證 invocation policy

目前驗證採分層方式：七個可由模型選擇的 skills 必須通過 Codex
`quick_validate.py`；八個 `SKILL.md` 都必須能解析 YAML frontmatter。救援
skill 在目前 Codex validator 中唯一允許的已知失敗是
`Unexpected key(s) in SKILL.md frontmatter: disable-model-invocation`，因為該
validator 尚未接受這個跨 host 的 explicit-only extension key。這不是忽略
policy：另外必須靜態確認 `disable-model-invocation: true` 與 OpenAI/Codex
sidecar 的 `allow_implicit_invocation: false` 同時存在。其他 validator 錯誤
仍視為失敗。

## License

MIT
