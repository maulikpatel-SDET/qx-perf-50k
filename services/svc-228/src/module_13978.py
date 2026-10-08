"""Service module 13978: business logic, no crypto."""


def calculate_total_13978(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13978():
    return 'module 13978 handles orders and invoices'
