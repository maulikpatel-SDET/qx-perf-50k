"""Service module 33787: business logic, no crypto."""


def calculate_total_33787(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33787():
    return 'module 33787 handles orders and invoices'
