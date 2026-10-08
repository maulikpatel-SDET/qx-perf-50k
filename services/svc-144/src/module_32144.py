"""Service module 32144: business logic, no crypto."""


def calculate_total_32144(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32144():
    return 'module 32144 handles orders and invoices'
