"""Service module 32787: business logic, no crypto."""


def calculate_total_32787(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32787():
    return 'module 32787 handles orders and invoices'
