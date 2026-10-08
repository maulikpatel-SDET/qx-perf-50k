"""Service module 21949: business logic, no crypto."""


def calculate_total_21949(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21949():
    return 'module 21949 handles orders and invoices'
