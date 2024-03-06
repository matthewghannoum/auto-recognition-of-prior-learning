import { RplSubjectPair } from "@/app/types";
import { Document, Page, Text, View } from "@react-pdf/renderer";

export default function RplPdf({
  formData,
  selectedSubjects,
}: {
  formData: {
    studentNumber: string;
    email: string;
    sName: string;
    fName: string;
    courseCode: string;
    courseName: string;
    prevInstitutionName: string;
    prevCourseName: string;
  };
  selectedSubjects: RplSubjectPair[];
}) {
  const {
    studentNumber,
    email,
    sName,
    fName,
    courseCode,
    courseName,
    prevInstitutionName,
    prevCourseName,
  } = formData;

  return (
    <Document>
      <Page
        size="A4"
        style={{
          width: "100%",
          padding: "40px",
          display: "flex",
          flexDirection: "column",
          alignItems: "flex-start",
          justifyContent: "flex-start",
          gap: "25px",
        }}
      >
        <View>
          <Text>
            First Name: {fName} | Family Name: {sName}
          </Text>
        </View>

        <View>
          <Text>UTS Student Number: {studentNumber}</Text>
          <Text>Email: {email}</Text>
        </View>

        <View>
          <Text>UTS Course Code: {courseCode}</Text>
          <Text>UTS Course Name: {courseName}</Text>
        </View>

        <View>
          <Text>Previous Study, Institution and Award Details</Text>
          <Text>Name of Institution: {prevInstitutionName}</Text>
          <Text>Course Name: {prevCourseName}</Text>
        </View>

        <View style={{ width: "100%" }}>
          <View style={{ width: "100%" }}>
            <Text>{"UTS Subject(s)"}</Text>
          </View>

          <View>
            {selectedSubjects.map((rplPair, index) => (
              <View
                key={index}
                style={{
                  width: "100%",
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "flex-start",
                  justifyContent: "flex-start",
                  gap: "10px",
                }}
              >
                <Text>
                  {rplPair.utsEquivlaentSubject.id} -{" "}
                  {rplPair.utsEquivlaentSubject.name} |{" "}
                  {rplPair.previousSubject.id} - {rplPair.previousSubject.name}
                </Text>
              </View>
            ))}
          </View>
        </View>
      </Page>
    </Document>
  );
}
