"""Service module 3934: business logic, no crypto."""


def calculate_total_3934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3934():
    return 'module 3934 handles orders and invoices'
