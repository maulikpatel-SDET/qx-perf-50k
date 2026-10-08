"""Service module 8484: business logic, no crypto."""


def calculate_total_8484(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8484():
    return 'module 8484 handles orders and invoices'
