"""Service module 4366: business logic, no crypto."""


def calculate_total_4366(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4366():
    return 'module 4366 handles orders and invoices'
