"""Service module 6188: business logic, no crypto."""


def calculate_total_6188(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6188():
    return 'module 6188 handles orders and invoices'
