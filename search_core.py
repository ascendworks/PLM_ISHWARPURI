from youtube_search import YoutubeSearch
import json
import time

queries = [
    "Consciousness Ishwar Puri",
    "Awareness Ishwar Puri",
    "Spirituality Ishwar Puri",
    "Spiritual path Ishwar Puri",
    "Mysticism Ishwar Puri",
    "Inner experience Ishwar Puri",
    "Spiritual home Ishwar Puri",
    "Inner home Ishwar Puri",
    "Radha Swami Ishwar Puri",
    "Divine love Ishwar Puri",
    "Surrender Ishwar Puri",
    "Inner sound Ishwar Puri",
    "Inner light Ishwar Puri",
    "Self-realization Ishwar Puri",
    "Enlightenment Ishwar Puri"
]

channels = ['Isha News Media', 'IshwarPuriSantMat', 'i-Seek_YT', 'i-Seek']

results = {}

print("Starting search for core topics")

for query in queries:
    print(f"Searching for: {query}")
    try:
        ys = YoutubeSearch(query, max_results=10)
        res = ys.to_dict()
        print(f"Found {len(res)} results")
        for r in res:
            print(f"Channel: {r['channel']}, Title: {r['title']}")
            if r['channel'] in channels:
                if query not in results:
                    results[query] = []
                results[query].append({
                    'id': r['id'],
                    'title': r['title'],
                    'channel': r['channel'],
                    'description': r.get('description', ''),
                    'publish_time': r.get('publish_time', ''),
                    'views': r.get('views', '')
                })
        time.sleep(1)
    except Exception as e:
        print(f"Error for {query}: {e}")

print("Results:")
print(json.dumps(results, indent=2))

with open('results_core.json', 'w') as f:
    json.dump(results, f, indent=2)