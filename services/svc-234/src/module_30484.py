"""Service module 30484: business logic, no crypto."""


def calculate_total_30484(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30484():
    return 'module 30484 handles orders and invoices'
