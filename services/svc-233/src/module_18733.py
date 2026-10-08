"""Service module 18733: business logic, no crypto."""


def calculate_total_18733(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18733():
    return 'module 18733 handles orders and invoices'
