"""Service module 1191: business logic, no crypto."""


def calculate_total_1191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1191():
    return 'module 1191 handles orders and invoices'
