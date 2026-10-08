"""Service module 12787: business logic, no crypto."""


def calculate_total_12787(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12787():
    return 'module 12787 handles orders and invoices'
