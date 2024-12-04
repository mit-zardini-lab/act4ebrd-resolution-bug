import yaml
from pathlib import Path


def write_service_network_design_yaml(
    fleet_composition: str,
    avg_travel_time: float,
    output_file_path: Path,
    avg_discomfort_level: float,
    avg_transfers: float,
    avg_hops: float,
    total_emissions: float,
    overwrite: bool = False
):
    # Check if file exists and load existing data if overwrite is False
    if output_file_path.exists():
        with output_file_path.open("r") as file:
            data = yaml.safe_load(file)
    else:
        data = {}

    # Initialize the YAML structure if file is new or overwrite is True
    if overwrite or "F" not in data or "R" not in data:
        data = {
            "F": [
                "satisfied_demand"
            ],
            "R": [
                "`fleet",  # Fixed fleet composition
                "s",  # avg_travel_time
                "Reals",  # avg_discomfort_level
                "Reals",  # avg_transfers
                "Reals",  # avg_hops
                "kg/year",  # total_emissions
            ],
            "implementations": {}
        }

    # Get the current implementation number and add the new entry
    implementations = data.get("implementations", {})
    model_number = len(implementations) + 1
    model_name = f"modelsub{model_number}"

    # Add the new implementation
    implementations[model_name] = {
        "f_max": [
            f"satisfied_demand: demand_1_8_10__2_6_190"
        ],
        "r_min": [
            f"`fleet: {fleet_composition}",
            f"{avg_travel_time} s",
            f"{avg_discomfort_level} Reals",
            f"{avg_transfers} Reals",
            f"{avg_hops} Reals",
            f"{total_emissions} kg/year"
        ]
    }

    data["implementations"] = implementations

    # Write the updated YAML file
    with output_file_path.open("w") as file:
        yaml.dump(data, file, default_flow_style=False)
