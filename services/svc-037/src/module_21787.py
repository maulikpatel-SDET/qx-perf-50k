"""Service module 21787: business logic, no crypto."""


def calculate_total_21787(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21787():
    return 'module 21787 handles orders and invoices'
