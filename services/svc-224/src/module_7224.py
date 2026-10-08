"""Service module 7224: business logic, no crypto."""


def calculate_total_7224(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7224():
    return 'module 7224 handles orders and invoices'
