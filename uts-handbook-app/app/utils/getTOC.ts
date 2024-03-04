export default function getToc(content: string) {
  const lines = content.split("\n");
  const toc = [];
  let highestLevel = 1000;

  for (const line of lines) {
    if (line.startsWith("#")) {
      const level = (line.match(/#+/) || [[1, 2, 3]])[0].length;
      const title = line.replace(/#+/, "").trim();

      if (level < highestLevel) highestLevel = level;
      toc.push({ level, title });
    }
  }

  return { toc, highestLevel };
}
