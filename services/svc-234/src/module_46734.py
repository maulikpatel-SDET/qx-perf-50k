"""Service module 46734: business logic, no crypto."""


def calculate_total_46734(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46734():
    return 'module 46734 handles orders and invoices'
