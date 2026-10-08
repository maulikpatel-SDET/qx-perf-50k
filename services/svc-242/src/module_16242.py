"""Service module 16242: business logic, no crypto."""


def calculate_total_16242(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16242():
    return 'module 16242 handles orders and invoices'
