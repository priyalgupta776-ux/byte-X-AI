import tlc

PROJECT = "Intel-Scene"

print("Available runs:")
runs = tlc.helpers.project_layout.ProjectLayout.list_run_names(
    project_name=PROJECT
)
print(runs)

for run_name in runs:
    print("\n" + "=" * 60)
    print("RUN:", run_name)

    run = tlc.Run.from_names(
        project_name=PROJECT,
        run_name=run_name,
    )

    print("Run URL:", run.url)
    print("Status:", run.status)

    print("\nMetrics tables:")
    for table in run.metrics_tables:
        print("  URL:", table.url)
        print("  Columns:", table.column_names)
