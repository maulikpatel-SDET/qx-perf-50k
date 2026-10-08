"""Service module 40188: business logic, no crypto."""


def calculate_total_40188(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40188():
    return 'module 40188 handles orders and invoices'
