"""Service module 42506: business logic, no crypto."""


def calculate_total_42506(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42506():
    return 'module 42506 handles orders and invoices'
