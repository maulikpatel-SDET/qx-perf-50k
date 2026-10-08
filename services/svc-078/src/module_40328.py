"""Service module 40328: business logic, no crypto."""


def calculate_total_40328(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40328():
    return 'module 40328 handles orders and invoices'
