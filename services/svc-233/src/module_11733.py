"""Service module 11733: business logic, no crypto."""


def calculate_total_11733(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11733():
    return 'module 11733 handles orders and invoices'
