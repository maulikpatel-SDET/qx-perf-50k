"""Service module 15733: business logic, no crypto."""


def calculate_total_15733(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15733():
    return 'module 15733 handles orders and invoices'
