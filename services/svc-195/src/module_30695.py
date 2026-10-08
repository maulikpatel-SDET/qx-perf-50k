"""Service module 30695: business logic, no crypto."""


def calculate_total_30695(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30695():
    return 'module 30695 handles orders and invoices'
