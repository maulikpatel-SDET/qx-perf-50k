"""Service module 4775: business logic, no crypto."""


def calculate_total_4775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4775():
    return 'module 4775 handles orders and invoices'
