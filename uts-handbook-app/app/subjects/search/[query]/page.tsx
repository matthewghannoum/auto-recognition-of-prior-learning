"use client";

import SearchBar from "@/app/components/search/SearchBar";
import { SkeletonCard } from "@/app/components/search/SkeletonCard";
import fetcher from "@/app/utils/fetcher";
import Link from "next/link";
import useSWR from "swr";

type SubjectSearchResult = {
  id: string;
  name: string;
};

const ten_zeros = new Array(10).fill(0);

const SubjectCard = ({ subject }: { subject: SubjectSearchResult }) => {
  return (
    <Link
      className="w-full"
      href={`/subjects/${subject.id}`}
      target="_blank"
      rel="noopener noreferrer"
    >
      <div
        className="h-[120px] w-full rounded-xl bg-gray-100 p-4"
        key={subject.id}
      >
        <h3 className="text-2xl">
          {subject.id}: {subject.name}
        </h3>
      </div>
    </Link>
  );
};

export default function SearchResults({
  params: { query },
}: {
  params: { query: string };
}) {
  let { data, error, isLoading } = useSWR(
    `${
      process.env.NEXT_PUBLIC_NLP_API
    }/search/subject?query=${encodeURIComponent(query)}`,
    fetcher
  );

  let subjectPreviews = data as SubjectSearchResult[];

  return (
    <div className="w-full">
      <div className="w-full flex items-center justify-center gap-4 py-8 bg-neutral-800">
        <SearchBar currentSearchQuery={query} />
      </div>

      <div className="min-h-[65vh] px-16 pb-8 pt-4">
        <div className="mx-auto max-w-screen-lg">
          <div className="w-full flex flex-col items-center justify-center gap-6">
            <h2 className="w-full text-left text-3xl my-4">
              Search Results for: {decodeURIComponent(query)}
            </h2>

            <div className="w-full flex flex-col items-center justify-center gap-4">
              {isLoading && (
                <>
                  {ten_zeros.map((_, i) => (
                    <SkeletonCard key={i} className="h-4 w-[250px]" />
                  ))}
                </>
              )}

              {!isLoading && (
                <>
                  {subjectPreviews &&
                    subjectPreviews.map((subject) => (
                      <SubjectCard key={subject.id} subject={subject} />
                    ))}
                </>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
