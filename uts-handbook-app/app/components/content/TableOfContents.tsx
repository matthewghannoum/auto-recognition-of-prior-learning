import getHeaderId from "@/app/utils/getHeaderId";
import getToc from "@/app/utils/getTOC";
import Link from "next/link";

export default function TableOfContents({ content }: { content: string }) {
  const { toc, highestLevel } = getToc(content);

  return (
    <div className="sticky min-w-96 max-w-xl bg-gray-100 rounded-lg p-6 left-0 top-10">
      <h4 className="mb-3">Contents</h4>

      <div className="flex flex-col items-start justify-start gap-1">
        {toc.map((item, index) => {
          const level = item.level - highestLevel + 1;

          return (
            <div
              key={index}
              className={level > 1 ? `pl-${(level - 1) * 6}` : ""}
            >
              <Link href={`#${getHeaderId(item.title)}`}>{item.title}</Link>
            </div>
          );
        })}
      </div>

      <div className="hidden pl-6 pl-12 pl-18 pl-24 pl-30"></div>
    </div>
  );
}
