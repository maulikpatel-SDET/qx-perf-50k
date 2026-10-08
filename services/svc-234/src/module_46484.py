"""Service module 46484: business logic, no crypto."""


def calculate_total_46484(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46484():
    return 'module 46484 handles orders and invoices'
