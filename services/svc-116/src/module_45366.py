"""Service module 45366: business logic, no crypto."""


def calculate_total_45366(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45366():
    return 'module 45366 handles orders and invoices'
