"""Service module 42787: business logic, no crypto."""


def calculate_total_42787(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42787():
    return 'module 42787 handles orders and invoices'
