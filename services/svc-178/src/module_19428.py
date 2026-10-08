"""Service module 19428: business logic, no crypto."""


def calculate_total_19428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19428():
    return 'module 19428 handles orders and invoices'
