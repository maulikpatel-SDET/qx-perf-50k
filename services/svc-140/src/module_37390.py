"""Service module 37390: business logic, no crypto."""


def calculate_total_37390(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37390():
    return 'module 37390 handles orders and invoices'
