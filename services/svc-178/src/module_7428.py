"""Service module 7428: business logic, no crypto."""


def calculate_total_7428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7428():
    return 'module 7428 handles orders and invoices'
