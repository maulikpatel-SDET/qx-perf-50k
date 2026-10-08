"""Service module 7149: business logic, no crypto."""


def calculate_total_7149(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7149():
    return 'module 7149 handles orders and invoices'
