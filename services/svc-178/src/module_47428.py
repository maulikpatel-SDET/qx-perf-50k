"""Service module 47428: business logic, no crypto."""


def calculate_total_47428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47428():
    return 'module 47428 handles orders and invoices'
