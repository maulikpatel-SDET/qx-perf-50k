"""Service module 42897: business logic, no crypto."""


def calculate_total_42897(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42897():
    return 'module 42897 handles orders and invoices'
