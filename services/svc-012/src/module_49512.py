"""Service module 49512: business logic, no crypto."""


def calculate_total_49512(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49512():
    return 'module 49512 handles orders and invoices'
