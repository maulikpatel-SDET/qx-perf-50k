"""Service module 2085: business logic, no crypto."""


def calculate_total_2085(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2085():
    return 'module 2085 handles orders and invoices'
