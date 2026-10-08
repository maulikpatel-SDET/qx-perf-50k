"""Service module 12390: business logic, no crypto."""


def calculate_total_12390(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12390():
    return 'module 12390 handles orders and invoices'
