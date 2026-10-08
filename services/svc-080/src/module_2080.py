"""Service module 2080: business logic, no crypto."""


def calculate_total_2080(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2080():
    return 'module 2080 handles orders and invoices'
