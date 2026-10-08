"""Service module 12026: business logic, no crypto."""


def calculate_total_12026(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12026():
    return 'module 12026 handles orders and invoices'
