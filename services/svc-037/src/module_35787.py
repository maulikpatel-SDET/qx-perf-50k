"""Service module 35787: business logic, no crypto."""


def calculate_total_35787(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35787():
    return 'module 35787 handles orders and invoices'
