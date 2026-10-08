"""Service module 21971: business logic, no crypto."""


def calculate_total_21971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21971():
    return 'module 21971 handles orders and invoices'
