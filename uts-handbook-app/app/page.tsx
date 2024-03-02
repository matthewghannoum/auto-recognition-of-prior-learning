import Image from "next/image";
import SearchBar from "./components/SearchBar";
import Link from "next/link";

export default function Home() {
  return (
    <main>
      <div className="bg-gray-dark p-16 flex flex-col justify-center items-center gap-6 relative">
        <Link
          href="/"
        >
          <Image
            className="absolute left-0 top-0"
            alt="UTS logo"
            src="/uts-logo.png"
            width="100"
            height="100"
          />
        </Link>

        <h1 className="text-center text-white font-bold text-5xl">
          University of Technology Sydney <br />
          Handbook
        </h1>

        <h2 className="text-center text-white font-bold text-2xl max-w-2xl">
          The authoritative source of information on approved courses and
          subjects at UTS.
        </h2>

        <SearchBar />
      </div>

      <div className="bg-gray p-16">
        <h3 className="text-xl">Recently Viewed</h3>

        <h3 className="text-xl">Frequently Searched Today</h3>
      </div>
    </main>
  );
}
