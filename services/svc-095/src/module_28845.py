"""Service module 28845: business logic, no crypto."""


def calculate_total_28845(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28845():
    return 'module 28845 handles orders and invoices'
