"""Service module 11986: business logic, no crypto."""


def calculate_total_11986(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11986():
    return 'module 11986 handles orders and invoices'
