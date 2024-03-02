import prisma from "@/app/utils/prisma";
import Image from "next/image";
import CMarkdown from "@/app/components/CMarkdown";
import { Prisma } from "@prisma/client";

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

  console.log("here", data);

  const sessions_text = sessions
    .map((s) => capitalizeFirstLetter(s.toLowerCase()))
    .join(", ");

  return (
    <>
      {data && data.subject && (
        <main>
          <div className="w-full">
            <div className="flex w-full items-center justify-start bg-black">
              <Image
                alt="UTS logo"
                src="/uts-logo.png"
                width="100"
                height="100"
              />

              <div className="w-full">
                <h1 className="text-center text-3xl font-bold text-white">
                  University of Technology Sydney Handbook
                </h1>
              </div>
            </div>

            <div className="p-16">
              <div className="mx-auto flex max-w-screen-lg flex-col items-start justify-start gap-4">
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
            </div>
          </div>
        </main>
      )}
    </>
  );
}
