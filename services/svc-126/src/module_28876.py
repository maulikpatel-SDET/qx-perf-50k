"""Service module 28876: business logic, no crypto."""


def calculate_total_28876(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28876():
    return 'module 28876 handles orders and invoices'
