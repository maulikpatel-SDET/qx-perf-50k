"""Service module 7069: business logic, no crypto."""


def calculate_total_7069(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7069():
    return 'module 7069 handles orders and invoices'
