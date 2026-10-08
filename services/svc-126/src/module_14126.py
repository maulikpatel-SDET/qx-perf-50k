"""Service module 14126: business logic, no crypto."""


def calculate_total_14126(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14126():
    return 'module 14126 handles orders and invoices'
