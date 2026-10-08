"""Service module 13191: business logic, no crypto."""


def calculate_total_13191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13191():
    return 'module 13191 handles orders and invoices'
