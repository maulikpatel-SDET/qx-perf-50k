"""Service module 22390: business logic, no crypto."""


def calculate_total_22390(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22390():
    return 'module 22390 handles orders and invoices'
