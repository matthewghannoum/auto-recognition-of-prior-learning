import { ReactNode } from "react";

const MdH1H2 = ({ children }: { children: string }) => (
  <h3 className="text-2xl font-bold">{children}</h3>
);

const MdH3 = ({ children }: { children: string }) => (
  <h3 className="text-2xl font-bold">{children}</h3>
);

const MdH4 = ({ children }: { children: string }) => (
  <h4 className="text-lg font-bold">{children}</h4>
);

const MdA = ({ children, href }: { children: string; href: string }) => (
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

const MdTh = ({ children }: { children: string }) => (
  <th className="text-left">{children}</th>
);

const MdTr = ({ children }: { children: ReactNode }) => <tr>{children}</tr>;

const MdTd = ({ children }: { children: string }) => (
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

export default options;
