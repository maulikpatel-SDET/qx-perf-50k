"""Service module 2366: business logic, no crypto."""


def calculate_total_2366(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2366():
    return 'module 2366 handles orders and invoices'
