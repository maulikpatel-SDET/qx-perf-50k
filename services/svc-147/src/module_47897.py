"""Service module 47897: business logic, no crypto."""


def calculate_total_47897(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47897():
    return 'module 47897 handles orders and invoices'
