"""Service module 37868: business logic, no crypto."""


def calculate_total_37868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37868():
    return 'module 37868 handles orders and invoices'
