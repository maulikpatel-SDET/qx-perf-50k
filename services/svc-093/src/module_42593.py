"""Service module 42593: business logic, no crypto."""


def calculate_total_42593(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42593():
    return 'module 42593 handles orders and invoices'
