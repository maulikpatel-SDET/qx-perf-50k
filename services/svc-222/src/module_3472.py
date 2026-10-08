"""Service module 3472: business logic, no crypto."""


def calculate_total_3472(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3472():
    return 'module 3472 handles orders and invoices'
