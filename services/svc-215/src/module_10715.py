"""Service module 10715: business logic, no crypto."""


def calculate_total_10715(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10715():
    return 'module 10715 handles orders and invoices'
