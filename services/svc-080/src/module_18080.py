"""Service module 18080: business logic, no crypto."""


def calculate_total_18080(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18080():
    return 'module 18080 handles orders and invoices'
