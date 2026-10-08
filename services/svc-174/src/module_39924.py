"""Service module 39924: business logic, no crypto."""


def calculate_total_39924(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39924():
    return 'module 39924 handles orders and invoices'
