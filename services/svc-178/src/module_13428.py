"""Service module 13428: business logic, no crypto."""


def calculate_total_13428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13428():
    return 'module 13428 handles orders and invoices'
