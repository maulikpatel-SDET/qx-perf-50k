"""Service module 2733: business logic, no crypto."""


def calculate_total_2733(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2733():
    return 'module 2733 handles orders and invoices'
