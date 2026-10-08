"""Service module 39144: business logic, no crypto."""


def calculate_total_39144(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39144():
    return 'module 39144 handles orders and invoices'
