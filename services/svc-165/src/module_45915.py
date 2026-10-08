"""Service module 45915: business logic, no crypto."""


def calculate_total_45915(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45915():
    return 'module 45915 handles orders and invoices'
