"""Service module 19775: business logic, no crypto."""


def calculate_total_19775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19775():
    return 'module 19775 handles orders and invoices'
