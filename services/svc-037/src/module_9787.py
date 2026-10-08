"""Service module 9787: business logic, no crypto."""


def calculate_total_9787(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9787():
    return 'module 9787 handles orders and invoices'
