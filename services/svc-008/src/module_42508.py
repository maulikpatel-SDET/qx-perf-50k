"""Service module 42508: business logic, no crypto."""


def calculate_total_42508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42508():
    return 'module 42508 handles orders and invoices'
