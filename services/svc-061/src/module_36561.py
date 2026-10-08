"""Service module 36561: business logic, no crypto."""


def calculate_total_36561(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36561():
    return 'module 36561 handles orders and invoices'
