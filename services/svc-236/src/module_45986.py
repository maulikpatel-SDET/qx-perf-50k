"""Service module 45986: business logic, no crypto."""


def calculate_total_45986(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45986():
    return 'module 45986 handles orders and invoices'
