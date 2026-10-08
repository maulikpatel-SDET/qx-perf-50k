"""Service module 35080: business logic, no crypto."""


def calculate_total_35080(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35080():
    return 'module 35080 handles orders and invoices'
