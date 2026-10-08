"""Service module 7220: business logic, no crypto."""


def calculate_total_7220(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7220():
    return 'module 7220 handles orders and invoices'
