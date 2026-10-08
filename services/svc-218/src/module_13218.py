"""Service module 13218: business logic, no crypto."""


def calculate_total_13218(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13218():
    return 'module 13218 handles orders and invoices'
