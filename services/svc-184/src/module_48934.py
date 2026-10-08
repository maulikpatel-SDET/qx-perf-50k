"""Service module 48934: business logic, no crypto."""


def calculate_total_48934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48934():
    return 'module 48934 handles orders and invoices'
