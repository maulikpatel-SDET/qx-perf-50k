"""Service module 49787: business logic, no crypto."""


def calculate_total_49787(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49787():
    return 'module 49787 handles orders and invoices'
