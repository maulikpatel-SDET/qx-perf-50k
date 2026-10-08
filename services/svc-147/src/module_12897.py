"""Service module 12897: business logic, no crypto."""


def calculate_total_12897(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12897():
    return 'module 12897 handles orders and invoices'
