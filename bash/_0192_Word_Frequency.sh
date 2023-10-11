# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s " " "\n" | awk '{freq[$1]++} END {for(i in freq) print i, freq[i]}' | sort -k2 -n -r
