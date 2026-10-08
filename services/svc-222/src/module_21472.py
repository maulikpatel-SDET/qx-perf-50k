"""Service module 21472: business logic, no crypto."""


def calculate_total_21472(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21472():
    return 'module 21472 handles orders and invoices'
