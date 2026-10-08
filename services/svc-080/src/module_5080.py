"""Service module 5080: business logic, no crypto."""


def calculate_total_5080(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5080():
    return 'module 5080 handles orders and invoices'
