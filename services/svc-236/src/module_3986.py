"""Service module 3986: business logic, no crypto."""


def calculate_total_3986(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3986():
    return 'module 3986 handles orders and invoices'
