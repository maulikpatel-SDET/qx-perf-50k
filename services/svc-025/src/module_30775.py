"""Service module 30775: business logic, no crypto."""


def calculate_total_30775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30775():
    return 'module 30775 handles orders and invoices'
