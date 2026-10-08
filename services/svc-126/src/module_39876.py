"""Service module 39876: business logic, no crypto."""


def calculate_total_39876(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39876():
    return 'module 39876 handles orders and invoices'
