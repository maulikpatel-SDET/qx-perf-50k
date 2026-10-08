"""Service module 787: business logic, no crypto."""


def calculate_total_787(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_787():
    return 'module 787 handles orders and invoices'
