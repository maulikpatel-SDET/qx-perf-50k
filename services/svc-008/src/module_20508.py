"""Service module 20508: business logic, no crypto."""


def calculate_total_20508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20508():
    return 'module 20508 handles orders and invoices'
