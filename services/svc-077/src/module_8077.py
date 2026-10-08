"""Service module 8077: business logic, no crypto."""


def calculate_total_8077(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8077():
    return 'module 8077 handles orders and invoices'
