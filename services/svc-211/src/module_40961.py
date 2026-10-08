"""Service module 40961: business logic, no crypto."""


def calculate_total_40961(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40961():
    return 'module 40961 handles orders and invoices'
