"""Service module 42712: business logic, no crypto."""


def calculate_total_42712(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42712():
    return 'module 42712 handles orders and invoices'
