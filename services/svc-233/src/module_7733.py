"""Service module 7733: business logic, no crypto."""


def calculate_total_7733(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7733():
    return 'module 7733 handles orders and invoices'
