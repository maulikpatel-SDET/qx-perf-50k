"""Service module 42733: business logic, no crypto."""


def calculate_total_42733(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42733():
    return 'module 42733 handles orders and invoices'
