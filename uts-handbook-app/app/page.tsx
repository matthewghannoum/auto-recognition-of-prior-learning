import Image from "next/image";
import SearchBar from "./components/search/SearchBar";
import Link from "next/link";
import Footer from "./components/navigation/Footer";

const courseAreas = [
  "Analytics and Data Science",
  "Business",
  "Communication",
  "Creative Intelligence and Innovation",
  "Design, Architecture and Building",
  "Education",
  "Engineering",
  "Health",
  "Information Technology",
  "International Studies",
  "Law",
  "Science",
  "Transdisciplinary Innovation",
];

// list all tailwind colors in array
const colors = [
  "green",
  "pink",
  "rose",
  "teal",
  "yellow",
  "purple",
  "red",
  "emerald",
  "amber",
  "lime",
  "orange",
  "blue",
  "indigo",
];

const colorLevel = "500";

// const hiddenColorImport = colors
//   .map((color) => `bg-${color}-${colorLevel}`)
//   .join(" ");
// console.log(hiddenColorImport);

export default function Home() {
  return (
    <main>
      <div className="w-full min-h-screen bg-black p-16 flex flex-col justify-center items-center gap-6 relative">
        <Link href="/">
          <Image
            className="absolute left-0 top-0"
            alt="UTS logo"
            src="/uts-logo.png"
            width="100"
            height="100"
          />
        </Link>

        <h1 className="text-center text-white font-bold text-6xl">
          University of Technology Sydney <br />
          Handbook
        </h1>

        <h2 className="text-center text-white font-bold text-2xl max-w-2xl">
          The authoritative source of information on approved courses and
          subjects at UTS.
        </h2>

        <SearchBar />

        <div className="flex max-w-6xl justify-center items-center gap-6 flex-wrap mt-6">
          {courseAreas.map((area, index) => (
            <Link
              className={`text-white text-center bg-${colors[index]}-${colorLevel} p-4 rounded-md`}
              href={`/area/${area.toLowerCase().replace(/ /g, "-")}`}
              key={index}
            >
              {area}
            </Link>
          ))}
        </div>
      </div>

      <div className="hidden bg-pink-500 bg-green-500 bg-blue-500 bg-purple-500 bg-red-500 bg-yellow-500 bg-indigo-500 bg-rose-500 bg-teal-500 bg-emerald-500 bg-amber-500 bg-orange-500 bg-lime-500"></div>
    </main>
  );
}
