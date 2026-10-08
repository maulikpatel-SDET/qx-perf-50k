"""Service module 1390: business logic, no crypto."""


def calculate_total_1390(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1390():
    return 'module 1390 handles orders and invoices'
