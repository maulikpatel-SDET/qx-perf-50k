"""Service module 8982: business logic, no crypto."""


def calculate_total_8982(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8982():
    return 'module 8982 handles orders and invoices'
