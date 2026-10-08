"""Service module 17978: business logic, no crypto."""


def calculate_total_17978(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17978():
    return 'module 17978 handles orders and invoices'
