"""Service module 14191: business logic, no crypto."""


def calculate_total_14191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14191():
    return 'module 14191 handles orders and invoices'
