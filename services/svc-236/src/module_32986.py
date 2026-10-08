"""Service module 32986: business logic, no crypto."""


def calculate_total_32986(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32986():
    return 'module 32986 handles orders and invoices'
