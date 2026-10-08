"""Service module 25903: business logic, no crypto."""


def calculate_total_25903(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25903():
    return 'module 25903 handles orders and invoices'
