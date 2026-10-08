"""Service module 21836: business logic, no crypto."""


def calculate_total_21836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21836():
    return 'module 21836 handles orders and invoices'
