"""Service module 5026: business logic, no crypto."""


def calculate_total_5026(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5026():
    return 'module 5026 handles orders and invoices'
