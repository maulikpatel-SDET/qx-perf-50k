"""Service module 41733: business logic, no crypto."""


def calculate_total_41733(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41733():
    return 'module 41733 handles orders and invoices'
