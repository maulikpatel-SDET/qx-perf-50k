"""Service module 20191: business logic, no crypto."""


def calculate_total_20191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20191():
    return 'module 20191 handles orders and invoices'
