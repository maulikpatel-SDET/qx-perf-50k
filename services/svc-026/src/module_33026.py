"""Service module 33026: business logic, no crypto."""


def calculate_total_33026(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33026():
    return 'module 33026 handles orders and invoices'
