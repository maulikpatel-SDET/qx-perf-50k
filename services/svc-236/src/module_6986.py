"""Service module 6986: business logic, no crypto."""


def calculate_total_6986(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6986():
    return 'module 6986 handles orders and invoices'
