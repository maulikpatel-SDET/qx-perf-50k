"""Service module 18982: business logic, no crypto."""


def calculate_total_18982(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18982():
    return 'module 18982 handles orders and invoices'
