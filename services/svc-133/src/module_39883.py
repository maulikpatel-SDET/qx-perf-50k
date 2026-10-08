"""Service module 39883: business logic, no crypto."""


def calculate_total_39883(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39883():
    return 'module 39883 handles orders and invoices'
