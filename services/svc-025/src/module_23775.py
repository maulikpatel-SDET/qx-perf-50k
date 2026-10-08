"""Service module 23775: business logic, no crypto."""


def calculate_total_23775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23775():
    return 'module 23775 handles orders and invoices'
