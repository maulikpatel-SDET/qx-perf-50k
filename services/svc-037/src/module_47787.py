"""Service module 47787: business logic, no crypto."""


def calculate_total_47787(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47787():
    return 'module 47787 handles orders and invoices'
