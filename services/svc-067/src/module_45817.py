"""Service module 45817: business logic, no crypto."""


def calculate_total_45817(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45817():
    return 'module 45817 handles orders and invoices'
