"""Service module 16508: business logic, no crypto."""


def calculate_total_16508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16508():
    return 'module 16508 handles orders and invoices'
