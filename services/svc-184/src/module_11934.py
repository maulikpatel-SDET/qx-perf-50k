"""Service module 11934: business logic, no crypto."""


def calculate_total_11934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11934():
    return 'module 11934 handles orders and invoices'
