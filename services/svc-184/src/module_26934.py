"""Service module 26934: business logic, no crypto."""


def calculate_total_26934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26934():
    return 'module 26934 handles orders and invoices'
