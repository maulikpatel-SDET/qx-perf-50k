"""Service module 10091: business logic, no crypto."""


def calculate_total_10091(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10091():
    return 'module 10091 handles orders and invoices'
