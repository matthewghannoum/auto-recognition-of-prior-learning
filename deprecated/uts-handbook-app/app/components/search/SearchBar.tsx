"use client";

import Image from "next/image";
import { useRouter } from "next/navigation";
import { useState } from "react";

type Props = {
  currentSearchQuery?: string | null;
  isLightBg?: boolean;
};

export default function SearchBar({ currentSearchQuery, isLightBg }: Props) {
  const router = useRouter();
  const [searchQuery, setSearchQuery] = useState(
    currentSearchQuery ? decodeURIComponent(currentSearchQuery) : ""
  );

  return (
    <div className="max-w-xl w-full relative">
      <Image
        className="absolute mt-[7px] ml-3"
        alt="search icon"
        src="/search-icon.png"
        width="25"
        height="25"
      />

      <input
        className={`w-full pl-12 py-2 rounded-lg ${
          isLightBg ? "border-black border-2" : ""
        }`}
        type="text"
        placeholder="Search for a subject by name, topic, course content or other details."
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.currentTarget.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter")
            router.push(`/subjects/search/${encodeURIComponent(searchQuery)}`);
        }}
      />
    </div>
  );
}
