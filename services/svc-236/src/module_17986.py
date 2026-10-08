"""Service module 17986: business logic, no crypto."""


def calculate_total_17986(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17986():
    return 'module 17986 handles orders and invoices'
