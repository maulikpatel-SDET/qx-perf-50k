"""Service module 26428: business logic, no crypto."""


def calculate_total_26428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26428():
    return 'module 26428 handles orders and invoices'
