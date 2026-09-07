export function createEditor(document) {
  let selection = null;
  return {
    select(blockId) { selection = blockId; },
    selectedBlock() { return selection; },
    updateText(blockId, text) {
      document.blocks.find(block => block.id === blockId).text = text;
    },
    serialize() { return JSON.stringify(document); },
  };
}
