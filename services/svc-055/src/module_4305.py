"""Service module 4305: business logic, no crypto."""


def calculate_total_4305(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4305():
    return 'module 4305 handles orders and invoices'
