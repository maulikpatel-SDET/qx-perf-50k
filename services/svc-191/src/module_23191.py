"""Service module 23191: business logic, no crypto."""


def calculate_total_23191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23191():
    return 'module 23191 handles orders and invoices'
