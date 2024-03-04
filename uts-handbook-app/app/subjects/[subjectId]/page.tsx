import prisma from "@/app/utils/prisma";
import CMarkdown from "@/app/components/content/CMarkdown";
import { Prisma } from "@prisma/client";
import TableOfContents from "@/app/components/content/TableOfContents";

function capitalizeFirstLetter(string: string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

async function getData(subjectId: string) {
  const subject = await prisma.subject.findUnique({
    where: { id: subjectId },
  });
  return { subject };
}

type Requisite = {
  subjectId: string;
  subjectName: string;
}[];

function getRequisitesString(requisites: Prisma.JsonValue[]) {
  const r = requisites as Requisite[];

  if (r.length === 0) return "None";

  return r
    .map((requisiteGroup) => {
      return requisiteGroup
        .map((requisite, index) => {
          return `${requisite.subjectId} ${requisite.subjectName}`;
        })
        .join(" OR ");
    })
    .join(" AND ");
}

// all components are server side rendered by default
export default async function Page({
  params,
}: {
  params: { subjectId: string };
}) {
  const data = await getData(params.subjectId);

  if (!data || !data.subject) {
    return <div>Subject not found</div>;
  }

  const {
    subject: {
      id,
      name,
      sessions,
      creditPoints,
      resultType,
      content,
      requisites,
      antiRequisites,
    },
  } = data;

  const sessions_text = sessions
    .map((s) => capitalizeFirstLetter(s.toLowerCase()))
    .join(", ");

  return (
    <div className="w-full">
      <div className="min-h-[65vh] p-16 flex items-start justify-start gap-16">
        <TableOfContents content={content} />

        <div className="max-w-screen-xl pr-24">
          {data && data.subject && (
            <>
              <div className="flex flex-col items-start justify-start gap-4">
                <h2 className="text-3xl font-bold">
                  {id}: {name}
                </h2>

                <h3 className="text-lg">
                  Credit points: {creditPoints}cp | Sessions: {sessions_text} |
                  Result type: {resultType}
                </h3>

                <h3 className="text-lg">
                  Requisites: {getRequisitesString(requisites)}
                </h3>

                <h3 className="text-lg">
                  AntiRequisites: {getRequisitesString(antiRequisites)}
                </h3>

                <CMarkdown content={content} />
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
