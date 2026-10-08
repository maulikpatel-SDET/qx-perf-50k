"""Service module 7150: business logic, no crypto."""


def calculate_total_7150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7150():
    return 'module 7150 handles orders and invoices'
