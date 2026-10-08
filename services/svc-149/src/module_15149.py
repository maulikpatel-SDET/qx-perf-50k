"""Service module 15149: business logic, no crypto."""


def calculate_total_15149(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15149():
    return 'module 15149 handles orders and invoices'
