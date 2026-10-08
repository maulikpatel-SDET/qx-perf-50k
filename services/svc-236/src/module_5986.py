"""Service module 5986: business logic, no crypto."""


def calculate_total_5986(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5986():
    return 'module 5986 handles orders and invoices'
