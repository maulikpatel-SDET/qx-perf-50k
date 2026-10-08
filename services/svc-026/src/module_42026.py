"""Service module 42026: business logic, no crypto."""


def calculate_total_42026(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42026():
    return 'module 42026 handles orders and invoices'
