"""Service module 36897: business logic, no crypto."""


def calculate_total_36897(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36897():
    return 'module 36897 handles orders and invoices'
