"""Service module 17428: business logic, no crypto."""


def calculate_total_17428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17428():
    return 'module 17428 handles orders and invoices'
