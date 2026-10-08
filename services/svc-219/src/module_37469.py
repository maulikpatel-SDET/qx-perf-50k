"""Service module 37469: business logic, no crypto."""


def calculate_total_37469(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37469():
    return 'module 37469 handles orders and invoices'
