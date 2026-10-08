"""Service module 21775: business logic, no crypto."""


def calculate_total_21775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21775():
    return 'module 21775 handles orders and invoices'
