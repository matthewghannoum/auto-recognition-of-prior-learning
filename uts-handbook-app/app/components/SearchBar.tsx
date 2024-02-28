import Image from "next/image";

export default function SearchBar() {
  return (
    <div className="max-w-xl w-full relative">
      <Image className="absolute mt-[7px] ml-3" alt="search icon" src="/search-icon.png" width="25" height="25" />

      <input
        className="w-full pl-12 py-2 rounded-lg"
        type="text"
        placeholder="Search for a subject by name, topic, course content or other details."
      />
    </div>
  );
}
