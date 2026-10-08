"""Service module 68: business logic, no crypto."""


def calculate_total_68(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_68():
    return 'module 68 handles orders and invoices'
