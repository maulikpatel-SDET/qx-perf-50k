"""Service module 49390: business logic, no crypto."""


def calculate_total_49390(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49390():
    return 'module 49390 handles orders and invoices'
