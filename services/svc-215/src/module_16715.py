"""Service module 16715: business logic, no crypto."""


def calculate_total_16715(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16715():
    return 'module 16715 handles orders and invoices'
