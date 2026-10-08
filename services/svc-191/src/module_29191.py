"""Service module 29191: business logic, no crypto."""


def calculate_total_29191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29191():
    return 'module 29191 handles orders and invoices'
