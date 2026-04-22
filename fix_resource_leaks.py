import os

fixes = [
    ("src/test/java/com/Rajkaran_122/distributedratelimiter/pipeline/DockerImageTest.java", 81, "static GenericContainer"),
    ("src/test/java/com/Rajkaran_122/distributedratelimiter/ratelimit/ConcurrentPerformanceTest.java", 26, "static GenericContainer"),
    ("src/test/java/com/Rajkaran_122/distributedratelimiter/ratelimit/RedisConnectionPoolTest.java", 32, "static GenericContainer"),
    ("src/test/java/com/Rajkaran_122/distributedratelimiter/TestcontainersConfiguration.java", 15, "static GenericContainer")
]

for path, line_no, content in fixes:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if "@SuppressWarnings(\"resource\")" not in lines[line_no-2]:
            lines.insert(line_no-1, "    @SuppressWarnings(\"resource\")\n")
            with open(path, "w", encoding="utf-8") as f:
                f.writelines(lines)
