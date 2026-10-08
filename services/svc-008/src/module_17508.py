"""Service module 17508: business logic, no crypto."""


def calculate_total_17508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17508():
    return 'module 17508 handles orders and invoices'
