"""Service module 26149: business logic, no crypto."""


def calculate_total_26149(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26149():
    return 'module 26149 handles orders and invoices'
