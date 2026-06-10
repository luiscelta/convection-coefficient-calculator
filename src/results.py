def showInputs(inputs1Dict, inputs2Dict):
    print("\n" + "=" * 60)
    print("  INPUTS")
    print("=" * 60)
    print("\n  Problem selection:")
    for key, value in inputs1Dict.items():
        if value is not None:
            print(f"    {key}: {value}")
    print("\n  Problem data:")
    for key, value in inputs2Dict.items():
        if isinstance(value, dict):
            for subKey, subValue in value.items():
                if isinstance(subValue, (int, float)):
                    print(f"    {subKey}: {subValue}")
        elif isinstance(value, (int, float)):
            print(f"    {key}: {value}")


def showValidation(result, message):
    print("\n" + "=" * 60)
    print("  VALIDATION")
    print("=" * 60)
    if result is not None:
        print("\n    Successful validation")
    else:
        print(f"\n    Failed validation: {message}")


def showResults(result):
    print("\n" + "=" * 60)
    print("  RESULTS")
    print("=" * 60)
    if result is None:
        return
    print(f"\n    h = {result:.4f} W/m²·K")
    print()