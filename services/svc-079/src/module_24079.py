"""Service module 24079: business logic, no crypto."""


def calculate_total_24079(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24079():
    return 'module 24079 handles orders and invoices'
