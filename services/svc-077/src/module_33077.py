"""Service module 33077: business logic, no crypto."""


def calculate_total_33077(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33077():
    return 'module 33077 handles orders and invoices'
