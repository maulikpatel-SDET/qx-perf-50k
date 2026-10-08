"""Service module 14764: business logic, no crypto."""


def calculate_total_14764(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14764():
    return 'module 14764 handles orders and invoices'
