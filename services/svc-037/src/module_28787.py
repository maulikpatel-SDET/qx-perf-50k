"""Service module 28787: business logic, no crypto."""


def calculate_total_28787(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28787():
    return 'module 28787 handles orders and invoices'
