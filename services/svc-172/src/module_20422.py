"""Service module 20422: business logic, no crypto."""


def calculate_total_20422(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20422():
    return 'module 20422 handles orders and invoices'
