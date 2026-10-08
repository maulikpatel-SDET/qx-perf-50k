"""Service module 39950: business logic, no crypto."""


def calculate_total_39950(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39950():
    return 'module 39950 handles orders and invoices'
