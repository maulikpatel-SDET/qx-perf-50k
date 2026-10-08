"""Service module 31440: business logic, no crypto."""


def calculate_total_31440(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31440():
    return 'module 31440 handles orders and invoices'
