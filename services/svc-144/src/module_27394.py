"""Service module 27394: business logic, no crypto."""


def calculate_total_27394(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27394():
    return 'module 27394 handles orders and invoices'
