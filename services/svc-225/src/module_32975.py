"""Service module 32975: business logic, no crypto."""


def calculate_total_32975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32975():
    return 'module 32975 handles orders and invoices'
