"""Service module 32080: business logic, no crypto."""


def calculate_total_32080(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32080():
    return 'module 32080 handles orders and invoices'
