"""Service module 6428: business logic, no crypto."""


def calculate_total_6428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6428():
    return 'module 6428 handles orders and invoices'
