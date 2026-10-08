"""Service module 38600: business logic, no crypto."""


def calculate_total_38600(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38600():
    return 'module 38600 handles orders and invoices'
