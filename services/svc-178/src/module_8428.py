"""Service module 8428: business logic, no crypto."""


def calculate_total_8428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8428():
    return 'module 8428 handles orders and invoices'
