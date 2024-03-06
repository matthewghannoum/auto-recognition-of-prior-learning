"use client";

import { useState } from "react";
import { PDFDownloadLink } from "@react-pdf/renderer";
import Link from "next/link";
import RplPdf from "@/app/components/content/RPLPdf";
import StudentDetailsForm from "@/app/components/forms/rpl/StudentDetailsForm";
import SubjectSimilarityForm from "@/app/components/forms/rpl/SubjectSimilarityForm";

type SubjectIdAndName = { id: string; name: string };

const getSimilarSubjects = async (content: string) => {
  const res = await fetch(
    `${process.env.NEXT_PUBLIC_NLP_API}/search/subject?query=${content}&limit=5`
  );

  if (res.status !== 200) {
    return null;
  }

  const data = await res.json();

  return data as SubjectIdAndName[];
};

export default function Page() {
  const [formData, setFormData] = useState({
    studentNumber: "",
    email: "",
    sName: "",
    fName: "",
    courseCode: "",
    courseName: "",
    prevInstitutionName: "",
    prevCourseName: "",
  });
  const [subjectContent, setSubjectContent] = useState("");
  const [similarSubjects, setSimilarSubjects] = useState<
    SubjectIdAndName[] | null
  >(null);
  const [selectedSubjects, setSelectedSubjects] = useState<SubjectIdAndName[]>(
    []
  );

  const updateStudentDetailsFields = (e: any) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <div className="w-full">
      <div className="min-h-[65vh] p-16 flex items-start justify-start gap-16">
        <div className="max-w-screen-2xl mx-auto flex flex-col items-start justify-start gap-4">
          <div className="w-2/3">
            <h1 className="text-3xl font-bold mb-2">
              Recognition of Prior Learning
            </h1>
            <p>
              Recognition of prior learning (RPL) is a process that allows you
              to gain credit for skills and knowledge you have acquired through
              work and life experience. It can be used to gain entry to a course
              or to gain credit towards a qualification.
            </p>
          </div>

          <div className="w-full flex items-center justify-between gap-6 py-2">
            <form className="w-full flex items-start justify-between gap-10">
              <div className="w-1/3 flex flex-col items-start justify-start gap-10">
                <StudentDetailsForm updateField={updateStudentDetailsFields} />

                <PDFDownloadLink
                  document={<RplPdf {...formData} />}
                  fileName="RPLForm.pdf"
                >
                  {({ blob, url, loading, error }) =>
                    loading ? (
                      "Loading document..."
                    ) : (
                      <div className="text-white max-w-48 text-center bg-blue-700 hover:bg-blue-600 py-2 px-4 rounded-lg">
                        Download RPL Form
                      </div>
                    )
                  }
                </PDFDownloadLink>
              </div>

              <SubjectSimilarityForm
                setSimilarSubjects={async () =>
                  setSimilarSubjects(await getSimilarSubjects(subjectContent))
                }
                setSubjectContent={setSubjectContent}
              />

              <div className="w-1/3 flex flex-col gap-8">
                {selectedSubjects.length > 0 && (
                  <>
                    <div className="w-full flex flex-col items-start justify-start gap-4">
                      <h3 className="text-lg">Selected Subjects</h3>

                      {selectedSubjects.map((subject, index) => (
                        <div
                          key={index}
                          className="w-full flex items-center justify-between gap-4 rounded-xl bg-gray-100 p-4"
                        >
                          <p>
                            {subject.id}: {subject.name}
                          </p>

                          <div className="w-[80px] flex items-center justify-center gap-2">
                            {/* open page icon */}
                            <Link
                              target="_blank"
                              rel="noopener noreferrer"
                              href={`/subjects/${subject.id}`}
                            >
                              <svg
                                className="w-[40px] cursor-pointer"
                                version="1.1"
                                viewBox="0 0 100 100"
                                xmlns="http://www.w3.org/2000/svg"
                              >
                                <g>
                                  <path d="m70 48c-1.1055 0-2 0.89453-2 2v16c0 0.53125-0.21094 1.0391-0.58594 1.4141s-0.88281 0.58594-1.4141 0.58594h-32c-1.1055 0-2-0.89453-2-2v-32c0-1.1055 0.89453-2 2-2h16c1.1055 0 2-0.89453 2-2s-0.89453-2-2-2h-16c-3.3125 0-6 2.6875-6 6v32c0 3.3125 2.6875 6 6 6h32c3.3125 0 6-2.6875 6-6v-16c0-0.53125-0.21094-1.0391-0.58594-1.4141s-0.88281-0.58594-1.4141-0.58594z" />
                                  <path d="m60 32h5.3008l-14.641 14.66c-0.77734 0.78125-0.77734 2.0391 0 2.8203 0.78125 0.77344 2.0391 0.77344 2.8203 0l14.52-14.48v5c0 0.53125 0.21094 1.0391 0.58594 1.4141s0.88281 0.58594 1.4141 0.58594 1.0391-0.21094 1.4141-0.58594 0.58594-0.88281 0.58594-1.4141v-10c0-0.53125-0.21094-1.0391-0.58594-1.4141s-0.88281-0.58594-1.4141-0.58594h-10c-1.1055 0-2 0.89453-2 2s0.89453 2 2 2z" />
                                </g>
                              </svg>
                            </Link>

                            {/* remove icon */}
                            <svg
                              className="w-[20px] cursor-pointer"
                              version="1.1"
                              viewBox="0 0 100 100"
                              xmlns="http://www.w3.org/2000/svg"
                              onClick={() =>
                                setSelectedSubjects(
                                  selectedSubjects.filter(
                                    (s) => s.id !== subject.id
                                  )
                                )
                              }
                            >
                              <g>
                                <path d="m50 0c-27.602 0-50 22.398-50 50s22.398 50 50 50 50-22.398 50-50-22.398-50-50-50zm0 92c-23.199 0-42-18.801-42-42s18.801-42 42-42 42 18.801 42 42-18.801 42-42 42z" />
                                <path d="m70 46h-40c-2.1992 0-4 1.8008-4 4s1.8008 4 4 4h40c2.1992 0 4-1.8008 4-4s-1.8008-4-4-4z" />
                              </g>
                            </svg>
                          </div>
                        </div>
                      ))}
                    </div>

                    <hr className="w-full" />
                  </>
                )}

                {similarSubjects && (
                  <>
                    <div className="w-full flex flex-col items-start justify-start gap-4">
                      <h3 className="text-lg">Similar Subjects</h3>
                      {similarSubjects.map((subject) => (
                        <div
                          className="w-full flex items-center justify-between gap-4 rounded-xl bg-gray-100 p-4"
                          key={subject.id}
                        >
                          <p>
                            {subject.id}: {subject.name}
                          </p>

                          <div className="w-[80px] flex items-center justify-center gap-2">
                            {/* open page icon */}
                            <Link
                              target="_blank"
                              rel="noopener noreferrer"
                              href={`/subjects/${subject.id}`}
                            >
                              <svg
                                className="w-[40px] cursor-pointer"
                                version="1.1"
                                viewBox="0 0 100 100"
                                xmlns="http://www.w3.org/2000/svg"
                              >
                                <g>
                                  <path d="m70 48c-1.1055 0-2 0.89453-2 2v16c0 0.53125-0.21094 1.0391-0.58594 1.4141s-0.88281 0.58594-1.4141 0.58594h-32c-1.1055 0-2-0.89453-2-2v-32c0-1.1055 0.89453-2 2-2h16c1.1055 0 2-0.89453 2-2s-0.89453-2-2-2h-16c-3.3125 0-6 2.6875-6 6v32c0 3.3125 2.6875 6 6 6h32c3.3125 0 6-2.6875 6-6v-16c0-0.53125-0.21094-1.0391-0.58594-1.4141s-0.88281-0.58594-1.4141-0.58594z" />
                                  <path d="m60 32h5.3008l-14.641 14.66c-0.77734 0.78125-0.77734 2.0391 0 2.8203 0.78125 0.77344 2.0391 0.77344 2.8203 0l14.52-14.48v5c0 0.53125 0.21094 1.0391 0.58594 1.4141s0.88281 0.58594 1.4141 0.58594 1.0391-0.21094 1.4141-0.58594 0.58594-0.88281 0.58594-1.4141v-10c0-0.53125-0.21094-1.0391-0.58594-1.4141s-0.88281-0.58594-1.4141-0.58594h-10c-1.1055 0-2 0.89453-2 2s0.89453 2 2 2z" />
                                </g>
                              </svg>
                            </Link>

                            {/* add subject icon */}
                            <svg
                              className="w-[30px] cursor-pointer"
                              version="1.1"
                              viewBox="0 0 100 100"
                              xmlns="http://www.w3.org/2000/svg"
                              onClick={() =>
                                setSelectedSubjects([
                                  ...selectedSubjects,
                                  subject,
                                ])
                              }
                            >
                              <path d="m17.707 25c0-1.7266 1.3984-3.125 3.125-3.125h58.332c1.7266 0 3.125 1.3984 3.125 3.125s-1.3984 3.125-3.125 3.125h-58.332c-1.7266 0-3.125-1.3984-3.125-3.125zm23.957 46.875h-20.832c-1.7266 0-3.125 1.3984-3.125 3.125s1.3984 3.125 3.125 3.125h20.832c1.7266 0 3.125-1.3984 3.125-3.125s-1.3984-3.125-3.125-3.125zm37.5-33.332h-58.332c-1.7266 0-3.125 1.3984-3.125 3.125 0 1.7266 1.3984 3.125 3.125 3.125h58.332c1.7266 0 3.125-1.3984 3.125-3.125 0-1.7266-1.3984-3.125-3.125-3.125zm-37.5 16.668h-20.832c-1.7266 0-3.125 1.3984-3.125 3.125 0 1.7266 1.3984 3.125 3.125 3.125h20.832c1.7266 0 3.125-1.3984 3.125-3.125 0-1.7266-1.3984-3.125-3.125-3.125zm37.5 8.332h-9.375v-9.375c0-1.7266-1.3984-3.125-3.125-3.125-1.7266 0-3.125 1.3984-3.125 3.125v9.375h-9.375c-1.7266 0-3.125 1.3984-3.125 3.125 0 1.7266 1.3984 3.125 3.125 3.125h9.375v9.375c0 1.7266 1.3984 3.125 3.125 3.125 1.7266 0 3.125-1.3984 3.125-3.125v-9.375h9.375c1.7266 0 3.125-1.3984 3.125-3.125 0-1.7266-1.3984-3.125-3.125-3.125z" />
                            </svg>
                          </div>
                        </div>
                      ))}
                    </div>
                  </>
                )}
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}
