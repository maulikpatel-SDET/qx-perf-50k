"""Service module 45080: business logic, no crypto."""


def calculate_total_45080(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45080():
    return 'module 45080 handles orders and invoices'
