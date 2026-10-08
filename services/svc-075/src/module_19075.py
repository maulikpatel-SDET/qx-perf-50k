"""Service module 19075: business logic, no crypto."""


def calculate_total_19075(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19075():
    return 'module 19075 handles orders and invoices'
