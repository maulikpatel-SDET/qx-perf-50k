"""Service module 5484: business logic, no crypto."""


def calculate_total_5484(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5484():
    return 'module 5484 handles orders and invoices'
