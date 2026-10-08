"""Service module 44242: business logic, no crypto."""


def calculate_total_44242(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44242():
    return 'module 44242 handles orders and invoices'
