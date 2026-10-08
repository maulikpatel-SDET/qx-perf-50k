"""Service module 39835: business logic, no crypto."""


def calculate_total_39835(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39835():
    return 'module 39835 handles orders and invoices'
