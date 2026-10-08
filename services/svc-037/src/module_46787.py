"""Service module 46787: business logic, no crypto."""


def calculate_total_46787(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46787():
    return 'module 46787 handles orders and invoices'
