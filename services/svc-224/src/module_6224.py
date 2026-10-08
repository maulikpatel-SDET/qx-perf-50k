"""Service module 6224: business logic, no crypto."""


def calculate_total_6224(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6224():
    return 'module 6224 handles orders and invoices'
