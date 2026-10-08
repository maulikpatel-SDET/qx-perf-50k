"""Service module 48428: business logic, no crypto."""


def calculate_total_48428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48428():
    return 'module 48428 handles orders and invoices'
