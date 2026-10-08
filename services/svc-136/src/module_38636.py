"""Service module 38636: business logic, no crypto."""


def calculate_total_38636(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38636():
    return 'module 38636 handles orders and invoices'
