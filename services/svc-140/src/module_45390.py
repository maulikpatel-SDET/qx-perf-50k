"""Service module 45390: business logic, no crypto."""


def calculate_total_45390(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45390():
    return 'module 45390 handles orders and invoices'
