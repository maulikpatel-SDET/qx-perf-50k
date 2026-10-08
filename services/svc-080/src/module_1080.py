"""Service module 1080: business logic, no crypto."""


def calculate_total_1080(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1080():
    return 'module 1080 handles orders and invoices'
