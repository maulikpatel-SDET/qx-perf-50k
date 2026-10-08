"""Service module 7986: business logic, no crypto."""


def calculate_total_7986(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7986():
    return 'module 7986 handles orders and invoices'
