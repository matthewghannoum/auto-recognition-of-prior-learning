"use client";

import { useState } from "react";
import {
  Document,
  PDFViewer,
  Page as PDFPage,
  View,
  Text,
  PDFDownloadLink,
} from "@react-pdf/renderer";

const RPLForm = (formData: {
  studentNumber: string;
  email: string;
  sName: string;
  fName: string;
  courseCode: string;
  courseName: string;
  prevInstitutionName: string;
  prevCourseName: string;
}) => {
  return (
    <Document>
      <PDFPage size="A4">
        <View>
          <Text>
            First Name: {formData.fName} | Family Name: {formData.sName}
          </Text>
        </View>

        <View>
          <Text>UTS Student Number: {formData.studentNumber}</Text>
          <Text>Email: {formData.email}</Text>
        </View>

        <View>
          <Text>UTS Course Code: {formData.courseCode}</Text>
          <Text>UTS Course Name: {formData.courseName}</Text>
        </View>

        <View>
          <Text>Previous Study, Institution and Award Details</Text>
          <Text>Name of Institution: {formData.prevInstitutionName}</Text>
          <Text>Course Name: {formData.prevCourseName}</Text>
        </View>
      </PDFPage>
    </Document>
  );
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

  const updateField = (e: any) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <div className="w-full">
      <div className="min-h-[65vh] p-16 flex items-start justify-start gap-16">
        <div className="max-w-screen-lg mx-auto flex flex-col items-start justify-start gap-6">
          <h1 className="text-3xl font-bold">Recognition of Prior Learning</h1>
          <p>
            Recognition of prior learning (RPL) is a process that allows you to
            gain credit for skills and knowledge you have acquired through work
            and life experience. It can be used to gain entry to a course or to
            gain credit towards a qualification.
          </p>

          <div className="w-full flex items-center justify-between gap-6">
            <form>
              <div className="flex flex-col items-start justify-start gap-4 py-4">
                <h3 className="text-lg">Personal Details</h3>
                <div className="flex items-start justify-start gap-4">
                  <input
                    onChange={updateField}
                    name="studentNumber"
                    type="number"
                    placeholder="UTS Student Number"
                    className="border-2 border-gray-400 min-w-96 px-4 py-2 rounded-lg"
                  />
                  <input
                    onChange={updateField}
                    name="email"
                    type="email"
                    placeholder="Email"
                    className="border-2 border-gray-400 min-w-96 px-4 py-2 rounded-lg"
                  />
                </div>

                <div className="flex items-start justify-start gap-4">
                  <input
                    onChange={updateField}
                    name="fName"
                    type="text"
                    placeholder="Given Name"
                    className="border-2 border-gray-400 min-w-96 px-4 py-2 rounded-lg"
                  />
                  <input
                    onChange={updateField}
                    name="sName"
                    type="text"
                    placeholder="Family Name"
                    className="border-2 border-gray-400 min-w-96 px-4 py-2 rounded-lg"
                  />
                </div>
              </div>

              <div className="w-full flex flex-col items-start justify-start gap-4 py-4">
                <h3 className="text-lg">UTS Course Details</h3>
                <input
                  onChange={updateField}
                  name="courseCode"
                  type="text"
                  placeholder="UTS Course Code"
                  className="border-2 border-gray-400 min-w-96 px-4 py-2 rounded-lg"
                />
                <input
                  onChange={updateField}
                  name="courseName"
                  type="text"
                  placeholder="UTS Course Name"
                  className="border-2 border-gray-400 min-w-96 px-4 py-2 rounded-lg"
                />
              </div>

              <div className="flex flex-col items-start justify-start gap-4 py-4">
                <h3 className="text-lg">
                  Previous Study, Institution and Award Details
                </h3>
                <input
                  onChange={updateField}
                  name="prevInstitutionName"
                  type="text"
                  placeholder="Name of Institution"
                  className="border-2 border-gray-400 min-w-96 px-4 py-2 rounded-lg"
                />
                <input
                  onChange={updateField}
                  name="prevCourseName"
                  type="text"
                  placeholder="Course Name"
                  className="border-2 border-gray-400 min-w-96 px-4 py-2 rounded-lg"
                />
              </div>

              <PDFDownloadLink
                document={<RPLForm {...formData} />}
                fileName="RPLForm.pdf"
              >
                {({ blob, url, loading, error }) =>
                  loading ? (
                    "Loading document..."
                  ) : (
                    <div className="text-white max-w-48 text-center bg-blue-700 hover:bg-blue-600 py-2 px-4 mt-6 rounded-lg">
                      Download RPL Form
                    </div>
                  )
                }
              </PDFDownloadLink>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}
