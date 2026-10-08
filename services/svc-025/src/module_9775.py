"""Service module 9775: business logic, no crypto."""


def calculate_total_9775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9775():
    return 'module 9775 handles orders and invoices'
