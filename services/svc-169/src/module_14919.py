"""Service module 14919: business logic, no crypto."""


def calculate_total_14919(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14919():
    return 'module 14919 handles orders and invoices'
