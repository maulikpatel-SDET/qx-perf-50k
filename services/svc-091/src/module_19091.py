"""Service module 19091: business logic, no crypto."""


def calculate_total_19091(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19091():
    return 'module 19091 handles orders and invoices'
