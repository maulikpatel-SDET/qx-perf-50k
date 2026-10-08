"""Service module 35224: business logic, no crypto."""


def calculate_total_35224(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35224():
    return 'module 35224 handles orders and invoices'
