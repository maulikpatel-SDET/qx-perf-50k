"""Service module 21220: business logic, no crypto."""


def calculate_total_21220(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21220():
    return 'module 21220 handles orders and invoices'
