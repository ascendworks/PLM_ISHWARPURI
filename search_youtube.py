from youtube_search import YoutubeSearch
import json
import time

titles = [
    "A Perfect Living Master Must Experience Totality",
    "Spiritual Path: A State of Awareness, Not a Journey",
    "The Endless Sound",
    "Glimpses of Higher Planes",
    "Ravidas's Gift to His Disciple",
    "How to Help the Soul",
    "The Journey Within",
    "The Path to Enlightenment",
    "Socratic Theme: Know Thyself",
    "In the Beginning Was the Word",
    "A Higher Consciousness",
    "Mysticism and Reason",
    "Spiritual Evolution",
    "Spiritual Healing",
    "Intuition and Reason",
    "Path of the Masters"
]

channels = ['Isha News Media', 'IshwarPuriSantmat', 'i-Seek_YT']

results = {}

print("Starting search")

for title in titles:
    query = f'{title} Ishwar Puri'
    print(f"Searching for: {query}")
    try:
        ys = YoutubeSearch(query, max_results=10)
        res = ys.to_dict()
        print(f"Found {len(res)} results")
        for r in res:
            print(f"Channel: {r['channel']}, Title: {r['title']}")
            if r['channel'] in channels:
                if title not in results:
                    results[title] = []
                results[title].append({
                    'id': r['id'],
                    'title': r['title'],
                    'channel': r['channel'],
                    'description': r.get('description', ''),
                    'publish_time': r.get('publish_time', ''),
                    'views': r.get('views', '')
                })
        time.sleep(1)
    except Exception as e:
        print(f"Error for {title}: {e}")

print("Results:")
print(json.dumps(results, indent=2))

with open('results.json', 'w') as f:
    json.dump(results, f, indent=2)