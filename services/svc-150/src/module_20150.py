"""Service module 20150: business logic, no crypto."""


def calculate_total_20150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20150():
    return 'module 20150 handles orders and invoices'
