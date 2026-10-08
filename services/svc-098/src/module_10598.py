"""Service module 10598: business logic, no crypto."""


def calculate_total_10598(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10598():
    return 'module 10598 handles orders and invoices'
