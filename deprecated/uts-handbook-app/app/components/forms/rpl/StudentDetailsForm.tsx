export default function StudentDetailsForm({
  updateField,
}: {
  updateField: (e: any) => void;
}) {
  return (
    <div className="w-full flex flex-col items-start justify-start gap-4">
      <div className="w-full flex flex-col items-start justify-start gap-4">
        <h3 className="text-lg">Personal Details</h3>
        <div className="w-full flex items-start justify-start gap-4">
          <input
            onChange={updateField}
            name="studentNumber"
            type="number"
            placeholder="UTS Student Number"
            className="border-2 border-gray-400 w-full px-4 py-2 rounded-lg"
          />
          <input
            onChange={updateField}
            name="email"
            type="email"
            placeholder="Email"
            className="border-2 border-gray-400 w-full px-4 py-2 rounded-lg"
          />
        </div>

        <div className="w-full flex items-start justify-start gap-4">
          <input
            onChange={updateField}
            name="fName"
            type="text"
            placeholder="Given Name"
            className="border-2 border-gray-400 w-full px-4 py-2 rounded-lg"
          />
          <input
            onChange={updateField}
            name="sName"
            type="text"
            placeholder="Family Name"
            className="border-2 border-gray-400 w-full px-4 py-2 rounded-lg"
          />
        </div>
      </div>

      <div className="w-full flex flex-col items-start justify-start gap-4 ">
        <h3 className="text-lg">UTS Course Details</h3>
        <input
          onChange={updateField}
          name="courseCode"
          type="text"
          placeholder="UTS Course Code"
          className="border-2 border-gray-400 w-full px-4 py-2 rounded-lg"
        />
        <input
          onChange={updateField}
          name="courseName"
          type="text"
          placeholder="UTS Course Name"
          className="border-2 border-gray-400 w-full px-4 py-2 rounded-lg"
        />
      </div>

      <div className="w-full flex flex-col items-start justify-start gap-4">
        <h3 className="text-lg">
          Previous Study, Institution and Award Details
        </h3>
        <input
          onChange={updateField}
          name="prevInstitutionName"
          type="text"
          placeholder="Name of Institution"
          className="border-2 border-gray-400 w-full px-4 py-2 rounded-lg"
        />
        <input
          onChange={updateField}
          name="prevCourseName"
          type="text"
          placeholder="Course Name"
          className="border-2 border-gray-400 w-full px-4 py-2 rounded-lg"
        />
      </div>
    </div>
  );
}
