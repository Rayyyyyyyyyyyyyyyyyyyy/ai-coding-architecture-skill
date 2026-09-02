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

## 目前包含三個核心 skills

| Skill | 它在背後處理的事 |
| --- | --- |
| `coding-architecture` | 讓新功能沿著專案原本的做法健康長進去，優先沿用、組合，再決定是否需要抽出共用做法。 |
| `architecture-context` | 把重要架構決定留在 repository 裡，讓不同 AI、不同對話和未來的人都能接著做。 |
| `safe-change` | 留意套件、私密資料、登入權限、資料庫、環境設定和破壞性修改等隱藏風險。 |

它們各自保持小而專注，可以單獨使用，也可以一起工作。

## 使用時不必改變你的習慣

你仍然可以只對 AI 說：

```text
幫我加上 Google 登入。
```

支援自動載入 skills 的 AI 程式助手，可以在背後分別處理：

1. 讀取專案原本的登入與架構規則；
2. 確認金鑰、登入和權限檢查放在安全的位置；
3. 沿用現有畫面和程式組織方式；
4. 執行目前能做的檢查，說清楚哪些外部設定仍待完成。

正常、可逆的工程判斷會安靜完成。只有可能造成資料遺失、洩漏私密資訊、破壞相容性、增加基礎設施成本，或需要你決定產品行為時，AI 才應該停下來說明影響。

## 安裝

若要在 Codex 中一次全域安裝三個 skills，執行：

```sh
npx skills@latest add Rayyyyyyyyyyyyyyyyyyyy/ai-coding-architecture-skill --skill '*' --agent codex --global --yes
```

這會安裝 `coding-architecture`、`architecture-context` 和 `safe-change`，並略過逐步選單。若只想安裝到目前專案，移除 `--global`；若使用其他 AI 工具，將 `codex` 換成該工具的 agent ID。安裝後開啟新的對話；如果 skills 沒有出現，請重新啟動工具。

如果你不熟悉終端機，可以把上面的指令交給負責設定開發工具的人。

## 也可以明確指定 skill

通常讓相容的 AI 自動選擇即可。需要時，也可以直接寫：

```text
請使用 $coding-architecture，依照專案原本的做法完成這個頁面。
```

```text
請使用 $architecture-context，確認這次修改沒有破壞原本的架構決定。
```

```text
請使用 $safe-change，檢查這次登入與資料庫修改的隱藏風險。
```

## 安靜，但不是省略責任

這些 skills 不會要求 AI 每次向你背誦設計模式或安全名詞。重點是讓它做出比較健康的工程決定，而不是讓回答看起來很專業。

它們也不是保證書。重要功能仍然需要實際操作與測試；涉及正式環境、資料移轉、金鑰設定或外部服務時，完成程式碼不代表部署已經完成。

## 跨 AI 使用

每個 skill 的核心行為只維護在標準 `SKILL.md` 中，不依賴某個 AI 的專有工具名稱。目標是讓 Codex、Claude Code，以及其他支援 Agent Skills 的 coding agent 都能採用一致的工程護欄。

## 評估與設計原則

- [Behavioral evaluation](evaluations/README.md)：測試 AI 最後做出的工程決定，不比對固定話術。
- [Collection philosophy](docs/philosophy.md)：說明為什麼 skills 要保持安靜、專注、可組合且不綁定模型。

## License

MIT
