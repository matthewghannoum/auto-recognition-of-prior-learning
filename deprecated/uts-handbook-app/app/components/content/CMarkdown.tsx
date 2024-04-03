import getHeaderId from "@/app/utils/getHeaderId";
import Markdown from "markdown-to-jsx";
import Link from "next/link";
import { ReactNode } from "react";

const MdH1H2 = ({ children }: { children: string | string[] }) => (
  <h3 id={getHeaderId(children)} className="text-2xl font-bold">
    {children}
  </h3>
);

const MdH3 = ({ children }: { children: string | string[] }) => (
  <h3 id={getHeaderId(children)} className="text-2xl font-bold">
    {children}
  </h3>
);

const MdH4 = ({ children }: { children: string | string[] }) => (
  <h4 id={getHeaderId(children)} className="text-lg font-bold">
    {children}
  </h4>
);

const MdA = ({ children, href }: { children: string | string[]; href: string }) => (
  <Link href={href} className="text-blue hover:text-blue-light">
    {children}
  </Link>
);

const MdOl = ({ children }: { children: ReactNode }) => (
  <ol className="list-inside list-decimal">{children}</ol>
);

const MdUl = ({ children }: { children: ReactNode }) => (
  <ul className="list-inside list-disc">{children}</ul>
);

const MdTable = ({ children }: { children: ReactNode }) => (
  <table className="my-4">{children}</table>
);

const MdTh = ({ children }: { children: string | string[] }) => (
  <th className="text-left">{children}</th>
);

const MdTr = ({ children }: { children: ReactNode }) => <tr>{children}</tr>;

const MdTd = ({ children }: { children: string | string[] }) => (
  <td className="py-2 pr-4 text-left">{children}</td>
);

const MdBr = () => <></>;

const options = {
  overrides: {
    h1: {
      component: MdH1H2,
    },
    h2: {
      component: MdH1H2,
    },
    h3: {
      component: MdH3,
    },
    h4: {
      component: MdH4,
    },
    a: {
      component: MdA,
    },
    ol: {
      component: MdOl,
    },
    ul: {
      component: MdUl,
    },
    table: {
      component: MdTable,
    },
    th: {
      component: MdTh,
    },
    tr: {
      component: MdTr,
    },
    td: {
      component: MdTd,
    },
    br: {
      component: MdBr,
    },
  },
};

type Props = {
  content: string;
  className?: string;
};

export default function CMarkdown({ content, className }: Props) {
  const defaultClassName = "flex flex-col items-start justify-start gap-4";

  return (
    <Markdown
      className={className ? className : defaultClassName}
      options={options}
    >
      {content}
    </Markdown>
  );
}
