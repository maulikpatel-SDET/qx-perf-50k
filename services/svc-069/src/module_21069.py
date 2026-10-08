"""Service module 21069: business logic, no crypto."""


def calculate_total_21069(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21069():
    return 'module 21069 handles orders and invoices'
