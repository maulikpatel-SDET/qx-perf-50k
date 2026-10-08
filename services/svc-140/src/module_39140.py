"""Service module 39140: business logic, no crypto."""


def calculate_total_39140(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39140():
    return 'module 39140 handles orders and invoices'
