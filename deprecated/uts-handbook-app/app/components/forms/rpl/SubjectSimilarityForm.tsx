import { SubjectIdAndName } from "@/app/types";
import { useState } from "react";

export default function SubjectSimilarityForm({
  setSubjectContent,
  setSimilarSubjects,
}: {
  setSubjectContent: (content: string) => void;
  setSimilarSubjects: (subject: SubjectIdAndName) => void;
}) {
  const [previousSubject, setPreviousSubject] = useState<SubjectIdAndName>({
    id: "",
    name: "",
  });

  return (
    <div className="w-1/3 flex flex-col items-start justify-start gap-4 ">
      <h3 className="text-lg">
        Find Similar Subjects based on Content You Studied
      </h3>

      <div className="w-full flex items-center justify-center gap-4">
        <input
          className="w-1/3 border-2 border-gray-400 px-4 py-2 rounded-lg"
          type="text"
          placeholder="Subject Code"
          onChange={(e) => {
            setPreviousSubject({ ...previousSubject, id: e.target.value });
          }}
        />
        <input
          className="w-2/3 border-2 border-gray-400 px-4 py-2 rounded-lg"
          type="text"
          placeholder="Subject Name"
          onChange={(e) => {
            setPreviousSubject({ ...previousSubject, name: e.target.value });
          }}
        />
      </div>

      <textarea
        className="w-full h-96 border-2 border-gray-400 px-4 py-2 rounded-lg"
        onChange={(e) => setSubjectContent(e.target.value)}
        placeholder="Copy and paste the content from your previous University's subject's page, notes you took or a general description of study or work experience."
      ></textarea>

      <div
        className="text-white max-w-48 text-center bg-blue-700 hover:bg-blue-600 py-2 px-4 mt-6 rounded-lg cursor-pointer"
        onClick={() => setSimilarSubjects(previousSubject)}
      >
        Get Similar Subjects
      </div>
    </div>
  );
}
