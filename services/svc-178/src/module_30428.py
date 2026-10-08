"""Service module 30428: business logic, no crypto."""


def calculate_total_30428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30428():
    return 'module 30428 handles orders and invoices'
