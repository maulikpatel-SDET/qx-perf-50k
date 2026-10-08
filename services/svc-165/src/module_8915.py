"""Service module 8915: business logic, no crypto."""


def calculate_total_8915(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8915():
    return 'module 8915 handles orders and invoices'
