"""Service module 31080: business logic, no crypto."""


def calculate_total_31080(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31080():
    return 'module 31080 handles orders and invoices'
