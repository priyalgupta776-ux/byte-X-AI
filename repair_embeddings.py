import tlc

PROJECT_NAME = "Intel-Scene"
RUN_NAME = "orange-packet"

PROJECT_ROOT = "/Users/priyalgupta/Library/Application Support/3LC/projects"

print("Loading existing 3LC run...")

run = tlc.Run.from_names(
    project_name=PROJECT_NAME,
    run_name=RUN_NAME,
    root_url=PROJECT_ROOT,
)

print(f"Run: {run.name}")
print(f"Run URL: {run.url}")

print("\nExisting metrics tables:")
for table in run.metrics_tables:
    print(" ", table.url)

print("\nReducing existing embeddings with UMAP 3D...")

result = run.reduce_embeddings_per_dataset(
    method="umap",
    n_components=3,
    n_neighbors=15,
    n_jobs=1,
    random_state=42,
    delete_source_tables=False,
)

print("\n[OK] Embedding reduction completed.")
print("Reduced tables:")

for original, reduced in result.items():
    print(f"  {original}")
    print(f"      -> {reduced}")

print("\nDone.")
