"""Service module 49351: business logic, no crypto."""


def calculate_total_49351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49351():
    return 'module 49351 handles orders and invoices'
