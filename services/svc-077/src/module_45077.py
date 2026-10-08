"""Service module 45077: business logic, no crypto."""


def calculate_total_45077(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45077():
    return 'module 45077 handles orders and invoices'
