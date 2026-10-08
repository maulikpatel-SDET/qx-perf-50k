"""Service module 29934: business logic, no crypto."""


def calculate_total_29934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29934():
    return 'module 29934 handles orders and invoices'
