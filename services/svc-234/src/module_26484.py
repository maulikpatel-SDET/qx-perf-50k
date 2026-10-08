"""Service module 26484: business logic, no crypto."""


def calculate_total_26484(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26484():
    return 'module 26484 handles orders and invoices'
