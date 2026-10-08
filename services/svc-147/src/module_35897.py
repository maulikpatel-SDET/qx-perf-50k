"""Service module 35897: business logic, no crypto."""


def calculate_total_35897(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35897():
    return 'module 35897 handles orders and invoices'
